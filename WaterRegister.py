class WaterRegister:
    def __init__(self, volume_ounces):
        self.volume_ounces = volume_ounces
        self.__volume_goal__ = 64

    def add_water(self, input_ounces):
        try:
            self.check_input(input_ounces)
        except TypeError:
            raise TypeError("Volume must be a number")
        self.volume_ounces += input_ounces
        print(f"Added {input_ounces} ounces of water.")

    def get_water_intake(self):
        return self.volume_ounces

    def check_input(self, input_value):
        if input_value < 0:
            raise ValueError("Volume cannot be negative")
        if not isinstance(input_value, (int, float)):
            raise TypeError("Volume must be a number")

    def check_goal(self):
        return self.volume_ounces >= self.__volume_goal__

    def reset(self):
        self.volume_ounces = 0
        print("Water intake has been reset.")
