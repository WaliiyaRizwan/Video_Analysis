
def load_bad_words(file_path):
    print(file_path)
    with open(file_path, "r") as file:
        return [line.strip() for line in file]