from utils.input import get_lines

def main():
    banks = get_lines("input.txt")

    sum = 0

    for bank in banks:
        bank = bank.strip() # strip off trailing 
        max_voltage = 0

        # convert bank to dicitonary -> key = number, value = list of positions
        dict = {num: [] for num in sorted(set(bank), reverse=True)}
        for i, num in enumerate(bank):
            dict[num].append(i)

        keys = list(int(num) for num in dict.keys())

        # find highest voltage
        for i in range(len(keys) - 1):
            i_key = keys[i]                             # grab the i'th key
            i_key_indexes = dict[str(i_key)]            # grab the corresponding i'th key's value pair

            for j in range(0, len(keys)):               # iterate through all keys
                j_key = keys[j]                         # grab the j'th key
                j_key_indexes = dict[str(j_key)]        # grab the corresponding j'th key's value pair

                # check to see if theres any index in j_key_indexes that is >= than any index in i_key_indexes
                min_i_index = sorted(i_key_indexes)[0]
                max_j_index = sorted(j_key_indexes, reverse=True)[0]

                # check to confirm that j comes AFTER i, since i will be first digit, and j will be second
                if max_j_index > min_i_index:
                    voltage = int(f"{i_key}{j_key}")
                    if voltage >= max_voltage:
                        max_voltage = voltage

            if max_voltage != 0:
                # no need to continue... future i_keys will be smaller
                break

        if max_voltage != 0:
            sum += max_voltage

    print(f"sum: {sum}")         

if __name__ == "__main__":
    main()