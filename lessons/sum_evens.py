"""Practice summing over lists."""

def sum_evens_of_list(input_list: list[int]) -> int:
    """Loop over a list and sum all even elements."""
    sum_total: int = 0
    i: int = 0
    while i<len(input_list):
        if input_list[i] % 2 == 0:
            sum_total = sum_total + input_list[i]
    return sum_total