from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

def ready(self):
            # Import your script or define your startup logic here
            print("Django server is starting up and MyAppConfig is ready!")
            # Example: Run a function from another file
            # from . import startup_script
            # startup_script.run_on_startup()
            # Or directly execute code:
            # print("Performing startup tasks...")
            # from cron import printgames
            # printgames()