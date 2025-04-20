from collections import Counter
import math

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        counter = Counter(answers)
        total_rabbits = 0
        
        for answer, count in counter.items():
            group_size = answer + 1  # each group can have up to (answer + 1) rabbits
            num_groups = math.ceil(count / group_size)  # how many such groups we need
            total_rabbits += num_groups * group_size  # total rabbits in those groups
        
        return init(total_rabbits)

# Example usage:
obj = Solution()
print(obj.numRabbits([1, 1, 1, 2, 3, 3, 4]))  # Output will be the minimum number of rabbits
