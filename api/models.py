from django.db import models

import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imt_id = models.IntegerField()
    nm_id = models.IntegerField()
    imt_name = models.CharField(max_length=255)
    slug = models.SlugField()
    subj_name = models.CharField(max_length=255)
    subj_root_name = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=255)
    description = models.TextField()



class ParseWB:
    def __init__(self, article: int):
        self.article = article
        self.volume = self.article // 100000
        self.part = self.article//1000

    def _get_basket(self):
        _short_id = self.volume
        if 0 <= _short_id <= 143:
            basket = '01'
        elif 144 <= _short_id <= 287:
            basket = '02'
        elif 288 <= _short_id <= 431:
            basket = '03'
        elif 432 <= _short_id <= 719:
            basket = '04'
        elif 720 <= _short_id <= 1007:
            basket = '05'
        elif 1008 <= _short_id <= 1061:
            basket = '06'
        elif 1062 <= _short_id <= 1115:
            basket = '07'
        elif 1116 <= _short_id <= 1169:
            basket = '08'
        elif 1170 <= _short_id <= 1313:
            basket = '09'
        elif 1314 <= _short_id <= 1601:
            basket = '10'
        elif 1602 <= _short_id <= 1655:
            basket = '11'
        elif 1656 <= _short_id <= 1919:
            basket = '12'
        elif 1920 <= _short_id <= 2045:
            basket = '13'
        elif 2046 <= _short_id <= 2189:
            basket = '14'
        elif 2190 <= _short_id <= 2405:
            basket = '15'
        else:
            basket = '16'
        return basket
    
    def parse(self):
        import requests
        try:
            r = requests.get(url=f"https://basket-{self._get_basket()}.wbbasket.ru/vol{self.volume}/part{self.part}/{self.article}/info/ru/card.json")
            data = r.json()

            product, created = Product.objects.update_or_create(
                nm_id=self.article,
                defaults={
                    'imt_id': data.get('imt_id', 0),
                    'imt_name': data.get('imt_name', ''),
                    'slug': data.get('slug', ''),
                    'subj_name': data.get('subj_name', ''),
                    'subj_root_name': data.get('subj_root_name', ''),
                    'vendor_code': data.get('vendor_code', ''),
                    'description': data.get('description', '')
                }
            )
            print(f"Product {'created' if created else 'updated'}: {product}")
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        except ValueError:
            print("Failed to parse JSON")
