import timeit

# calculate the time the algorithm takes to run
class Timer:
    def __init__(self):
        self.time_passed = timeit.default_timer()
    def stop(self):
        self.time_passed = round(timeit.default_timer() - self.time_passed, 5)
        print("Program Executed in " + str(self.time_passed) + " seconds.")  # It returns time in seconds