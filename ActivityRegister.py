class ActivityRegister:
    def __init__(self):
        self.activities = {}
        self.__time_goal__ = 30  # in minutes

    def add_activity(self, activity, time_spent):
        self.check_input(time_spent)
        if activity in self.activities:
            self.activities[activity] += time_spent
        else:
            self.activities[activity] = time_spent

    def get_activities(self):
        return self.activities

    def get_total_time(self):
        return sum(self.activities.values())

    def check_input(self, input_value):
        if not isinstance(input_value, (int, float)):
            raise TypeError("Time must be a number")
        if input_value < 0:
            raise ValueError("Time cannot be negative")

    def check_goal(self, goal_time):
        total = self.get_total_time()
        return total >= goal_time

    def reset(self):
        self.activities = {}
        print("Activity data has been reset.")
