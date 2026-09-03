from utils.input import get_lines

def main():
    lines = get_lines("input.txt")
    split_index = lines.index("")
    lines = lines[:split_index] + lines[split_index+1:]

    ranges = [(int(line.split("-")[0]), int(line.split("-")[1]) )for line in lines[:split_index]]
    ids = [int(num) for num in lines[split_index:]]

    fresh_count = 0
    for id in ids:
        for min, max in ranges:
            if min <= id <= max:
                fresh_count += 1
                break

    print(f"fresh_count: {fresh_count}")

            
if __name__ == "__main__":
    main()