from ..utils.recursive_search import recursive_binary_search
from fastapi import HTTPException

async def recur_search(item):
    try:
        # Sort the list for binary search requirement
        data_list = sorted(item.data_list)
    
    
        # Execute the search
        index_in_sorted = recursive_binary_search(data_list, item.target, 0, len(data_list) - 1)
    
        if index_in_sorted != -1:
            # If found, find the *first* occurrence of the target in the *original* unsorted list
            # to provide a meaningful index back to the user's input list.
            try:
                original_index = item.data_list.index(item.target)
            except ValueError:
                # Should not happen if index_in_sorted is valid, but safe guard.
                original_index = -1 
            
            return {
                "target": item.target,
                "found": True,
                "index": original_index
            }
        else:
            return {
            "target": item.target,
            "found": False,
            "index": -1
        }
    except HTTPException as httpexc:
        raise httpexc