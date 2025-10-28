def recursive_binary_search(arr, target, low, high):
        """Standard recursive binary search implementation."""
        if low > high:
            return -1  # Not found
        
        mid = (low + high) // 2
        
        if arr[mid] == target:
            # We found the element, but since the list was sorted, we need to find its
            # original index in the provided (unsorted) list. For simplicity in recursive
            # context, we return the index in the sorted array, and the endpoint handles the message.
            return mid
        elif arr[mid] > target:
            return recursive_binary_search(arr, target, low, mid - 1)
        else:
            return recursive_binary_search(arr, target, mid + 1, high)