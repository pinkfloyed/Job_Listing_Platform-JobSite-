# Job_Listing_Platform-JobSite-
This project is based on Django REST backend for a job listing platform supporting role-based access (Recruiter, Candidate). Implements JWT auth, email-based registration and password reset, job CRUD operations, candidate applications, a recruiter dashboard, and auto-generated Swagger API docs.


# JobSite Backend

A role-based job listing platform backend built with Django REST Framework.

## Features

- User registration and JWT authentication
- Role-based access control (Recruiter, Candidate)
- Job posting CRUD operations (Recruiters only)
- Job applications (Candidates only)
- Password reset via email
- Recruiter dashboard with stats
- Swagger/OpenAPI documentation

## 📄 Applications
- Candidates can apply to jobs
- Application constraints:
- Cannot apply after job deadline
- Cannot apply multiple times to the same job

## 📊 Recruiter Dashboard
**View total:**
- Published jobs
- Closed jobs
- Candidate applications
- Candidates hired
- Candidates rejected
---

## 🚀 Getting Started

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT for authentication
- drf-yasg for API documentation

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/jobsite-backend.git
cd jobsite-backend
```

2. **Create and activate virtual environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Configure environment variables**
```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True
```
5. **Run migrations**
```bash
python manage.py migrate
```
6. **Run the development server**
```bash
python manage.py runserver
```
7. **Access Swagger API docs**
Visit: http://127.0.0.1:8000/swagger/

---

## 📁 Project Structure

```text
jobsite/
├── auth/                 # Authentication app (register, login, password)
├── job/                  # Jobs and applications logic
├── core/                 # Custom user model, profiles
├── config/               # Django project settings
├── templates/            # (If using any)
├── media/                # Uploaded files (if any)
├── requirements.txt
└── .env                  # Sensitive configs (not committed)
└── README.md
```

---

## API Endpoints

### Auth:
- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/token/` - Obtain JWT token
- `POST /api/v1/auth/forgot-password/` - Request password reset email
- `POST /api/v1/auth/reset-password/` - Reset password using token
- `POST /api/v1/auth/tokenrefresh/` - Refresh JWT token

### Jobs:
- `GET /jobs/all/` - List all available jobs (public)
- `POST /jobs/jobs/create/` - Create a new job (Recruiter only)
- `DELETE /jobs/jobs/{id}/delete/` - Delete a job (Recruiter only)
- `GET /jobs/jobs/{id}/update/` - Retrieve job details for update (Recruiter only)
- `PUT /jobs/jobs/{id}/update/` - Update a job (Recruiter only)
- `PATCH /jobs/jobs/{id}/update/` - Partially update a job (Recruiter only)

### Job Applications:
- `POST /jobs/jobs/apply/` - Apply to a job (Candidate only)

### Dashboard:
- `GET /jobs/recruiter/dashboard/` - Get recruiter dashboard statistics

---

## License

This project is licensed under the MIT License.

