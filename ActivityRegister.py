class ActivityRegister:
    def __init__(self):
        self.activities = {}
        self.__time_goal__ = 30  # in minutes

    def add_activity(self, activity, time_spent):
        try:
            self.check_input(time_spent)
        except TypeError:
            raise TypeError("Time must be a number")
        except ValueError:
            raise ValueError("Time cannot be negative")
        self.activities[activity] = time_spent

    def get_activities(self):
        return self.activities

    def get_total_time(self):
        return sum(self.activities.values())

    def check_input(self, input_value):
        if input_value < 0:
            raise ValueError("Time cannot be negative")
        if not isinstance(input_value, (int, float)):
            raise TypeError("Time must be a number")

    def check_goal(self, goal_time):
        total = self.total_time()
        return total >= goal_time

    def reset(self):
        self.activities = {}
        print("Activity data has been reset.")
