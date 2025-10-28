from fastapi import APIRouter, HTTPException, status
from ..schema.binary_convert import BinRes
from ..crud.binary_convert import converter

router = APIRouter(tags=["Binary Base10 Coverter"])

@router.get("/binary", response_model=BinRes, status_code=status.HTTP_200_OK)
async def binary_base10_convertor():
    """ answers Question 8"""
    try:
        return await converter()
    except HTTPException as Httpexc:
        raise Httpexc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )