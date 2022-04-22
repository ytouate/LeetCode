class Solution:
    def average(self, salary: List[int]) -> float:
        a = min(salary)
        b = max(salary)
        sum = 0
        for i in salary:
            if i != a and i != b:
                sum += i
        return sum / (len(salary) - 2)
        