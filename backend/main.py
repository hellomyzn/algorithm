import copy 

from sort.bubble_sort import bubble_sort
from sort.cocktail_sort import cocktail_sort
from sort.comb_sort import comb_sort
from sort.selection_sort import selection_sort

if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for _ in range(100)]

    bubble = bubble_sort(copy.copy(nums))
    comb = comb_sort(copy.copy(nums))
    cocktail = cocktail_sort(copy.copy(nums))
    selection =  selection_sort(copy.copy(nums))

    print(bubble == comb)
    print(bubble == cocktail)
    print(bubble == selection)