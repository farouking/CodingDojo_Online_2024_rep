#Create a class
class User:
    #! Constructor
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    #method display_info:

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("S Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)

    #method enroll:

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print("Enrolled successfully!")

    #method spend_points:
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"Spend {amount} points successfully!")
        else:
            print("Insufficient points!")

# Test:

# Create two more instances of the User class
user1 = User("Alice", "Smith", "alice@example.com", 25)
user2 = User("Bob", "Johnson", "bob@example.com", 35)

# Example usage:

print("Before spending points:")
user1.display_info()
#First user:(user1) spend 50 point:
print("\n after Spending points...")
user1.spend_points(50)

#second user : user2 have to enroll
# Example usage:
print("\nBefore enrollment:")
user2.display_info()

print("\nEnrolling user 2...")
user2.enroll()

print("\nAfter enrollment:")
user2.display_info()

#Second user:(user2) spend 80 point:

print("Before spending points:")
user2.display_info()
print("\n after Spending points...")
user2.spend_points(80)