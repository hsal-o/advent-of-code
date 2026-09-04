from utils.input import get_lines

def main():
    lines = get_lines("input.txt")
    split_index = lines.index("")
    lines = lines[:split_index] + lines[split_index+1:]

    ranges = [(int(line.split("-")[0]), int(line.split("-")[1]) )for line in lines[:split_index]]

    # Merge overlapping ranges
    i_index = 0
    while i_index < len(ranges):
        i_min, i_max = ranges[i_index]

        for j_index, (j_min, j_max) in enumerate(ranges):
            if i_index == j_index:
                # Skip current
                continue

            if i_max < j_min or i_min > j_max:
                # They dont overlap
                continue

            # Safe to assume they overlap

            true_min = i_min
            true_max = i_max

            if i_min <= j_min:
                true_min = i_min
            else:
                true_min = j_min

            if i_max >= j_max:
                true_max = i_max
            else:
                true_max = j_max

            ranges = ranges[:i_index] + ranges[i_index+1:]
            ranges = ranges[:(j_index-1)] + ranges[(j_index-1)+1:]
            ranges.append((true_min, true_max))
            i_index = -1 # start at the beginning again
            break

        i_index += 1

    # Count fresh id's
    fresh_count = 0
    for min, max in ranges:
        fresh_count += (max-min) + 1
            
    print(f"fresh_count: {fresh_count}")

if __name__ == "__main__":
    main()