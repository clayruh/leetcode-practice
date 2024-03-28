class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        # for employee `i` in array of `hours`, print out a statement of hours they've worked
        numOfEmployees = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                numOfEmployees += 1
        # if hours[i] is greater than or equal to `target`, the employee has me the `target`, and another variable counting `numOfEmployees` += 1
        # return numOfEmployees
        return numOfEmployees