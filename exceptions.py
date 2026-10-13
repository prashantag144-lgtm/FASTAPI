from fastapi.responses import JSONResponse
from fastapi import Request

class PincodeNotFoundError(Exception):
    def __init__(self, pincode:str):
        self.pincode=pincode


class InvalidPinCodeError(Exception):
    def __init__(self,pincode:str,reason:str="INVALID FORMAT"):
        self.pincode=pincode
        self.reason=reason


# CUSTOM HANDLERS

async def pincode_not_found_handler(request:Request,exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"Pincode not found",
            "message":f"No location for pincode {exc.pincode}",
            "pincode":exc.pincode
        }
    )


async def invalid_pincode_handler(request:Request,exc:InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error":"Invalid_pincode",
            "message":f"Pincode {exc.pincode} is invalid:{exc.reason}",
            "pincode":exc.pincode
        }
    )

 