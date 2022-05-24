def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))


"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:
    """
        find_target -> YOUR_CODE
    """

    def find_target(self, list, target):
        for num in range(len(list)):
            if list[num] == target:
                print(f'objact {target} on {num}')


l = get_list()




Solution.find_target("", l, 50_000_000)


