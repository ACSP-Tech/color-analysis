from fastapi import APIRouter, HTTPException, status
from ..schema.recursive_search import ReSear, SearchItem
from ..crud.recursive_search import recur_search

router = APIRouter(tags=["Recursive Search"])



@router.post("/algorithm/recursive-search", response_model=ReSear, status_code=status.HTTP_201_CREATED)
async def recursive_search_endpoint(item: SearchItem):
    """
    Q7 (BONUS): Implements a recursive binary searching algorithm.
    """
    try:
        return await recur_search(item)
    except HTTPException as Httpexc:
        raise Httpexc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )