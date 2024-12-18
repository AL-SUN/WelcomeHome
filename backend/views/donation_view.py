# views/donation_views.py
from datetime import datetime
from flask import Blueprint, app, request, jsonify
from .auth_view import staff_required
from utils import get_db_connection, process_string_value

donation_bp = Blueprint('donation_bp', __name__)


@donation_bp.route('/categories', methods=['GET'])
def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named access

    cursor.execute("SELECT mainCategory, subCategory, catNotes FROM Category")
    categories = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return jsonify(categories)

@donation_bp.route('/locations', methods=['GET'])
def get_locations():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get all locations except the preparation room
    cursor.execute("SELECT roomNum, shelfNum, shelf, shelfDescription FROM Location WHERE roomNum != -1 AND shelfNum != -1")
    locations = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return jsonify(locations)

@donation_bp.route('/donations', methods=['GET'])
def get_donations():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DonatedBy")
    donations = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(donations)

@donation_bp.route('/donations', methods=['POST'])
def create_donation():
    new_donation = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO DonatedBy (ItemID, userName, donateDate) VALUES (%s, %s, %s)",
                   (new_donation['ItemID'], new_donation['userName'], new_donation['donateDate']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_donation), 201



@donation_bp.route('/accept_donation', methods=['POST'])
@staff_required
def accept_donation():
    data = request.get_json()
    user_name = data.get('userName')
    items = data.get('items')  # Expecting a list of items, each containing multiple pieces

    if not user_name or not items:
        return jsonify({"error": "userName and items are required."}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if the user is a registered donor
    cursor.execute("""
        SELECT * FROM Act WHERE userName = %s AND roleID = 'donor'
    """, (user_name,))
    donor_check = cursor.fetchone()

    if not donor_check:
        return jsonify({"error": "User is not a registered donor."}), 403

    try:
        for item in items:
            # Check if the item has pieces
            pieces = item.get('pieces')
            if not pieces:
                return jsonify({"error": "Each item must have one piece at least."}), 400
            
            # Check mainCategory and subCategory
            if not item.get('mainCategory') or not item.get('subCategory'):
                return jsonify({"error": "Each item must have mainCategory and subCategory."}), 400
            
            # Process string values
            iDescription= process_string_value(item.get('iDescription'))
            color = process_string_value(item.get('color'))
            material = process_string_value(item.get('material'))
                        
            cursor.execute("""
                INSERT INTO Item (iDescription, color, isNew, hasPieces, material, mainCategory, subCategory)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (iDescription, color, item.get('isNew'), False # if change table schema, hasPieces not needed
                  , material, item.get('mainCategory'), item.get('subCategory')))
            
            # Get the last inserted ItemID
            item_id = cursor.lastrowid

            # Insert each piece associated with this item
            for piece in pieces:
                piece_num = piece.get('pieceNum')
                room_num = piece.get('roomNum')
                shelf_num = piece.get('shelfNum')
                
                if not room_num or not shelf_num:
                    return jsonify({"error": "Each piece must have roomNum, and shelfNum."}), 400
                
                # Process string values
                pDescription = process_string_value(piece.get('pDescription'))
                pNotes = process_string_value(piece.get('pNotes'))

                cursor.execute("""
                    INSERT INTO Piece (ItemID, pieceNum, pDescription, length, width, height, roomNum, shelfNum, pNotes)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (item_id, piece_num, pDescription, piece.get('length'), 
                       piece.get('width'), piece.get('height'), room_num, shelf_num, pNotes))
            
            # Insert the donation record into DonatedBy
            donation_date = datetime.now().date()  # Assuming you want the current date
            cursor.execute("""
                INSERT INTO DonatedBy (ItemID, userName, donateDate)
                VALUES (%s, %s, %s)
            """, (item_id, user_name, donation_date))

        connection.commit()
    except Exception as e:
        connection.rollback()
        return jsonify({"error": f"Donation acceptance failed: {str(e)}"}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({"message": "Donation accepted successfully."}), 200
    
@donation_bp.route('/check_donor', methods=['POST'])
@staff_required
def check_donor():
    data = request.get_json()
    user_name = data.get('userName')

    if not user_name:
        return jsonify({"error": "userName is required."}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT * FROM Act WHERE userName = %s AND roleID = 'donor'
        """, (user_name,))
        donor_check = cursor.fetchone()
    except Exception as e:
        return jsonify({"error": f"Error checking donor: {str(e)}"}), 500
    finally:
        cursor.close()
        connection.close()

    if donor_check:
        return jsonify({"isDonor": True}), 200
    else:
        return jsonify({"isDonor": False}), 200