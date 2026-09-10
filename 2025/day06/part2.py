from utils.input import get_lines

def get_column_lens(symbols):
    counts = []
    count = 1 # Start at one since we count current char
    for i in range(len(symbols)):
        if(symbols[i] in ["+", "*"]):
            counts.append(count - 1) # Dont include current symbol
            count = 1
            continue

        count += 1

        # Append last column before finishing loop        
        if i+1 >= len(symbols):
            counts.append(count)

    return counts[1:] # Exclude first element since first char in symbol is a symbol

def get_expression_result(symbol, numbers):
    result = 0
    if symbol == "+":
        for num in numbers:
            result += int(num)
    elif symbol == "*":
        for num in numbers:
            if result == 0:
                result = int(num)
            else:
                result *= int(num)

    return result

def main():
    lines = get_lines("input.txt", False)
    
    symbol_line = lines[-1]
    lines = lines[:len(lines)-1]

    column_lens = get_column_lens(symbol_line)

    total = 0
    curr_index = 0
    for length in column_lens:
        # Collect raw numbers from column
        raw_numbers = []
        for row in lines:
            raw_numbers.append(row[curr_index:curr_index + length])

        # Build new numbers from raw numbers
        new_numbers = ["" for _ in range(length)]
        for i in range(len(new_numbers)):
            for j, raw_num in enumerate(raw_numbers):
                # Skip if stripped completely
                if raw_num == "":
                    continue

                # Build new number using last digit of number
                if(raw_num[-1] != " "):
                    new_numbers[i] += raw_num[-1]

                # Strip away last digit from original number
                raw_numbers[j] = raw_num[:len(raw_num)-1]

        # Add expression result to total
        total += get_expression_result(symbol_line[curr_index], new_numbers)

        # Shift over to new column
        curr_index += length + 1   

    print(f"total: {total}")

if __name__ == "__main__":
    main()