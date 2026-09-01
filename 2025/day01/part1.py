from utils.input import get_lines

def main():
    lines = get_lines("input.txt")

    curr_point = 50
    count = 0

    for line in lines:
        dir = line[0]
        rot = int(line[1:])

        if dir == "R":
            curr_point = (curr_point + rot) % 100
        else:
            curr_point = (curr_point - rot) % 100

        if curr_point == 0:
            count += 1

    print(f"count: {count}")


if __name__ == "__main__":
    main()