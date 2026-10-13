from fastapi import FastAPI
from exceptions import (
    pincode_not_found_handler,
    PincodeNotFoundError,
    InvalidPinCodeError,
    invalid_pincode_handler,

)
from pincode_db import pincode_db
from p2_model import (
    pincodeRequest,
    BulkRequest,
    BulkResponse,
    LocationResponse

)


app=FastAPI(
    title="Pincode lookup API",
    description="Auto fill city and state from Indian pincode during checkout"
)

# register custim exception handler

app.add_exception_handler(PincodeNotFoundError,pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError,pincode_not_found_handler)

@app.get("/")
def root():
    return {"message":"Pincode lookup api"}

### CUSTOM EXCEPTIONS classes and exception handlers

@app.get("/pincode/{code}",response_model=LocationResponse)
def lookup_pincode(code:str):
    if len(code)!=6 or not  code.isdigit():
        raise InvalidPinCodeError(code,"Must be exactly 6 digit")

    if code not in pincode_db:
        raise PincodeNotFoundError(code)
    return pincode_db[code]


@app.post("/pincode/bulk",response_model=BulkRequest)
def bulk_lookup(request:BulkRequest):
    results=[]
    missing=[]

    for code in request.pincode:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        results=results,
        missing=missing

    )


