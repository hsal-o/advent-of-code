from utils.input import get_lines

collisions = 0

def get_start_pos(line):
    return (line.find("S"), 0)

def get_beam_collision(lines, start_pos):
    curr_x, curr_y = start_pos

    if (curr_x < 0 or curr_x >= len(lines[0])
        or curr_y < 0 or curr_y >= len(lines)):
        return

    curr_y += 1 # Shift to next line

    while(True):

        if lines[curr_y][curr_x] == "^":
            break

        lines[curr_y] = lines[curr_y][:curr_x] + "|" + lines[curr_y][curr_x+1:]


        curr_y += 1

    print(f"'^' detected on ({curr_x}, {curr_y})")
    collisions += 1

    get_beam_collision(lines, (curr_x-1, curr_y))
    get_beam_collision(lines, (curr_x+1, curr_y))



def main():
    lines = get_lines("input.txt")

    start_pos = get_start_pos(lines[0])

    get_beam_collision(lines, start_pos)

    for line in lines:
        print(line)



if __name__ == "__main__":
    main()