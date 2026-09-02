def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

# Square root approach for getting factors
def get_factors(num):
    factors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)

    factors.discard(num) # we dont want the number itself

    return sorted(factors)

def main():
    raw = get_lines_from_file("input.txt")[0].split(",")
    ranges = [[int(num) for num in item.split("-")] for item in raw]

    sum = 0

    for first, last in ranges:
        for num in range(first, last+1):
            s = str(num)

            factors = get_factors(len(s))
            for f in factors:
                # split string s evenly into strings of size f
                list = [s[i:i+f] for i in range(0, len(s), f)]

                if len(set(list)) == 1:
                    sum += num
                    break

    print(f"sum: {sum}")

if __name__ == "__main__":
    main()