"""

Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

"""

n = 5
arr = [34,34,36,6,39,25,76,34,34]

arr.sort(reverse=True)

unique_elements = sorted(set(arr), reverse=True)

if len(unique_elements) > 1:
    second = unique_elements[1]
    print(second)
else:
    print("No hay segundo elemento unico")

print(second)


