# 🐰 Rabbits in Forest - LeetCode Problem 781

### 🔧 Problem Statement
There is a forest with an unknown number of rabbits.  
We asked `n` rabbits:  
> *"How many other rabbits have the same color as you?"*

Each rabbit gives an integer answer. You're given an array `answers` where:
- `answers[i]` is the response of the `i-th` rabbit.

Return the **minimum number of rabbits** that could be in the forest.

---

### 🧠 Intuition
- If a rabbit says `"x"`, then there are `x + 1` rabbits (including itself) of the same color.
- Multiple rabbits saying the same number can be in the **same group**, but at most `x + 1` rabbits per group.
- Use **ceil division** to handle overflow cases and compute minimum groups needed.

---

### 📦 Example

#### Input:
```
answers = [1, 1, 1, 2, 3, 3, 4]
```
# Output:
 ```
9
```
# 💻 Python Code
```
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
            group_size = answer + 1
            num_groups = math.ceil(count / float(group_size))
            total_rabbits += num_groups * group_size
        
        return init(total_rabbits)
```
# 🚀 How to Use
```
sol = Solution()
print(sol.numRabbits([1, 1, 1, 2, 3, 3, 4]))  # Output: 9
```
# 📌 Constraints
- 1 <= answers.length <= 1000

- 0 <= answers[i] < 1000

# 📺 From: Coding Moves
Follow <a href="https://wwww.youtube.come@Coding_Moves">Coding Moves</a> on YouTube for more awesome coding content, explanations, and project tutorials!


