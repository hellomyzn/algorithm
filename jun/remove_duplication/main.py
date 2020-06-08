"""
[1,3,3,5,5,7,7,7,10,12,12,15] => [,13,5,7,10,12,15]
"""

# l = [1,3,3,5,5,7,7,7,10,12,12,15]
# print(list(set(l)))
# print(list(dict.fromkeys(l)))
# print([ n for i , n in enumerate(l) if n not in l[:i]])

from typing import List


def delete_duplicate_v1(numbers: List[int]) -> None:
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp


def delete_duplicate_v2(numbers: List[int]) -> None:
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) - 1
    while i < len_num:
        if numbers[i] != numbers[i+1]:
            tmp.append(numbers[i+1])
        i += 1
    numbers[:] = tmp


if __name__ == "__main__":
    l = [1,3,3,5,5,7,7,7,10,12,12,15]
    delete_duplicate_v2(l)
    print(l)
