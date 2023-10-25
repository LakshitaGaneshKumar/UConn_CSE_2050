class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Compares two points as being equal or not (they are equal if they have the same x and y value)"""
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def equidistant(self, other):
        """Compares if two points are the same distant away from the origin as each other"""
        self_distance = (self.x**2 + self.y**2)**(1/2)
        other_distance = (other.x**2 + other.y**2)**(1/2)

        if self_distance == other_distance:
            return True
        return False

    def within(self, distance, other):
        """Compares if two points are within a given distance from each other"""
        if ((other.x - self.x)**2 + (other.y - self.y)**2)**(1/2) <= distance:
            return True
        return False
