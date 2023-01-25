from app.database import con, execute_query_response, execute_query_no_response
from fastapi import APIRouter
from app.products.model import ProductBase, ProductUpdate
router = APIRouter()

connection_ctx = con
# Crud operations
@router.get("/")
def get_all_products():
    query = "SELECT * FROM fastapi_db.products"
    res = execute_query_response(connection_ctx, query)
    return res

@router.get("/{id}")
async def get_product(id: int):
    query = f"SELECT * FROM fastapi_db.products WHERE id = {id}"
    res = execute_query_response(connection_ctx, query)
    return res

@router.post("/")
async def create_product(product: ProductBase):
    if product.serie > 0:
        query = f"INSERT INTO fastapi_db.products (name, price, category_id, serie) VALUES ('{product.name}', {product.price}, {product.category_id}, {product.serie})"
        try:
            execute_query_no_response(connection_ctx, query)
            return {"message": "product created"}
        except Exception as e:
            return {"message": e}
    else:
        return {"message": "serie must be greater than 0"}


@router.put("/{id}")
async def update_product(product: ProductUpdate, id: int):
    query = f"UPDATE fastapi_db.products SET name = '{product.name}', price = {product.price}, category_id = {product.category_id} WHERE id = {id}"
    try:
        execute_query_no_response(connection_ctx, query)
        return {"message": "product updated"}
    except Exception as e:
        return {"message": e}
    
@router.delete("/{id}")
async def delete_product(id: int):
    query = f"DELETE FROM fastapi_db.products WHERE id = {id}"
    try:
        execute_query_no_response(connection_ctx, query)
        return {"message": "product deleted"}
    except Exception as e:
        return {"message": e}
        