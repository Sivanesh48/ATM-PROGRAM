class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to store User objects

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        return None

    def display_menu(self):
        # Display the available operations in the console
        pass

    def execute_operation(self, user, choice):
        # Implement the selected operation based on the user's choice
        pass

# Example usage
if __name__ == "__main__":
    atm = ATM()

    # Create user accounts
    user1 = User("vignesh", "8772", 1000)
    user2 = User("vicky", "2778", 500)

    atm.add_user(user1)
    atm.add_user(user2)

    # User authentication
    user_id_input = input("Enter User ID: ")
    pin_input = input("Enter PIN: ")

    current_user = atm.authenticate_user(user_id_input, pin_input)

    if current_user:
        print("Authentication successful. Welcome, {}!".format(current_user.user_id))
        atm.display_menu()
        user_choice = input("Enter your choice: ")
        atm.execute_operation(current_user, user_choice)
    else:
        print("Authentication failed. Please check your User ID and PIN.")
