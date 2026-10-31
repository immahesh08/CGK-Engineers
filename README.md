# CGK Engineers & Consultants — Full Stack Website

Premium corporate HVAC, VRF, chiller, AC and lighting website.

## Stack
- Frontend: React + Vite + Axios + React Router + Lucide React
- Backend: Django + Django REST Framework + Simple JWT
- Database: PostgreSQL

## Backend
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Frontend
```bash
cd frontend
npm install
copy .env.example .env
npm run dev
```

Frontend: http://localhost:5173
Backend: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin/

Configure PostgreSQL and environment variables before production use.
