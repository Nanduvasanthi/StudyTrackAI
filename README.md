#  StudyTrackAI

A smart study tracking platform that helps students monitor their study progress with AI-powered notifications and personalized reminders.


##  Key Features

###  Authentication & User Management
 **Student Registration & Login**: Secure user authentication system  
 **Admin Dashboard**: Comprehensive admin interface for user management  
 **Role-based Access**: Separate views for students and administrators  

###  Study Tracking & Analytics
 **Personalized Dashboards**: Individual study track display for each user  
 **Course Progress Monitoring**: Track completion percentage for different courses  
 **Multi-course Support**: Support for different courses with varying durations per user  

###  AI-Powered Notifications
 **Smart Email Reminders**: Automated notifications sent at morning, afternoon, and evening  
 **Course Completion Alerts**: Notifications for courses with high completion (75%+)  
 **Quiz Reminders**: Automated reminders for pending quizzes  
 **Progress-based Triggers**: AI-driven notification system based on user progress  

###  Dashboard Features
 **High Completion Alerts**: Pop-up notifications for nearly completed courses  
 **Real-time Progress Tracking**: Live updates on course completion percentages  
 **User-specific Data**: Each user sees only their own study tracks and courses  

### Screenshots

### Authentication & User Management
<div align="center"> <table> <tr> <td align="center" width="50%"> <strong>Login Page</strong><br> <img width="840" height="692" alt="Login Page" src="https://github.com/user-attachments/assets/4dcf1369-8e49-4982-b8a2-1682e31d1029" /> </td> <td align="center" width="50%"> <strong>Registration Page</strong><br> <img width="480" height="788" alt="Registration Page" src="https://github.com/user-attachments/assets/e058da92-27a0-46a4-bf4a-676011f9c16f" /> </td> </tr> </table> <p><em>Secure student authentication system with login and registration</em></p> </div>

### Student Dashboard & Study Tracking

<div align="center"> <img width="1897" height="865" alt="Student Dashboard" src="https://github.com/user-attachments/assets/9f4f8956-9a95-4590-83af-8489c2b93d37" /> <p><em>Personalized dashboard with real-time progress tracking</em></p> </div>

### Multi-Course Support & Analytics

<div align="center"> <table> <tr> <td align="center" width="50%"> <strong>My Courses</strong><br> <img width="1919" height="859" alt="My Courses" src="https://github.com/user-attachments/assets/09c23779-23a4-4151-a038-f50c49ae61b9" /> </td> <td align="center" width="50%"> <strong>Progress Analytics</strong><br> <img width="1916" height="860" alt="Progress Analytics" src="https://github.com/user-attachments/assets/f65b2125-00e6-4850-b1ee-9e52b95c9fba" /> </td> </tr> </table> <p><em>Support for multiple courses with detailed progress analytics</em></p> </div>

### AI-Powered Notifications

<div align="center"> <table> <tr> <td align="center" width="50%"> <strong>Email Notifications</strong><br> <img width="1661" height="506" alt="Email Notifications" src="https://github.com/user-attachments/assets/a01316bd-7b31-4349-9a7d-8ad4d23ce33a" /> </td> <td align="center" width="50%"> <strong>Pop-up Alerts</strong><br> <img width="1564" height="790" alt="Pop-up Alerts" src="https://github.com/user-attachments/assets/70729646-c364-4f8e-b3e2-60c4a6bb1157" /> </td> </tr> </table> <p><em>Smart email reminders and real-time pop-up notifications for course completion</em></p> </div>

### User Profile & Settings

<div align="center"> <img width="1907" height="872" alt="User Profile" src="https://github.com/user-attachments/assets/9754753d-68c9-4173-b643-f08bae1d8716" /> <p><em>User profile management and notification preferences</em></p> </div>


##  Technologies Used

### Backend
 **Django 4.0+** – Python web framework  
 **MySQL** – Database management system  
 **Celery** – Distributed task queue for background tasks  
 **django-celery-results** – Store Celery task results in Django database  

### Frontend
 **HTML / CSS / JavaScript** – Core frontend technologies  
 **Bootstrap** – CSS framework (via `django-widget-tweaks`)  
 **Django Templates** – Server-side rendering  

### Email & Notifications
 **SMTP (Gmail)** – Email service for notifications  
 **Custom Email Backend** – Tailored email configuration  
 **SSL/TLS** – Secure email transmission  

### Task Scheduling
 **Celery Beat** – Periodic task scheduler  
 **Background Workers** – Asynchronous task processing  

### Security & Authentication
 **Django Auth** – Built-in authentication system  
 **Custom User Model** – Extended user functionality  
 **CSRF Protection** – Cross-site request forgery protection  
 **Session Management** – Secure user sessions  



##  Prerequisites

Before running this project, make sure you have installed:

 **Python 3.8+**
 **MySQL Server**
 **Git**



##  Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nanduvasanthi/StudyTrackAI.git
cd StudyTrackAI
```

### 2️⃣ Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

```

### 3️⃣ Install Dependencies
```bash
pip install django
pip install mysqlclient
pip install celery
pip install django-celery-results
pip install django-widget-tweaks
```

### 4️⃣ Setup MySQL Database
Make sure MySQL is running, then create a database:
```bash
mysql -u root -p -e "CREATE DATABASE studytrack;"
```

### 5️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```

Then open your browser and visit:  
👉 http://127.0.0.1:8000/

---

##  Additional Commands (Optional)

### Start Celery Worker
```bash
celery -A studytrack worker -l info
```

### Start Celery Beat (for scheduled tasks)
```bash
celery -A studytrack beat -l info
```

---

##  License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

[ Download StudyTrack Presentation](./StudyTrack.pptx)






