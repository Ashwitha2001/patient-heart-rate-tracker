# Patient Heart Rate Tracker API

This is a Django REST framework-based API for tracking patient heart rates. It includes user authentication, role-based access, patient management, heart rate recording, filtering, pagination, and validation.

## Features
- **User Authentication:** Register and log in users.
- **Role-Based Access:** Users can have roles like `Doctor` or `Nurse`.
- **Patient Management:** Create and retrieve patients linked to users.
- **Heart Rate Tracking:** Store and retrieve patient heart rate data.
- **Filtering & Pagination:** Filter heart rate data by patient and paginate results.
- **Validation & Error Handling:** Ensures proper data constraints and informative error messages.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django & Django REST Framework
- PostgreSQL

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Ashwitha2001/patient-heart-rate-tracker.git
   cd patient-heart-rate-tracker
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```sh
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- **Register:** `POST /register/`
- **Login:** `POST /login/`

### Patients
- **List Patients:** `GET /patients/{user_id}/`
- **Create Patient:** `POST /patients/create/`

### Heart Rate Data
- **List Heart Rate Records:** `GET /patients/{patient_id}/heartrate/`
- **Create Heart Rate Record:** `POST /patients/{patient_id}/heartrate/create/`

### Filtering & Pagination
- Use query parameters:
  - `?page=1` for pagination
  - `?heart_rate__gte=80` to filter heart rate greater than or equal to 80

## Assumptions & Decisions
- Users must be authenticated to access patient data.
- Heart rate values are stored as integer fields.
- Patients are linked to users who manage their records.
- Default pagination is set to 10 records per page.

## Testing
- Use Postman or cURL to test API endpoints.

## License
This project is open-source and free to use.
