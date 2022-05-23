
for first_num in range(1, 1000, 2):
    second_num = first_num**3
    third_num = []
    third_num.append(second_num)
    print(third_num)
    for i in third_num:
        fourth_num = sum(map
                         (int,
                          str(i)
                          )
                         )
        if fourth_num % 7 == 0:
            print(fourth_num)
            last_num = fourth_num + 17
            if last_num % 7:
                print(last_num)


