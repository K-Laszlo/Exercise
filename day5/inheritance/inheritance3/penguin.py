from day5.inheritance.inheritance3.bird import Bird


class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print('Penguin ready')

    def who_is_this(self):
        print('penguin')

    def run(self):
        print('run faster!')
