"""
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
pass
controller = TVController(CHANNELS)
"""


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.position = 0

    def first_channel(self):
        self.position = 0
        return self.current_channel()

    def last_channel(self):
        self.position = len(self.channels) - 1
        return self.current_channel()

    def next_channel(self):
        self.position = (self.position + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.position = (self.position - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.position]

    def is_exist(self, name):
        return 'Yes' if name in range(len(self.channels)) or name in self.channels else 'No'


if __name__ == '__main__':

    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)
    print('last', controller.last_channel())
    for i in range(5):
        print('next', controller.next_channel())
    print('first', controller.first_channel())
    for i in range(5):
        print('previous', controller.previous_channel())
    print('current', controller.current_channel())
    print(controller.is_exist('BBC'))
    print(controller.is_exist('BBS'))
    print(controller.is_exist(1))
    print(controller.is_exist(15))

