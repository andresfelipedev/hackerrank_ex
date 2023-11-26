"""

Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

"""

n = 5
arr = [34,34,36,6,39,25,76,34,34]

doing_each = set(arr)

doing_arr_again = list(doing_each)

doing_arr_again.sort(reverse=True)

second = doing_arr_again[1]



print(doing_arr_again)
print(second)


