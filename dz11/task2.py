'''
_________________________
------ LOREM IPSUM ------
2 days ago
_________________________
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#news #article #important #hello
'''
from datetime import *
class News:
    def __init__(self, heading, date_of_publish, text, tegs):
        self.heading = heading
        self.date = date_of_publish
        self.text = text
        self.tegs = tegs
        self.today = datetime.today()
        self.then = datetime.strptime(date_of_publish, "%d.%m.%Y")

    @property
    def delta(self):
        return self.today - self.then
    
    def print(self):
        print('_' * 50)
        print("{:-^50s}".format(self.heading))
        if self.delta.days == 0:
            self.print_day = 'Today'
        elif self.delta.days <= 7:
            self.print_day = str(self.delta.days) + ' days ago'
        else:
            self.print_day = self.date
        print("{:^50s}".format(self.print_day))
        print('_' * 50)
        print(self.text)
        print()
        print(self.tegs)


heading = 'LOREM IPSUM'
date_of_publish = '30.01.2020'
text = '    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
tegs = '#news #article #important #hello'
news1 = News(heading, date_of_publish, text, tegs)
news1.print()

