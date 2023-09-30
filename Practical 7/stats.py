import math
import random

class Stats:
    """
    Stats class for working with statistical quantities.
    Attributes:
    mean (float) representing the mean value of the data
    stdev (float) representing the standard deviation of the data
    data (list of floats) a list of floats values read from the data file
    """

    def __init__(self, mean=0, stddev=1):
        self.mean = mean
        self.stddev = stddev
        self.data = []

    def calculate_mean(self):
        """Method to calculate the mean of the data set."""
        if len(self.data) > 0:
            self.mean = sum(self.data) / len(self.data)
        else:
            self.mean = 0

    def calculate_stdev(self):
        """Method to calculate the standard deviation of the data set."""
        if len(self.data) > 1:
            sum_squared_diff = [(x - self.mean) ** 2 for x in self.data]
            self.stddev = math.sqrt(sum(sum_squared_diff) / (len(self.data) - 1))
        else:
            self.stddev = 0

    def generate_data(self, start=1, end=10, count=10):
        """This code generates random numbers between start and stop
        and appends the data to a list called data."""
        data_list = [random.randint(start, end) for _ in range(count)]
        self.data = data_list
        self.calculate_mean()
        self.calculate_stdev()

    def generate_normal_data(self, mean=0, stddev=1, count=10):
        """Method to generate normally distributed data."""
        self.data = [random.gauss(mean, stddev) for _ in range(count)]
        self.calculate_mean()
        self.calculate_stdev()

    @classmethod
    def get_stats_instance(cls, mean=0, stddev=1):
        """Method to create a Stats class instance."""
        return cls(mean, stddev)

    @staticmethod
    def find_max(data):
        return max(data)

    @staticmethod
    def find_min(data):
        if len(data) > 0:
            return min(data)
        else:
            return None

    def __del__(self):
        print("Last Message before deletion")

def main():
    print("Something")
    instance = Stats(3, 5)
    print(type(instance))
    print(instance.mean, "-", instance.stddev)
    print(vars(instance))
    instance.generate_data()
    print(instance.mean, "-", instance.stddev)
    print(instance.data)
    del instance

if __name__ == "__main__":
    main()
