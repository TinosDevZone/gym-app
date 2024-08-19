# Main.py

class FitnessCentreApp:
    def __init__(self):
        self.class_schedule = {}
        self.bookings = {}
        self.trainer_profiles = {}
        self.user_account = {}

    def show_menu(self):
        print("Welcome to Arcade Abs App!")
        print("1. View Class Schedule")
        print("2. Book a Class")
        print("3. View Trainer Profiles")
        print("4. Manage User Account")
        print("5. Exit")

    def view_class_schedule(self):
        print("Class Schedule:")
        for day, classes in self.class_schedule.items():
            print(f"{day}: {', '.join(classes)}")

    def book_class(self):
        day = input("Enter the day for booking: ")
        class_name = input("Enter the class name: ")
        if day in self.class_schedule and class_name in self.class_schedule[day]:
            if day not in self.bookings:
                self.bookings[day] = []
            self.bookings[day].append(class_name)
            print(f"Booked {class_name} for {day}")
        else:
            print("Class not available on that day.")

    def view_trainer_profiles(self):
        print("Trainer Profiles:")
        for trainer, info in self.trainer_profiles.items():
            print(f"{trainer}: {info}")

    def manage_user_account(self):
        print("User Account:")
        for key, value in self.user_account.items():
            print(f"{key}: {value}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.view_class_schedule()
            elif choice == '2':
                self.book_class()
            elif choice == '3':
                self.view_trainer_profiles()
            elif choice == '4':
                self.manage_user_account()
            elif choice == '5':
                print("Thank you for using Fitness Centre App!")
                break
            else:
                print("Invalid choice. Please try again.")

# Sample data
app = FitnessCentreApp()
app.class_schedule = {
    "Monday": ["Yoga", "Zumba"],
    "Tuesday": ["Pilates", "Spinning"],
    "Wednesday": ["Boxing", "HIIT"]
}
app.trainer_profiles = {
    "John": "Yoga and Pilates expert",
    "Sarah": "Cardio and HIIT specialist"
}
app.user_account = {
    "Name": "Alex",
    "Membership": "Gold",
    "Classes Attended": 10
}

# Run the app
if __name__ == "__main__":
    app.run()