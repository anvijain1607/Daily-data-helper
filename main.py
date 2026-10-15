class DailyMessage:
    def get_message(self):
        message = input("Enter today's message: ")
        print("Message in uppercase:", message.upper())


class HelperSession:
    def __init__(self):
        print("Session started")

    def __del__(self):
        print("Session ended")


class PairFinder:
    def find_pair(self, numbers, target):
        seen = {}

        for i, num in enumerate(numbers):
            if target - num in seen:
                return seen[target - num], i

            seen[num] = i

        return None


DailyMessage().get_message()

session = HelperSession()

numbers = (10, 20, 30, 40, 50, 60, 70)
target = int(input("Enter target sum: "))

result = PairFinder().find_pair(numbers, target)

if result:
    print(f"index1={result[0]}, index2={result[1]}")
else:
    print("No matching pair found.")

del session
print("Program End")
