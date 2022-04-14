import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Product_ShowTime.settings")

import django
django.setup()

from django.core.management import call_command

from ShowTime_app.models import Movies

print(Movies.objects.all())