"""
A production facility needs an iterable object to keep track of remaining warranty for products.
A class called "KeyboardProductionTimes" that will store the information needs to be created.
Each object created with class above will have information regarding serial number ("KBXXXXXX") and
production date (datetime object for production date) corresponding to each serial.
Iterating objects created with KeyboardProductionTimes will return all keyboards for witch warranty is still active
(less than 1000 days)
1) 40p: Definition
    a) 10p: Basic class structure of KeyboardProductionTimes
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add produced keyboards with serial and production date
    d) 10p: Method that returns average keyboard age
2) 40p: Execution:
    a) 10p: Create instance of KeyboardProductionTimes
    b) 10p: Call method to add keyboard <add_keyboard(serial, <datetime>)>
        - KB023871, datetime(2020, 03, 04)
        - KB023873, datetime(2022, 04, 05)
        - KB023875, datetime(2024, 05, 06)
    c) 10p: Call method to return average production time <average_product_age()>
    d) 10p: Iterate the created object and write each keyboard serial and warranty remaining in a file on a new line,
            Only for keyboards that have active warranty (age < 1000 days)
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""

from datetime import datetime

# Module Documentation
"""
This module provides a system for tracking the warranty of keyboards in a production facility.
It includes classes to store keyboard production data, calculate average production age, and
iterate over keyboards with active warranties.
"""

class KeyboardWarrantyTracker:
    """
    A class to track keyboard production data and calculate warranty status.

    Attributes:
        keyboard_data (list): A list of tuples, each containing a serial number (str)
                             and a production date (datetime).
    """

    def __init__(self):
        """
        Initializes an empty list to store keyboard production data.
        """
        self.keyboard_data = []

    def add_keyboard(self, serial_number: str, production_date: datetime) -> None:
        """
        Adds a keyboard's serial number and production date to the data.

        Args:
            serial_number (str): The serial number of the keyboard.
            production_date (datetime): The production date of the keyboard.
        """
        self.keyboard_data.append((serial_number, production_date))

    def calculate_average_age(self) -> float | None:
        """
        Calculates the average age of all keyboards in days.

        Returns:
            float: The average age of keyboards in days. Returns None if no keyboards exist.
            None: No keyboards have been added.
        """
        if not self.keyboard_data:
            return None
        current_date = datetime.now()
        total_days = sum((current_date - production_date).days for _, production_date in self.keyboard_data)
        return total_days / len(self.keyboard_data)

    def __iter__(self):
        """
        Returns an iterator for keyboards with active warranties.

        Returns:
            WarrantyIterator: An iterator over keyboards with active warranties.
        """
        return WarrantyIterator(self.keyboard_data)

class WarrantyIterator:
    """
    An iterator to filter and return keyboards with active warranties.

    Attributes:
        keyboard_data (list): A list of tuples containing serial numbers and production dates.
        current_index (int): The current index of the iteration.
    """

    def __init__(self, keyboard_data: list):
        """
        Initializes the iterator with keyboard data and sets the current index to 0.

        Args:
            keyboard_data (list): A list of tuples containing serial numbers and production dates.
        """
        self.keyboard_data = keyboard_data
        self.current_index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            WarrantyIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next keyboard with an active warranty.

        Returns:
            tuple: A tuple containing the serial number (str) and remaining warranty days (int).

        Raises:
            StopIteration: If there are no more keyboards with active warranties.
        """
        current_date = datetime.now()
        while self.current_index < len(self.keyboard_data):
            serial_number, production_date = self.keyboard_data[self.current_index]
            self.current_index += 1
            age_in_days = (current_date - production_date).days
            remaining_warranty = 1000 - age_in_days
            if remaining_warranty > 0:
                return serial_number, remaining_warranty
        raise StopIteration

if __name__ == "__main__":
    # Create an instance of KeyboardWarrantyTracker
    warranty_tracker = KeyboardWarrantyTracker()

    # Add keyboards with serial numbers and production dates
    warranty_tracker.add_keyboard("KB023871", datetime(2020, 3, 4))
    warranty_tracker.add_keyboard("KB023873", datetime(2021, 4, 5))
    warranty_tracker.add_keyboard("KB023875", datetime(2023, 5, 6))

    # Calculate and print the average age of keyboards
    average_age = warranty_tracker.calculate_average_age()
    if average_age is not None:
        print(f"Average age of keyboards: {average_age:.2f} days")
    else:
        print("No keyboards have been added.")

    # Write active warranty keyboards to a file
    with open("Active_warranty_KB.txt", "w") as file:
        for serial_number, remaining_days in warranty_tracker:
            file.write(f"{serial_number}: {remaining_days} days remaining\n")
    print("Active warranty keyboards written to file.")
