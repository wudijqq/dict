



def mean(sorted_list):
    if not sorted_list:
        return (([],[]))
    big = sorted_list[-1]
    small = sorted_list[-2]
    big_list, small_list = mean(sorted_list[:-2])
    big_list.append(small)
    small_list.append(big)
    big_list_sum = sum(big_list)
    small_list_sum = sum(small_list)
    if big_list_sum > small_list_sum:
        return((big_list,small_list))
    else:mean(sorted_list[:-2])
        return ((small_list, big_list))


test = [
    [1,2,3,4,5,6,700,800],
    [10001,10000,100,90,50,1],
    [x for x in range(1, 11)],
    [12312,12311,232,210,30,29,3,2,1,1]
]

for l in test:
    l.sort()

    print()
    print('Source List:   ', l)
    l1, l2 = mean(l)
    print('Result List:   ', l1, l2)
    print ('Distance:   ', abs(sum(l1) - sum(l2)))
    print ('-*' * 40)