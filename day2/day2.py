#f = open("input.txt", "r")
f = open("test_input.txt", "r")

x = 0
y = 0

for direction in f:
    splitted_d = direction.split(" ")

    if splitted_d[0] == 'forward':
       x += int(splitted_d[1].rstrip("\n"))
    elif splitted_d[0] == 'down':
       y += int(splitted_d[1].rstrip("\n"))
    elif splitted_d[0] == 'up':
       y -= int(splitted_d[1].rstrip("\n"))

print(x*y)

x = 0
y = 0
aim = 0

f = open("input.txt", "r")

# up increase aim by x
# down decrease aim by x
# forward increase horizontal position by x and increase depth by aim * x
for direction in f:
    splitted_d = direction.split(" ")
    print('ok')
    if splitted_d[0] == 'forward':
       x += int(splitted_d[1].rstrip("\n"))
       y += aim * int(splitted_d[1].rstrip("\n"))
    elif splitted_d[0] == 'down':
       aim += int(splitted_d[1].rstrip("\n"))
    elif splitted_d[0] == 'up':
       aim -= int(splitted_d[1].rstrip("\n"))

print(f'{x*y} {aim}')
