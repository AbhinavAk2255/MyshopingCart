import json
from django.core.management.base import BaseCommand
from products.models import newproducts,product

class Command(BaseCommand):
    help = 'import external JSON file into Django database'

    def handle(self, *args, **kwargs):
        with open('/home/abhinav/Desktop/hello_django/mycart/all_product.js','r',encoding='utf8') as file:
            data = json.load(file)

            for item in data:
                product.objects.create(
                    title=item['name'],
                    genter=item['category'],
                    image=item['image'],
                    price=item['new_price']
                    
                )
        self.stdout.write(self.style.SUCCESS('Done'))

