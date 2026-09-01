def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None


def main():
    lines = get_lines_from_file("input.txt")

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