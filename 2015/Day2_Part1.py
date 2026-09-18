
with open("2015/Day2_input.txt") as f:
    entries = f.read().split()

total_paper = 0

for entry in entries:
    l, w, h = map(int, entry.split("x"))

    sides = [l*w, h*w, l*h]

    surface_area = 2 * sum(sides)
    slack = min(sides)

    total_paper += surface_area + slack

print(total_paper)




