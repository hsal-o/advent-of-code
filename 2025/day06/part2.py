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

        # Find the # of numbers we have to construct = max length
        max_length = 0
        for row in range(num_row):
            length = len(digit_lines[row][col])
            if length > max_length:
                max_length = length

        numbers = ["" for _ in range(max_length)]
        
        for i in range(len(numbers)): 

            for row in range(num_row):
                num = digit_lines[row][col]

                # Skip if number has been stripped completely
                if(not num):
                   continue

                # Build number using the last digit of number
                numbers[i] += num[-1]

                # Strip away last digit from number
                digit_lines[row][col] = num[:len(num)-1]


        if symbol == "+":
            for num in numbers:
                result += int(num)
            
        elif symbol == "*":
            for num in numbers:
                if result == 0:
                    result = int(num)
                else:
                    result *= int(num)

        print(f"numbers: {numbers} \t\treuslt: {result}")

        total += result

    print(f"total: {total}")

if __name__ == "__main__":
    main()