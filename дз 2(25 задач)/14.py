class log_operation():
    def __init__(self, file, proces):
        self.file = file
        self.proces = proces
    def __enter__(self):
        with open(self.file, "a", encoding="UTF-8") as f:
            f.write(f"START:{self.proces}\n")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            with open(self.file, "a", encoding="UTF-8") as f:
                f.write(f"END:{self.proces}\n")
        else:
            with open(self.file, "a", encoding="UTF-8") as f:
                f.write(f"ERROR:{self.proces}\n")

        return False

with log_operation("operation.log", "Data processing"):
    print("...") 