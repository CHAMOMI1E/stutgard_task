from celery import shared_task
from .models import Product
import requests

@shared_task
def parse_product_task(nm_id):
    url = f"https://www.wildberries.ru/catalog/{nm_id}/detail.aspx"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        product, created = Product.objects.get_or_create(nm_id=nm_id)
        product.imt_name = data.get('name')
        product.description = data.get('description')
        product.save()