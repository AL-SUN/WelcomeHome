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

### Frontend:

- TypeScript
- React

### Backend:

  - Python
  - Flask

### Database:

  - MySQL

## 📥 Setup & Installation

To run this project locally, follow these steps:

1️⃣ **Clone the repository**:  

```bash
git clone https://github.com/AL-SUN/WelcomeHome.git
cd WelcomeHome
```

---

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

---

3️⃣ **Configure the Database**

1. Ensure **MySQL** is installed and running on your local machine.

2. Update the `config.py` file in the `backend/` folder to match your MySQL database settings (user, password, host and port).

---

4️⃣ **Import the Database Schema & Seed Data**

1. Start your MySQL server.

2. Import the SQL files to set up the database schema and populate it with sample data. 

   Use graphic interface to import `projectTableDefs-v2.sql` and `examplesData.sql` in `backend` folder.
   Or run following commands (replace `your_db_user` and `your_database_name`):

  ```bash
  mysql -u your_db_user -p your_database_name < backend/projectTableDefs-v2.sql
  mysql -u your_db_user -p your_database_name < backend/examplesData.sql
  ```

---

5️⃣ **Start the Development Servers**

1. **Start the backend:** Run the following command in the `backend/` folder:

  ```bash
  python app.py 
  ```

The backend server will run on http://localhost:5000 (default Flask port).

2. **Start the frontend:** Run the following command in the `frontend/` folder:

  ```bash
  npm start  # Run in frontend folder
  ```

  The frontend will be available at http://localhost:3000.


#### **⚠️ Important Notes**

- **Both the frontend and backend servers must be running simultaneously** to access the full application.
- If you encounter issues connecting to MySQL, double-check your `config.py` settings and MySQL server status.
