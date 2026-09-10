def get_lines(file_name, strip=True):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            if(strip):
                return [line.strip() for line in lines]
            else:
                return [line.rstrip("\n") for line in lines]
    except Exception:
        print(f"File '{file_name}' not found")
        return None
