from random import choice

class RandomWalk():
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.distance = [3,4,5,6]
        self.x_direction = [5,-5]
        self.y_direction = [5,-5]
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:
            x_step = self.get_step(self.x_direction)
            y_step = self.get_step(self.y_direction)

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self, direction):
        """Calculate step."""
        return choice(direction) * choice(self.distance)
