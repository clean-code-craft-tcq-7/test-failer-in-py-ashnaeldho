def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    colorCode = {}
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            colorCode[str({major} | {minor})] = i * 5 + j
    return len(major_colors) * len(minor_colors)
result = print_color_map()
assert(result == 25)
assert(colorCode[str({"White"} | {"Green"})] == 3)
assert(colorCode[str({"Black"} | {"Slate"})] == 15)
print("All is well (maybe!)\n")
