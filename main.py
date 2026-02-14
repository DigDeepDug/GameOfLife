# have fun!


SIZE = 10

display = [[' ' for i in range(SIZE)] for i in range(SIZE)]

display[5][5] = 'a'
display[5][6] = 'a'
display[5][7] = 'a'


print(display)


should_continue = True
generation = 1

gen_char = ord('a')



for n in range(5):
    print(generation)
    new_display = display
    for i in range(SIZE):
        for j in range(SIZE):
            cur_char = display[i][j]
            neighbor_count = 0
            check_list = ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1))

            for k, l in check_list:
                if k > 0 and l > 0 and k < SIZE and l < SIZE:
                    if display[k][l] != ' ':
                        neighbor_count += 1
            
            if display[i][j] == ' ':
                if neighbor_count == 3:
                    new_display[i][j] = 'a'
            elif neighbor_count < 2 or neighbor_count > 3:
                new_display[i][j] = ' '
            else:
                new_display[i][j] = 'a'


    display = new_display
    
    for i in range(SIZE):
        print(display[i])




    generation += 1

