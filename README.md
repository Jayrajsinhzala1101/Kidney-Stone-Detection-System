# KidneyStoneAI - AI Kidney Stone Detection System

A comprehensive web application for detecting kidney stones using AI/ML technology. Built with a Django REST API backend and React frontend.

## Features

- **AI-Powered Kidney Stone Detection**: Upload scan images to detect whether a kidney stone is likely present
- **User Authentication**: Secure email-based authentication system
- **Detection History**: Track all your previous detections
- **Real-time Analysis**: Get instant results with confidence scores
- **Treatment Suggestions**: Receive treatment recommendations for detected diseases

## Technology Stack

- **Backend**: Django 4.2.7, Django REST Framework
- **Frontend**: React 18, Tailwind CSS, Framer Motion
- **Database**: PostgreSQL
- **AI/ML**: CNN-based model for kidney stone classification

## Project Structure

```
KidneyStoneAI/
├── frontend/                 # React frontend application
├── detection/               # Django app (main application & API)
├── crop_disease_detection/  # Django project settings (module name kept for legacy)
├── media/                   # Uploaded images
├── templates/               # Django templates
└── manage.py               # Django management script
```

## Quick Start

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   # Backend
   pip install -r requirements.txt
   
   # Frontend
   cd frontend
   npm install
   ```

3. **Setup database**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the application**:
   ```bash
   # Backend (Terminal 1)
   python manage.py runserver
   
   # Frontend (Terminal 2)
   cd frontend
   npm start
   ```

5. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

## API Endpoints

- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `POST /api/logout/` - User logout
- `POST /api/detect/` - Disease detection
- `GET /api/history/` - Detection history
- `GET /api/user/` - User information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 