class School():
    total_std = 0

    def __init__(self, name):
        self.name = name
        School.total_std += 1 

    @classmethod
    def num_std(cls):
        print(f"total students : {cls.total_std}")

    @staticmethod
    def is_valid(name):
        if len(name) > 0:
            print(f"{name} is valid name.")
        else:
            print(f"{name} is invalid name!")


s1 = School("Krishna")
s2 = School("Rudra")

School.num_std()
School.is_valid("krishna")
School.is_valid("")
