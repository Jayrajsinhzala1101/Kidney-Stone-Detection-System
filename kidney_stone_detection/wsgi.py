"""
WSGI config for kidney_stone_disease_detection project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kidney_stone_detection.settings')

application = get_wsgi_application() 