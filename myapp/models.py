from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    category = models.ForeignKey('EquipmentCategory', on_delete=models.CASCADE)


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=100)


class ResponsiblePerson(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('EquipmentCategory', on_delete=models.CASCADE)


class EquipmentLog(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    responsible_person = models.ForeignKey('ResponsiblePerson', on_delete=models.CASCADE)
    operation_type = models.CharField(max_length=100)
    operation_date = models.DateField()
    description = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=(('admin', 'Admin'), ('user', 'User')))

    def __str__(self):
        return self.user.get_full_name()


class UserOwnedEquipment(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)