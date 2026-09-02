from utils.input import get_lines

def main():
    banks = get_lines("input.txt")

    sum = 0
    for bank in banks:
        bank = [int(num) for num in bank.strip()]

        max_voltage = 0
        for ptr_i in range(0, len(bank)-1): 

            for ptr_j in range(ptr_i+1, len(bank)):
                voltage = bank[ptr_i]*10 + bank[ptr_j]
                if voltage > max_voltage:
                    max_voltage = voltage

        sum += max_voltage

    print(f"sum: {sum}")         

if __name__ == "__main__":
    main()