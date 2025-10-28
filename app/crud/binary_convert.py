import random
from fastapi import HTTPException, status

async def converter():
    try:
        # Generate 4 random digits (0 or 1)
        binary_list = [str(random.randint(0, 1)) for _ in range(4)]
        binary_input = "".join(binary_list)
    
        # Convert binary string to base 10 integer
        base_10_output = int(binary_input, 2)
    
        return {
            "binary_input": binary_input,
            "base_10_output": base_10_output
        }
    except HTTPException as Httpexc:
        raise Httpexc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )
    
    