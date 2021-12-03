def day1():
    data = open("data_day1_a.txt", "r")
    increased = 0
    prev_value = 0
    for value in data:
        if prev_value != 0:
            print(type(value))



day1()
