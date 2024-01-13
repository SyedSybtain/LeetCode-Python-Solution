class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_salary = min(salary)
        max_salary = max(salary)

        salary.remove(min_salary)
        salary.remove(max_salary)
        output = float(sum(salary))/len(salary)
        return output
