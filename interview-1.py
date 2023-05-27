"""

<---CHALLENGE--->
* Given an array of integers, return the indices
of the two numbers that add up to a given target

* [1, 3, 7, 9, 2], target = 11

<---SOLUTION APPROACH--->
* Verifying the constraints *
- Are all the numbers positive or can there be negatives?
- Are there duplicate numbers or are they unique?
- Will there always be a solution available?
- What do we return if there are no solutions?
- Can there be multiple pairs that add up to the target value?

* Write some test cases *
- [1, 3, 7, 9, 2], target = 11 indexes 3, 4 will be returned as the numbers in those positions
 add up to the target value
- [1, 3, 7, 9, 2], target = 25 in this case should return null since there are no values that add up to 25
- [], target = 1 in this case should return null since the arr is empty
- [5], target = 5 in this case should return null because we need two values
- [1, 6] target = 7, should return [0, 1] as answer

* Figure out solution without code *
- Try every single possible combination that exists in the array
- If none adds up, then the solution is null
- Use the two-pointer technique

""" 



# IMPLEMENTATION

arr = [1, 3, 7, 9, 2]
target = 11

def findTwoSum(arr, target):
    length = len(arr)
    for p1 in range(length):
        num_to_find = target - arr[p1]
        for p2 in range(p1 + 1, length):
            if num_to_find == arr[p2]:
                return [p1, p2]
    return None

result = findTwoSum(arr, target)
print(result)



