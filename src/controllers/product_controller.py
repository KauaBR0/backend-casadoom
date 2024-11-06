from fastapi import HTTPException
from models.product import Product
from services.product_service import ProductService
from typing import List

class ProductController:
    def __init__(self):
        self.service = ProductService()

    def create_product(self, product: Product) -> Product:
        return self.service.create(product)

    def get_all_products(self) -> List[Product]:
        return self.service.get_all()

    def get_product(self, id: int) -> Product:
        product = self.service.get_by_id(id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def update_product(self, id: int, product: Product) -> Product:
        updated_product = self.service.update(id, product)
        if not updated_product:
            raise HTTPException(status_code=404, detail="Product not found")
        return updated_product

    def delete_product(self, id: int) -> bool:
        if not self.service.delete(id):
            raise HTTPException(status_code=404, detail="Product not found")
        return True
