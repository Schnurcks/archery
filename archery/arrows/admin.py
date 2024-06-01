from django.contrib import admin
from django.apps import apps

# Register your models here.
arrows_models = apps.get_app_config('arrows').get_models()

for model in arrows_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

