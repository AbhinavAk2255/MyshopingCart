# update_product_description.py
from django.core.management.base import BaseCommand
from products.models import newproducts,product

class Command(BaseCommand):
    help = 'Update product description'

    def handle(self, *args, **options):
        # Your update logic goes here
        message = product.objects.all()

        for dilog in message:
            # Update description for each product as needed
            dilog.description = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo exercitationem laborum suscipit temporibus dignissimos tenetur consequuntur minus omnis illum, blanditiis perferendis repellendus, commodi ducimus itaque libero veritatis voluptatem architecto pariatur!"
            dilog.save()

        self.stdout.write(self.style.SUCCESS('Product descriptions updated successfully'))
