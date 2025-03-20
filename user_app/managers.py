from django.contrib.auth.models import BaseUserManager

# Manager: UserManager
# -------------------------------------------------------------------------------------------------------------
class UserManager(BaseUserManager):
    def create_user(self, address, password=None, **extra_fields):
        """
        Create and save a User with the given telegram_id, first_name, and last_name.
        """
        if not address:
            raise ValueError("User must have an address")

        extra_fields.setdefault("is_active", True)

        user = self.model(
            address=address,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, address, password, **extra_fields):
        """
        Create and save a Superuser with given telegram_id, first_name, last_name, and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True")
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True")

        return self.create_user(address, password, **extra_fields)