from utils.input import get_lines

def main():
    lines = get_lines("input.txt")
    lines = [[item.strip() for item in line.split(" ") if item.strip()] for line in lines]

    digit_lines = lines[:len(lines)-1]
    symbol_lines = lines[len(lines)-1:][0]

    num_col = len(digit_lines[0])
    num_row = len(digit_lines)

    total = 0
    for col in range(num_col):
        result = 0
        symbol = symbol_lines[col]

        for row in range(num_row):
            num = int(digit_lines[row][col])

            if symbol == "+":
                result += num
            elif symbol == "*": 
                if(result == 0):
                    result = num
                else:
                    result *= num

        total += result

    print(f"total: {total}")

if __name__ == "__main__":
    main()