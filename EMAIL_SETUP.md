# Email Setup Guide for KidneyStoneAI

## ✅ **Email Configuration Complete!**

Your Gmail app password has been successfully configured:
- **App Password:** `oaulnlcbnqymollo`
- **Email:** `cropguard.app@gmail.com`

## 🔧 **Current Configuration**

The email functionality is now ready to use. When new users register, they will automatically receive a welcome email.

### **Files Updated:**
- ✅ `crop_disease_detection/settings.py` - Email backend configuration
- ✅ `detection/email_service.py` - Email service functions
- ✅ `detection/views.py` - Registration integration

## 📧 **Email Features**

### **Welcome Email**
- **Trigger:** New user registration
- **Content:** Personalized welcome message with user's name
- **Template:** Professional greeting with KidneyStoneAI branding

### **Email Template**
```
Hi [Name], 👋

Welcome to KidneyStoneAI! 🩺  
We're excited to have you on board.

With KidneyStoneAI, you can analyze scan images easily, track your detections, and experiment with AI-based kidney stone detection.

Start by uploading a scan image, and we'll help you get a quick AI-based assessment in seconds!

If you have any questions or need support, we're just a click away.

Warm regards,  
Team KidneyStoneAI
```

## 🚀 **Testing the Email Functionality**

1. **Start the Django server:**
   ```bash
   python manage.py runserver
   ```

2. **Register a new user** through the frontend
3. **Check the console** for email sending confirmation
4. **Check the user's email** for the welcome message

## 🔒 **Security Notes**

- The app password is configured in Django settings
- Emails are sent using Gmail SMTP with TLS encryption
- Email sending runs in a separate thread to avoid blocking the registration process
- Error handling ensures registration continues even if email fails

## 🛠️ **Troubleshooting**

If emails are not being sent:
1. Verify the app password is correct
2. Check that Gmail 2FA is enabled
3. Ensure the email address is correct
4. Check Django console for error messages

The email functionality is now fully configured and ready to use! 🎉 