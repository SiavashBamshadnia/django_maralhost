import random

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand
from django.utils import lorem_ipsum

from ecommerce.models import Car


class Command(BaseCommand):
    help = "generates user groups and 1000 users"

    def handle(self, *args, **options):
        # Generate groups
        support_group = Group(name='support')
        support_group.save()
        support_group.permissions.add(Permission.objects.filter(codename='search_car').get())
        support_group.save()

        sale_group = Group(name='sale')
        sale_group.save()

        sale_group.permissions.set(Permission.objects.filter(codename__in=['add_car',
                                                                           'change_car',
                                                                           'delete_car',
                                                                           'view_car']).all())
        sale_group.save()

        # Generate users
        user_model = get_user_model()

        user_model.objects.create_superuser(username='admin', email='sbamtr@gmail.com', password='admin')

        support_user = user_model.objects.create_user(username='support', email='support@example.com',
                                                      password='support')
        support_user.groups.set([support_group])
        support_user.save()

        support_user = user_model.objects.create_user(username='sale', email='sale@example.com', password='sale')
        support_user.groups.set([sale_group])
        support_user.save()

        # Generate cars
        colors = ["قرمز", "آبی", "زرد", "سبز", "صورتی", "بنفش", "نارنجی", "خاکستری", "قهوه‌ای", "سفید"]

        cars = []
        for i in range(1_000):
            car = Car()
            car.name = f'Car {i + 1}'
            car.price = random.randint(100_000_000, 1_000_000_000)
            car.cylinder_count = random.randint(2, 10)
            car.passenger_count = random.choice([2, 4])
            car.color = random.choice(colors)
            car.cylinder_volume = random.randint(2, 10)
            car.owner_name = lorem_ipsum.words(2, common=False)

            cars.append(car)

        Car.objects.bulk_create(cars)
