# 🌍WelcomeHome Web Application

**The project aims to build a web interface for Welcome Home, a non-profit organization that assists refugees and asylum seekers. This web application allows administrators to track donations, manage client orders, and oversee delivery logistics — all in one place.**

🎯**Key Objectives:**

- Streamline donation tracking and order fulfillment.
- Facilitate effective coordination between staff, donors, volunteers, and clients.
- Provide a secure, user-friendly experience for different roles.

## ✨ Features

- **Order Management**: Track and manage client orders from request to delivery.
- **Donation Tracking**: Track donations and their availability for orders.
- **Delivery Scheduling**: Plan and manage delivery routes to optimize efficiency.
- **Role-based Access Control**: Secure access for staff, client, donors, and volunteers.
- **Rank System**: Track volunteer contributions and recognize top participants.

## 🛠️ Tech Stack

<table>
  
  <tr>
    <td><strong>Frontend</strong></td>
    <td>TypeScript, React</td>
  </tr>
  <tr>
    <td><strong>Backend</strong></td>
    <td>Python, Flask</td>
  </tr>
  <tr>
    <td><strong>Database</strong></td>
    <td>MySQL</td>
  </tr>
</table>


## 📥 Setup & Installation

To run this project locally, follow these steps:

1️⃣ **Clone the repository**:  

```bash
git clone https://github.com/AL-SUN/WelcomeHome.git
cd WelcomeHome
```

##

2️⃣ **Install dependencies**:

1. **Frontend**: Make sure you have [Node.js](https://nodejs.org/)  installed.

```bash
cd frontend # Navigate to the frontend folder
npm install
```

2. **Backend**: Make sure you have Python and pip installed.

```bash
cd ../backend # Navigate to the backend folder
pip install -r requirements.txt
```

##

3️⃣ **Configure the Database**

1. Ensure **MySQL** is installed and running on your local machine.

2. Update the `config.py` file in the `backend/` folder to match your MySQL database settings (user, password, host and port).

##

4️⃣ **Import the Database Schema & Seed Data**

1. Start your MySQL server.

2. Import the SQL files to set up the database schema and populate it with sample data, using `projectTableDefs-v2.sql` and `examplesData.sql` in `backend/` folder.
##

5️⃣ **Start the Development Servers**

1. **Start the backend:** Run the following command in the `backend/` folder:

  ```bash
  python app.py 
  ```

The backend server will run on http://localhost:5000 (default Flask port).

2. **Start the frontend:** Run the following command in the `frontend/` folder:

  ```bash
  npm start 
  ```

  The frontend will be available at http://localhost:3000.

#### **⚠️ Important Notes**

- **Both the frontend and backend servers must be running simultaneously** to access the full application.
- If you encounter issues connecting to MySQL, double-check your `config.py` settings and MySQL server status.


<details>
  <summary>Stay tuned for future developments! 🚀</summary>
  
## 💡 Future Enhancements

To further improve the WelcomeHome application, here are some key features and improvements we plan to implement:

1. **Image Upload Support**  
   - Enable users to upload images for donations and submissions.  
   - Update the database to store image references.  
   - Display uploaded images in donation details and client orders.  

2. **Enhanced Frontend Information Display**  
   - Improve the presentation of data on the frontend for better readability and clarity.  
   - Optimize how donation, order, and delivery information is displayed to users.  

3. **UI/UX Improvements**  
   - Redesign the UI for a more modern and visually appealing experience.  
   - Enhance navigation and user experience (UX) for administrators, donors, and volunteers.  

4. **Notification System**  
   - Implement a system to notify users of order status updates.  
   - Provide real-time updates for order changes and delivery schedules.  
5. **Data Visualization & Analytics**  
   - Create dashboards to display trends in donations, orders, and volunteer activities.  
   - Use charts and graphs to provide insights for administrators.
   - Prepare data for a year-end report with key information for grant applications.

6. **Security Enhancements**  
   - Conduct regular security audits to protect against vulnerabilities like SQL injection and XSS.  
   - Implement robust input validation and sanitization for all user inputs.

(Planned for Winter Break)
</details>
