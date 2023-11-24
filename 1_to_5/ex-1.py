#x = int(input(f'Pon la x: '))
#y = int(input(f'Pon la y: '))
#z = int(input(f'Pon la z: '))
#n = int(input(f'Pon la n: '))
    

list_1 = [1,2,3]





new_m = [list_1[:i] + list_1[i + 1:] + [list_1[i]] for i in range(len(list_1)) for i in range(len(list_1))]

print(new_m)
