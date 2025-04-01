from django.core.management import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    """
    Creates products
    """
    
    def handle(self, *args, **options):
        self.stdout.write("Create products")
        
        products_names = {
            "Laptop",
            "Descktop",
            "Smartphone",
        }
        
        for products_name in products_names:
            prouduct, created = Product.objects.get_or_create(name=products_name)
            self.stdout.write("Created product {product.name}")
            
            
        self.stdout.write(self.style.SUCCESS("Product created"))
        