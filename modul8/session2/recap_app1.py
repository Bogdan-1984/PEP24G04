"""
A production facility needs an iterable object to keep track product assembly times.
A class called "KeyboardProductionTimes" that will store the information needs to be created.
Each keyboard will have a string serial number "KBXXXXXX" and timedelta (or int) for production time
Iterating objects created with KeyboardProductionTimes will return all keyboards that had production
time greater than 2000s
1) 40p: Definition
    a) 10p: Basic class structure of KeyboardProductionTimes
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add produced keyboards with serial and time
    d) 10p: Method that returns average keyboard production time
2) 40p: Execution:
    a) 10p: Create instance of KeyboardProductionTimes
    b) 10p: Call method to add keyboard <add_keyboard(serial, <timedelta | int>)>
        - KB023871, 3210s
        - KB023873, 1890s
        - KB023875, 1982s
    c) 10p: Call method to return average production time <average_production_time()>
    d) 10p: Iterate the created object and write each keyboard serial with production
            time greater then 2000s in a file on a new line
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""

# chat GPT

from datetime import timedelta
from typing import List, Iterator, Tuple, Union


class KeyboardProductionTimes:
    """
    Tracks production times for keyboards and provides an iterable to filter keyboards with production
    times greater than 2000 seconds.
    """

    def __init__(self):
        """
        Initializes an empty list to store keyboard production data.
        """
        self._keyboards: List[Tuple[str, Union[timedelta, int]]] = []

    def add_keyboard(self, serial: str, time: Union[timedelta, int]) -> None:
        """
        Adds a keyboard's production time to the storage.
        Args:
            serial (str): The keyboard's serial number (e.g., "KBXXXXXX").
            time (Union[timedelta, int]): The production time for the keyboard.
        """
        self._keyboards.append((serial, time))

    def average_production_time(self) -> Union[float, None]:
        """
        Calculates the average production time for all keyboards.
        Returns:
            Union[float, None]: The average production time in seconds, or None if no keyboards are present.
        """
        if not self._keyboards:
            return None
        total_time = sum(
            time.total_seconds() if isinstance(time, timedelta) else time
            for _, time in self._keyboards
        )
        return total_time / len(self._keyboards)

    def __iter__(self) -> Iterator[str]:
        """
        Returns an instance of KeyboardIterator to iterate over keyboards with production times > 2000 seconds.
        Returns:
            Iterator[str]: An instance of KeyboardIterator.
        """
        return KeyboardIterator(self._keyboards)


class KeyboardIterator:
    """
    Iterator class to filter keyboards with production times greater than 2000 seconds.
    """

    def __init__(self, keyboards: List[Tuple[str, Union[timedelta, int]]]):
        """
        Initializes the iterator with the list of keyboards.
        Args:
            keyboards (List[Tuple[str, Union[timedelta, int]]]): List of keyboards with their production times.
        """
        self._keyboards = keyboards
        self._index = 0

    def __iter__(self) -> "KeyboardIterator":
        return self

    def __next__(self) -> str:
        """
        Returns the next keyboard serial number with production time > 2000 seconds.
        Returns:
            str: The serial number of the next qualifying keyboard.
        Raises:
            StopIteration: When no more keyboards meet the criteria.
        """
        while self._index < len(self._keyboards):
            serial, time = self._keyboards[self._index]
            self._index += 1
            if (time.total_seconds() if isinstance(time, timedelta) else time) > 2000:
                return serial
        raise StopIteration


if __name__ == "__main__":
    # Create an instance of the class
    production_times = KeyboardProductionTimes()
    # Add keyboard production times
    production_times.add_keyboard("KB023871", 3210)
    production_times.add_keyboard("KB023873", 1890)
    production_times.add_keyboard("KB023875", 1982)
    # Calculate and display the average production time
    avg_time = production_times.average_production_time()
    print(f"Average Production Time: {avg_time} seconds")
    # Write keyboards with production time > 2000s to a file
    with open("keyboards_above_2000s.txt", "w") as file:
        for serial in production_times:
            file.write(f"{serial}\n")
    print("Keyboards with production time > 2000 seconds written to file.")

# Nvidia

from typing import Dict, List, Union
from datetime import timedelta


class KeyboardProductionTimes:
    def __init__(self):
        self.keyboards: Dict[str, Union[timedelta, int]] = {}

    def __iter__(self):
        return KeyboardProductionTimesIterator(self.keyboards)

    def add_keyboard(self, serial: str, time: Union[timedelta, int]):
        self.keyboards[serial] = time

    def average_production_time(self) -> Union[timedelta, int]:
        total_time = sum(time for time in self.keyboards.values())
        return total_time / len(self.keyboards)


class KeyboardProductionTimesIterator:
    def __init__(self, keyboards: Dict[str, Union[timedelta, int]]):
        self.keyboards = keyboards
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.keyboards):
            raise StopIteration

        serial, time = list(self.keyboards.items())[self.current_index]
        self.current_index += 1

        if time > 2000:
            return serial, time
        else:
            return self.__next__()


production_times = KeyboardProductionTimes()

production_times.add_keyboard("KB023871", 3210)
production_times.add_keyboard("KB023873", 1890)
production_times.add_keyboard("KB023875", 1982)

average_time = production_times.average_production_time()
print(f"Average production time: {average_time}")

with open("production_times.txt", "w") as file:
    for serial, time in production_times:
        file.write(f"{serial}: {time}\n")
