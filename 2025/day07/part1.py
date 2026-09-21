from utils.input import get_lines

def get_start_pos(line):
    return (line.find("S"), 0)

def do_beam_collision(
        lines, 
        start_pos, 
        visited, 
        split_points
    ):

    curr_x, curr_y = start_pos

    if (curr_x, curr_y) in visited:
        return

    visited.add((curr_x, curr_y))

    while(True):
        if (curr_x < 0 or curr_x >= len(lines[0])
            or curr_y < 0 or curr_y >= len(lines)):
            # We exited the grid
            return
        
        if lines[curr_y][curr_x] == "^":
            break

        # lines[curr_y] = lines[curr_y][:curr_x] + "|" + lines[curr_y][curr_x+1:]
        curr_y += 1

    # We're here if we found a split point ("^")
    split_points.add((curr_x, curr_y))

    # Recursively split beam to continue
    do_beam_collision(
        lines, 
        (curr_x-1, curr_y),
        visited,
        split_points
    )
    do_beam_collision(
        lines, 
        (curr_x+1, curr_y),
        visited,
        split_points
    )


def main():
    lines = get_lines("input.txt")

    visited = set()
    split_points = set()
    start_pos = get_start_pos(lines[0])

    do_beam_collision(
        lines, 
        start_pos,
        visited,
        split_points
    )

    # for line in lines:
    #     print(line)

    print(f"count: {len(split_points)}")

if __name__ == "__main__":
    main()