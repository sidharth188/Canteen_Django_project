# Canteen Management System

This is a Django-based web application designed to manage and streamline operations for a canteen. It includes features for booking, menu browsing, and administrative control.

## 📹 Demo Video
[Watch Here]([https://drive.google.com/file/d/YOUR_FILE_ID/view](https://drive.google.com/file/d/1U4x5CE_LJjgB5AWu2NiUA363nTwKnank/view?usp=drive_link))

## 🚀 Features

- Homepage with navigation
- Menu page to display available items
- Booking functionality
- Admin panel for managing data
- SQLite database for storage

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (static templates)
- **Backend**: Django (Python)
- **Database**: SQLite3

## 📂 Project Structure

canteen/ ├── about.html ├── book.html ├── index.html ├── menu.html └── Canteen_project/ ├── db.sqlite3 ├── manage.py ├── requirements.txt └── Base_App/ ├── admin.py ├── apps.py ├── models.py ├── views.py ├── tests.py └── migrations

## 🧑‍💻 Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/canteen-management.git
    cd canteen-management/canteen/Canteen_project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the site**:
    Open your browser and go to `http://127.0.0.1:8000/`

## 📝 License

This project is open-source and free to use under the MIT License.

---

## 🖼️ Screenshots

### 🍽️ Login Page
![Menu Page](Screenshot%20(42).png)

### 🍽️ Register Page
![Menu Page](Screenshot%20(43).png)

### 🏠 Home Page
![Home Page](Screenshot%20(30).png)

### ℹ️ About Page
![About Page](Screenshot%20(32).png)

### 🍽️ Feedback Page
![Menu Page](Screenshot%20(33).png)

### 🍽️ Feedback View Page
![Menu Page](Screenshot%20(34).png)

### 🍽️ Menu Page
![Menu Page](Screenshot%20(31).png)

### 📅 Empty Cart Page
![Booking Page](Screenshot%20(35).png)

### 🍽️ added to cart Page
![Menu Page](Screenshot%20(36).png)

### 🍽️ Cart Page
![Menu Page](Screenshot%20(37).png)

### 🍽️ Payment view Page
![Menu Page](Screenshot%20(38).png)

### 🍽️ Payment Page
![Menu Page](Screenshot%20(39).png)

### 🍽️ Adminlogin Page
![Menu Page](Screenshot%20(40).png)

### 🍽️ Admin View Page
![Menu Page](Screenshot%20(41).png)

### 🍽️ aboutus Page
![Menu Page](Screenshot%20(43).png)
