from utils.input import get_lines

max_digits = 12


def main():
    banks = get_lines("input.txt")

    def get_lookahead_pos(_result, _curr_pos):
        return _curr_pos + (max_digits - len(_result) - 1)

    sum = 0
    for bank in banks:
        bank = [int(num) for num in bank.strip()]

        result = ""

        curr_pos = 0
        best_pos = 0
        lookahead_pos = get_lookahead_pos(result, curr_pos)

        while len(result) < max_digits:

            while (lookahead_pos < len(bank) - 1) and bank[best_pos] != 9:
                lookahead_pos = get_lookahead_pos(result, curr_pos)

                if bank[curr_pos] > bank[best_pos]:
                    best_pos = curr_pos

                curr_pos += 1

            result += str(bank[best_pos])
            curr_pos = best_pos + 1
            lookahead_pos = get_lookahead_pos(result, curr_pos)
            best_pos = curr_pos

        sum += int(result)

    print(f"sum: {sum}")         

if __name__ == "__main__":
    main()