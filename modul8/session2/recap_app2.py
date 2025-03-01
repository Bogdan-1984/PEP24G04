"""
A shoe factory needs an iterable object to keep track of shoes produces by each worker each day.
Each worker has a string name and each shoe has an int serial number.
Object will have an instance variable tha will keep track of workers trying to cheat in the form of a list of names.
Iterating the object will return the serial numbers produced that day by all workers
1) 40p: Definition
    a) 5p: Class with constructor that receives the date in the format you desire
    b) 25p: Method for adding work done by worker
        - 5p: argument: 5p
            - 1 receives worker name as string
            - 2 receives series produced as list of ints
        - 10p: using this method more than once for the same worker allows the worker to add new values but not
            retransmit old values .In case existing value is entered by two workers a specific exception
            (DuplicateDataException - created by you) and inheriting ValueError will be raised.
            (ex name1: 100, 101; name2: 101, 102; results in exception DuplicateDataException) 10p
        - 10p: method validates that series introduced do not already belong to another worker. In case of conflict
            series will be removed from both workers and information will be added to instance variable that tracks
            cheating workers and then ValueError with message: "Conflict series: <series>, Workers: <nume1>, <nume2>"
            will be raised
    c) 10p: Iterating this object will return an instance of an iterator that will have all series produced that day
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add data for the following workers:
        - Joe: 402, 403, 409
        - Ana: 399, 404, 405
        - Tim: 400, 401, 406
        - workerX: 406, 407, 408 - after adding workerX, workerX will have 407, 408 and Tim will have 400, 401
    c) 10p: Add data for Tim: 400, 401 and check that DuplicateDataException is raised
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""
from datetime import datetime


class DuplicateDataException(ValueError):
    """ABC COMMENT"""
    pass


class ShoeProductionIterator:
    def __iter__(self):
        return self

    def __next__(self):
        if not self.all_series:
            raise StopIteration
        return self.all_series.pop()

    def __init__(self, data):
        self.data: dict[str: set] = data
        self.all_series = []
        for series in self.data.values():
            self.all_series.extend(list(series))


class ShoeProduction:
    """Keeps track or series produces in factory by each worker"""

    def __init__(self, date=datetime.now()):
        self.date = date
        self.worker_data: dict[str: set] = {}
        self.bad_workers: dict[int: list[str, str]] = {}

    def add_work(self, worker_name: str, series: list[int]):
        """Allows adding work series for a specific worker"""

        for worker, series_ in self.worker_data.items():
            duplicate = set(series).intersection(series_)
            if duplicate:
                self.worker_data[worker].difference_update(duplicate)
                self.bad_workers.update({duplicate.copy().pop(): [worker, worker_name]})
                break
        else:
            result = self.worker_data.get(worker_name, set())
            result.update(series)
            self.worker_data.update({worker_name: result})
            return None

        result = self.worker_data.get(worker_name, set())
        limited_series = set(series)
        limited_series.difference_update(duplicate)
        result.update(limited_series)
        self.worker_data.update({worker_name: result})
        raise DuplicateDataException

    def __iter__(self):
        return ShoeProductionIterator(self.worker_data)


if __name__ == "__main__":
    shoe_prod = ShoeProduction(datetime(year=2024, month=12, day=16))
    shoe_prod.add_work("Joe", [402, 403, 409])
    shoe_prod.add_work("Ana", [399, 404, 405])
    shoe_prod.add_work("Tim", [400, 401, 406])
    try:
        shoe_prod.add_work("workerX", [406, 407, 408])
    except DuplicateDataException:
        for data in shoe_prod.bad_workers.items():
            print(f"Conflict series: {data[0]}, Workers: {data[1][0]}, {data[1][1]}")
    with open("production.txt", "w") as file:
        for serial in shoe_prod:
            file.write(f"{serial}\n")
