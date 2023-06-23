from django.utils import timezone
from faker import Faker
from random import randint
from .myapp/models import Equipment, EquipmentCategory

fake = Faker()

categories = EquipmentCategory.objects.all()

for i in range(500):
    name = fake.company()
    model = fake.word()
    serial_number = fake.ean13()
    cost = randint(1, 10000)
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