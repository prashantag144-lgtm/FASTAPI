from fastapi import FastAPI, Query, HTTPException
from models import MenuItem,Menuresponse
from data import menu_items

app=FastAPI(
    title="Bengaluru Cafe",
    description="Read only menu API for Kiosk display and mobile app"
)

@app.get("/")
def root():
    return {
        "message":"welcome to Bengaluru cafe API"
    }
# /menu -->Path
# /menu?category=chai&available=true  -->Query parameter
# /menu?category=chai


@app.get("/menu",response_model=Menuresponse)
def get_menu(category:str |None=Query(None, description="filter by chai, snacks, combos")):
    if category:
        filtered=[item for item in menu_items if item["category"]==category.lower()]
        if not filtered:
            raise HTTPException(status_code=404,detail=f"No item found in category: {category}")
        return Menuresponse(count=len(filtered),items=filtered)

    return Menuresponse(count=len(menu_items),items=menu_items)

@app.get("/menu/{id}",response_model=MenuItem)
def get_item(id:int):
    for item in menu_items:
        if item["id"]==id:
            return item

    raise HTTPException(status_code=404, detail=f"Menu item with ID: {id}")