from utils.input import get_lines

empty_char   = "."
roll_char    = "@"

def main():
    grid = [line.strip() for line in get_lines("input.txt")]

    count = 0

    def get_neighboring_empty_count(x, y):
        neighbor_count = 0

        for j in range(-1, 2):
            _y = y + j
            if (_y < 0  
                or _y >= len(grid)
                ):
                continue

            for i in range(-1, 2):
                _x = x + i
                if(_x < 0 
                    or _x >= len(grid[_y]) 
                    or (_x == x and _y == y)
                    ):
                    continue

                if grid[_y][_x] == roll_char:
                    neighbor_count += 1

        return neighbor_count

    # Store all positions that hold roll chars ("@")
    roll_positions = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == roll_char:
                roll_positions.append((x, y))

    # Count neighboring empty positions for each roll position
    for x, y in roll_positions:
        neighbor_count = get_neighboring_empty_count(x, y)
        if neighbor_count < 4:
            count += 1

    print(f"count: {count}")

if __name__ == "__main__":
    main()