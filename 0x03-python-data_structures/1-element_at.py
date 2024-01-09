def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Check if idx is out of range
    if idx >= len(my_list):
        return None

    # Return the element at the specified index
    return my_list[idx]

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

