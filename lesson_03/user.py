class User:
    def __init__(self, first_name, last_name):
        self.firtst_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.firtst_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"My name is - {self.firtst_name}"
              f" and lastname is - {self.last_name}")
