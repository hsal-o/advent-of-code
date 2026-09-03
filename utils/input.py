def get_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except Exception:
        print(f"File '{file_name}' not found")
        return None