from fastapi import FastAPI
from fastapi import Request
import uvicorn

app=FastAPI(
    title="Swiggy order service",
    description=(
        "This is internal api for managing orders"
        "Hnadle creation , tracking of deleivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    #FASTAPI coverts this dict into JSON 
    return {"message":"welcome to swiggy order service",
            "status":"healthy"}

@app.get("/about")
def about():
    """Return API metadata"""
    return {
        "service":"order-service",
        "team":"backend platform ",
        "region":"ap-south-1",
        "version":"1.2.2"
    }

@app.get("/orders")
def list_orders():
    """List recent orders"""
    return {
        "orders":[
            {"id":1,"item":"Butter CHicken","status":"delivered"},
            {"id":2,"item":"Masala Dosa","status":"preparing"},
            {"id":3,"item":"Paneer Tikka","status":"delivered"},
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get order status"""
    return {
        "total_today":2_340_23,
        "today_city":"Bengaluru"
    }

@app.get("/debug/request-info")
async def request_info(request:Request):
    return {
        "method":request.method,
        "url":str(request.url),
        "headers":dict(request.headers),
        "path_params":request.path_params,
        "query_params":dict(request.query_params),

    }


    
@app.get(
    "/orders/active",
    summary="Get Acitve Orders",
    description=(
        "returns all orders that are currenty being prepared "
        "or are out for deleivery"
    ),
    tags=["orders"],
    response_description="List of active order objects",
    deprecated=False

)

def get_activate_orders():
    """This docstring alos appears in docs"""
    return {
        "active_order":[
            {"id":1,"item":"Masala Dosa","status":"out_for_delivery"}
        ]
    }


@app.get("/restraunts",tags=["Restaurants"])
def list_restro():
    """another docstring for another endpoint"""
    return {
        "restaurants":[
            {"test":"test"}
        ]
    }

@app.get("/restraunts/delhi",tag=["Restraunts"])
def list_restro_delhi():
    """another docstring for another endpoint"""
    return {
        "restraunts":[{
            "test":"test"
        }]
    }