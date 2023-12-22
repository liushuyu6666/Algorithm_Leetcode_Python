# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Validator:
    def __init__(self):
        self.store = set()

    def append(self, value: int) -> bool:
        if value in self.store:
            return False
        else:
            self.store.add(value)
        return True


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    validator = Validator()
    print(validator.append(123))
    print(validator.append(123))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
