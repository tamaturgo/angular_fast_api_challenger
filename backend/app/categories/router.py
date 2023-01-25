from app.database import con, execute_query_response, execute_query_no_response
from fastapi import APIRouter
from app.categories.model import CategoryBase, CategoryUpdate
router = APIRouter()

connection_ctx = con
# Crud operations
@router.get("/")
def get_all_categories():
    query = "SELECT * FROM fastapi_db.categories"
    res = execute_query_response(connection_ctx, query)
    return res

@router.get("/{id}")
async def get_category(id: int):
    query = f"SELECT * FROM fastapi_db.categories WHERE id = {id}"
    res = execute_query_response(connection_ctx, query)
    return res

@router.post("/")
async def create_category(category: CategoryBase):
    query = f"INSERT INTO fastapi_db.categories (name) VALUES ('{category.name}')"
    try:
        execute_query_no_response(connection_ctx, query)
        return {"message": "category created"}
    except Exception as e:
        return {"message": e}

@router.put("/{id}")
async def update_category(category: CategoryUpdate, id: int):
    query = f"UPDATE fastapi_db.categories SET name = '{category.name}' WHERE id = {id}"
    try:
        execute_query_no_response(connection_ctx, query)
        return {"message": "category updated"}
    except Exception as e:
        return {"message": e}

@router.delete("/{id}")
async def delete_category(id: int):
    query = f"DELETE FROM fastapi_db.categories WHERE id = {id}"
    try:
        execute_query_no_response(connection_ctx, query)
        return {"message": "category deleted"}
    except Exception as e:
        return {"message": e}

