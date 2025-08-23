from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/items")  # This receives the HTTP GET request
def get_items(category: str = Query(None)):
    print("Made it")
    return {"message": "Got items!", "category": category}
