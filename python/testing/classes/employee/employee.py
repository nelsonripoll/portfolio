class Employee():
    """Collect anonymous answers to a survey question."""

    def __init__(self, first_name, last_name, salary):
        """Store employee first and last name along with their salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        """Raise employee's salary by given amount, 5000 by default."""
        self.salary += raise_amount
