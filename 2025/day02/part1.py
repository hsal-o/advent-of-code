def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None


def main():
    raw = get_lines_from_file("input.txt")[0].split(",")
    ranges = [[int(num) for num in item.split("-")] for item in raw]

    sum = 0

    for first, last in ranges:
        for num in range(first, last+1):
            s = str(num)

            if len(s) % 2 == 0:
                half_length = len(s) // 2

                if s[:half_length] == s[half_length:]:
                    sum += num

    print(f"sum: {sum}")

if __name__ == "__main__":
    main()