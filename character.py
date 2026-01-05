class Character:
    def __init__(self, x_center, y_center, speed):
        # מיקום הדמות
        self.x_center = x_center
        self.y_center = y_center
        self.speed = speed

        self.x_change = 0
        self.y_change = 0
