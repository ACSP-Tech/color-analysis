from fastapi import APIRouter, HTTPException, status, Depends
from ..schema.color_analysis import ColorRes
from ..crud.color_analysis import analyse_store_color
from ..database_setup import get_db

router = APIRouter(tags=["Color Analysis"])

@router.get("/analysis", response_model=ColorRes, status_code = status.HTTP_200_OK)
async def analyse_color(session = Depends(get_db)):
    """
    Answers questions 1, 2, 3, 4 (BONUS), 5 (BONUS), 6
    """
    try:
        return await analyse_store_color(session)
    except HTTPException as Httpexc:
        raise Httpexc
    except Exception as e:
        raise(HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e))
        )