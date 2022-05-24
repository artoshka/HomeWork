def get_list() -> list:
    return list(range(0, 1_000_000, 2))


"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:
    """
        find_target -> YOUR_CODE
    """

    def find_target(self, target: int, mass: list) -> int:
        low = 0
        high = len(mass) - 1

        while low <= high:
            midle = (low + high) // 2
            if mass[midle] < target:
                low = midle - 1
            elif mass[midle] > target:
                high = midle + 1
            else:
                return midle
        return -1




value = Solution().find_target(400000, get_list())

print(value)



