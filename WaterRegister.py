class WaterRegister:
    def __init__(self):
        self.volume_ounces = 0
        self.__volume_goal__ = 64

    def add_water(self, input_ounces):
        self.check_input(input_ounces)
        self.volume_ounces += input_ounces
        print(f"Added {input_ounces} ounces of water.")

    def get_water_intake(self):
        return self.volume_ounces

    def check_input(self, input_value):
        if not isinstance(input_value, (int, float)):
            raise TypeError("Volume must be a number")
        if input_value < 0:
            raise ValueError("Volume cannot be negative")

    def check_goal(self):
        return self.volume_ounces >= self.__volume_goal__

    def reset(self):
        self.volume_ounces = 0
        print("Water intake has been reset.")
