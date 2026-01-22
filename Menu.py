from WaterRegister import WaterRegister
from ActivityRegister import ActivityRegister


class Menu:
    def __init__(self):
        self.water_register = WaterRegister()
        self.activity_register = ActivityRegister()

    def display(self):
        print("-----------------------------------")
        print("1. Log Water Intake")
        print("2. Log Activity Time")
        print("3. View Daily Totals")
        print("4. Reset Data")
        print("5. Exit")
        print("-----------------------------------")

    def get_choice(self):
        choice = input("Please select an option (1-5): ")
        return choice

    def run(self):
        print("Welcome to the Personal Health Tracker!")
        while True:
            self.display()
            choice = self.get_choice()

            if choice == '1':
                # user input for water intake
                print("Logging Water Intake...")
                print("Enter the amount of water (in ounces): ")
                water_input = input()
                try:
                    self.water_register.add_water(float(water_input))
                    if self.water_register.check_goal():
                        print(
                            "Congratulations! You've reached your daily water intake goal!")
                except (ValueError, TypeError) as e:
                    print(f"Invalid input: {e}")
            elif choice == '2':
                # user input for activity time
                print("Logging Activity Time...")
                print("Enter the activity name: ")
                activity_name = input()
                print("Enter the time spent (in minutes): ")
                time_input = input()
                try:
                    self.activity_register.add_activity(
                        activity_name, float(time_input))
                except (ValueError, TypeError) as e:
                    print(f"Invalid input: {e}")
            elif choice == '3':
                # user input for view daily totals
                print("Daily Totals:")
                print(
                    f"Total Water Intake: {self.water_register.get_water_intake()} Ounces")
                print(
                    f"Total Activity Time: {self.activity_register.get_total_time()} Minutes")
            elif choice == '4':
                # user input for values reset
                print("Resetting Data...")
                print("Are you sure you want to reset all data? (yes/no):")
                confirm = input().lower()
                if confirm == 'yes':
                    self.water_register.reset()
                    self.activity_register.reset()
                    print("All data has been reset.")
                else:
                    print("Data reset canceled.")
            elif choice == '5':
                # user input for exit
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
