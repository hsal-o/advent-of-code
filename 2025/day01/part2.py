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

        prev_point = curr_point

        if dir == "R":
            curr_point = (curr_point + rot) % 100

            if prev_point + rot >= 100:
                remaining = rot - (100 - prev_point)
                count += (remaining // 100) + 1  # passes at least once

        else:
            curr_point = (curr_point - rot) % 100

            if prev_point == 0:
                count += (rot // 100) # does not guarantee a pass unless rotation is large enough

            elif prev_point - rot <= 0:
                remaining = rot - prev_point
                count += (remaining // 100) + 1  # passes at least once

    print(f"count: {count}")


if __name__ == "__main__":
    main()