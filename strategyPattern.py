from abc import ABC, abstractmethod

# Abstract base class for filter strategies
class FilterStrategy(ABC):
    
    # Abstract method to be implemented by concrete strategies
    @abstractmethod
    def removeValue(self, val):
        pass

# Concrete strategy to remove negative values
class RemoveNegativeStrategy(FilterStrategy):
    
    # Returns True if the value is negative, indicating it should be removed
    def removeValue(self, val):
        return val < 0

# Concrete strategy to remove odd values
class RemoveOddStrategy(FilterStrategy):
    
    # Returns True if the value is odd, indicating it should be removed
    def removeValue(self, val):
        return abs(val) % 2 == 1

# Class to hold and filter a list of values
class Values:
    def __init__(self, vals):
        self.vals = vals  # Initialize with a list of values
    
    # Filters the values using a given filter strategy
    def filter(self, strategy):
        res = []  # Initialize an empty list for filtered results
        for n in self.vals:  # Iterate through each value
            # If the strategy doesn't recommend removal, keep the value
            if not strategy.removeValue(n):
                res.append(n)
        return res  # Return the filtered list

# Create a Values instance with a list of integers
values = Values([-7, -4, -1, 0, 2, 6, 9])

# Apply the RemoveNegativeStrategy and print the result
print(values.filter(RemoveNegativeStrategy()))  # Output: [0, 2, 6, 9]

# Apply the RemoveOddStrategy and print the result
print(values.filter(RemoveOddStrategy()))  # Output: [-4, 0, 2, 6]
