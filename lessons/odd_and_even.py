"""def odd_and_even(input: list[int])-> list[int]:
    Returns a new list.
    output: list[int] = []
    for i in range(len(input)):
        if (i % 2 == 0) and (input[i] % 2 != 0):
            output.append(input[i])
    return output


def value_exists(dictionary: dict[str, int], val: int) -> bool: 
    for i in dictionary:
        if dictionary[i] == val:
            return True
    return False


print(odd_and_even([7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]))
test_dict : dict [str ,int] = {"a": 2 , "b": 4 , "c": 7 , "d": 1}
test_val : int = 4
print(value_exists ( test_dict , test_val ))

print(value_exists ( test_dict , 5))

dictionary: dict[str, str] = {"hello": "hola", "adios": "bye"}

for i in range(len(dictionary)):
    dictionary[i] = "cool

for i in dictionary:
    dictionary[i] = "cool"
    print(dictionary)"""

def short_words(input: list[str]) -> list[str]:
    """hello."""
    output: list[str] = []
    for i in input:
        if len((i)) < 5:
            output.append(i)
        else: 
            print(i + " was too long!")
    return output

my_list : list [str ] = ["sun", "cloud", "sky"]
print(short_words ( my_list ))