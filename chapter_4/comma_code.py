def comma_code(arr: list) -> str:
    """
    Return a string of comma separated values, with and inserted before the last value.

    Args:
        arr (list): The list of values to be comma separated.
    
    Returns:
        str: comma separated values
    """
    return ", ".join(arr[:-1]) + " and " + arr[-1] if len(arr) > 1 else arr


spam = ["apples", "bananas", "tofu", "cats"]
print(comma_code(spam))
print(comma_code([]))
