import os

import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab16.settings')
django.setup()

from faker import Faker
from random import randint
from myapp.models import Equipment, EquipmentCategory

fake = Faker()

categories = EquipmentCategory.objects.all()

if not categories:
    # Handle the case where there are no categories in the database
    # For example, you could create some default categories here
else:
    for i in range(500):
        name = fake.company()
        model = fake.word()
        serial_number = fake.ean13()
        cost = = randint(1, 10000)
        purchase_date = fake.date_this_year()
        category = categories[randint(0, len(categories) - 1)]

        Equipment.objects.create(
            name=name,
            model=model,
            serial_number=serial_number,
            cost=cost,
            purchase_date=purchase_date,
            category=category,
        )
