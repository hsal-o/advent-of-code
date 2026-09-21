from utils.input import get_lines

def get_start_pos(line):
    return (line.find("S"), 0)

def do_beam_collision(
        lines, 
        start_pos, 
        visited, 
        nodes
    ):

    curr_x, curr_y = start_pos

    if (curr_x, curr_y) in visited:
        return

    visited.add((curr_x, curr_y))

    while(True):
        if (curr_x < 0 or curr_x >= len(lines[0])
            or curr_y < 0 or curr_y >= len(lines) - 1):
            # We exited the grid
            nodes[(curr_x, curr_y)] = 0
            return
        
        if lines[curr_y][curr_x] == "^":
            break

        curr_y += 1

    # We're here if we found a split point ("^")
    nodes[(curr_x, curr_y)] = 0

    # Recursively split beam to continue
    do_beam_collision(
        lines, 
        (curr_x-1, curr_y),
        visited,
        nodes
    )
    do_beam_collision(
        lines, 
        (curr_x+1, curr_y),
        visited,
        nodes
    )

def fulfill_beam(x, y, curr_value, nodes):
    max_y = max(node[1] for node in nodes)

    while(y <= max_y):
        if (x, y) in nodes:
            nodes[(x, y)] += curr_value
            return

        y += 1

def main():
    lines = get_lines("input.txt")

    visited = set()
    nodes = {}
    start_pos = get_start_pos(lines[0])

    # Generate nodes
    do_beam_collision(
        lines, 
        start_pos,
        visited,
        nodes
    )

    # Separate points by depth
    points_by_depth = {}
    for (x, y) in nodes.keys():
        if y not in points_by_depth.keys():
            points_by_depth[y] = []
        points_by_depth[y].append((x, y))

    # Instantiate the node below start node
    nodes[start_pos[0], 2] = 1

    # Iterate per depth level, excluding the last depth
    for depth in sorted(points_by_depth.keys())[:-1]:
        for (x, y) in points_by_depth[depth]:
            # split into two beams, and pass down node's value
            fulfill_beam(x-1, y, nodes[(x, y)], nodes)
            fulfill_beam(x+1, y, nodes[(x, y)], nodes)

    # Sum up bottom depth node's values
    sum = 0
    for node in points_by_depth[max(points_by_depth.keys())]:
        sum += nodes[node]
    print(f"sum: {sum}")


if __name__ == "__main__":
    main()