from utils.input import get_lines

def main():
    lines = get_lines("input.txt")

    coords = [[int(x) for x in line.split(",")] for line in lines]
    max_area = 0

    for i in range(len(coords)):
        x1, y1 = coords[i]

        for j in range (i+1, len(coords)):
            x2, y2 = coords[j]

            area = (abs((x2 - x1)) + 1) * (abs((y2 - y1)) + 1) # add one to each since endpoints are included in the rectangle

            if area > max_area:
                max_area = area

    print(max_area)

            
if __name__ == "__main__":
    main()