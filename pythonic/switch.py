

def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknown'


switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}

day_name = switcher.get(1, get_default)()
print(day_name)
day_name = switcher.get(6, get_default)()
print(day_name)
