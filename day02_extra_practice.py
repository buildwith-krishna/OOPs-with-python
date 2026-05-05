class PasswordVault():
    def __init__(self):
        self.__password = None

    def set_password(self, new_pass):
        char = 0
        for ch in new_pass:
            char += 1

        if char < 8:
            print("Password should be at least 8 characters.")
        else:
            self.__password = new_pass
            print("Password Changed")

    def check_pass(self, guess):
        if guess == self.__password:
            print("Access Granted")

        else:
            print("Wrong Password")


new_pass = input("Enter new password: ").strip()
p = PasswordVault()
p.set_password(new_pass)
guess = input("Enter password to access: ").strip()
p.check_pass(guess)   

     
