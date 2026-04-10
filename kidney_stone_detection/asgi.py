"""
ASGI config for kidney_stone_disease_detection project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kidney_stone_detection.settings')

application = get_asgi_application() 