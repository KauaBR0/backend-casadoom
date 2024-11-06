from models.product import Product
from typing import List

class ProductService:
    def __init__(self):
        self.products: List[Product] = []
        self.counter = 1

    def create(self, product: Product) -> Product:
        product.id = self.counter
        self.counter += 1
        self.products.append(product)
        return product

    def get_all(self) -> List[Product]:
        return self.products

    def get_by_id(self, id: int) -> Product:
        return next((product for product in self.products if product.id == id), None)

    def update(self, id: int, product: Product) -> Product:
        for i, p in enumerate(self.products):
            if p.id == id:
                product.id = id
                self.products[i] = product
                return product
        return None

    def delete(self, id: int) -> bool:
        product = self.get_by_id(id)
        if product:
            self.products.remove(product)
            return True
        return False
