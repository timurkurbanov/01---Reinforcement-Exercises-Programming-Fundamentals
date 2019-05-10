#Create the following list in Python:

# [
# {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
# {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
# {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
# {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
# {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
# {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
# {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
# {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
# ]

def get_trains(schedule, direction):
    trains = []
    for train in schedule:
        if train['direction'] == direction:
            trains.append(train)
    return trains


train_schedule = [
    {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
    {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
    {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
    {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
    {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
    {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

direction_train_111 = "south"
frequency_train_80B = 30
direction_train_610 = "north"


print(get_trains(train_schedule, "east"))
print(get_trains(train_schedule, "north"))


train = train_schedule[0]
train['first_departure_time'] = 6
print(train_schedule)
