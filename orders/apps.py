from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        """
        Automatically creates a default superuser (admin/Admin1234)
        after database migrations are ready.
        """
        import threading
        from django.db import connection
        from django.contrib.auth.models import User
        from django.db.utils import OperationalError, ProgrammingError

        def create_admin():
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1;")
                if not User.objects.filter(username='admin').exists():
                    User.objects.create_superuser(
                        username='admin',
                        email='admin@ayannayoghurt.com',
                        password='Admin1234'
                    )
                    print("✅ Default superuser created: admin / Admin1234")
            except (OperationalError, ProgrammingError):
                print("⚠️ Database not ready yet — skipping admin creation.")

        # Run this check after startup in a separate thread (avoids migration issues)
        threading.Timer(10.0, create_admin).start()
