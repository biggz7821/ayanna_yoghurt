from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        """
        Automatically creates a default superuser (admin/Admin1234)
        if one does not already exist. This helps when deploying
        to environments like Render that have no shell access.
        """
        from django.contrib.auth.models import User
        from django.db.utils import OperationalError, ProgrammingError

        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@ayannayoghurt.com',
                    password='Admin1234'
                )
                print("✅ Default superuser created: admin / Admin1234")
        except (OperationalError, ProgrammingError):
            # Database might not be ready yet on first startup
            pass
