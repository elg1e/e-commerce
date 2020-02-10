from django.contrib.auth.models import User

class EmailAuth:
    """Authenticate user by an exact match on email and password"""

    def authenticate(self, username=None, password=None):
        """Get instance of user based off email and verify the password"""

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Used by the Django traffic system"""

        try:
            user = User.object.get(pk=user_id)

            if user.is_active:
                return user
                return None
        expect User.DoesNotExist:
            return None
