from fastapi import APIRouter
from models.product import Product
from controllers.product_controller import ProductController
from typing import List

router = APIRouter(prefix="/products", tags=["products"])
controller = ProductController()

@router.post("/", response_model=Product)
async def create_product(product: Product):
    return controller.create_product(product)

@router.get("/", response_model=List[Product])
async def get_all_products():
    return controller.get_all_products()

@router.get("/{id}", response_model=Product)
async def get_product(id: int):
    return controller.get_product(id)

@router.put("/{id}", response_model=Product)
async def update_product(id: int, product: Product):
    return controller.update_product(id, product)

@router.delete("/{id}")
async def delete_product(id: int):
    controller.delete_product(id)
    return {"message": "Product deleted successfully"}
