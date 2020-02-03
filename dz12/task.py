from datetime import datetime


class News:
    '''Хранит новость и методы работы с ней'''
    def __init__(self, date_of_publish, heading, text, tegs):
        self.heading = heading
        self.date = date_of_publish
        self.text = text
        self.tegs = ' #'.join(('#'+tegs).split())
        self.today = datetime.today()
        self.date_of_news = datetime.strptime(date_of_publish, "%d.%m.%Y")

    def __str__(self):
        return f"{self.date} {self.heading}"

    @property
    def delta(self):
        '''Показывает количество дней между датами новости и сегодняшней'''
        return self.today - self.date_of_news
    
    def search(self, text):
        '''Ищет текст в новости'''
        if text in self.text:
            return True
    
    def print(self):
        '''Печатает новость'''
        print('_' * 100)
        print("{:-^100s}".format(self.heading))
        if self.delta.days == 0:
            self.print_day = 'Today'
        elif self.delta.days <= 7:
            self.print_day = str(self.delta.days) + ' days ago'
        else:
            self.print_day = self.date
        print("{:^100s}".format(self.print_day))
        print('_' * 100)
        print(self.text)
        print()
        print(self.tegs)
        print('_' * 100,'\n\n')


class NewsArray:
    ''''Инициализирует новости и позволяет работать с масивом новостей'''
    def __init__(self, file):
        self.file = file
        self.array = []
        with open(self.file, 'r') as text_file:
            for line in text_file:
                self.array.append(News(*line.strip().split('|')))
                
    @property
    def len(self):
        ''' Количество новостей'''
        return len(self.array)
    
    def print(self):
        '''Печатает дату и заголовок всех новостей'''
        for n in self.array:
            print(n)
            
    def print_full(self):
        '''Печатает полные новости'''
        for n in self.array:
            n.print()
            
    def add(self,new_news):
        '''Добавляет новость'''
        self.array.append(News(*new_news.strip().split('|')))
        
    def remove(self,n):
        '''Удаляет новость'''
        del self.array[n]
        
    def search(self, text):
        '''Ищет текст в новостях и печатает новость в случае успеха'''
        for n in self.array:
            if n.search(text):
                n.print()
            
    def sorted(self):
        '''Сортирует новости'''
        self.array = sorted(self.array, reverse=True, key = lambda d : d.date_of_news)

        
news_array = NewsArray('News.txt')
news_array.print()
#news_array.print_full()
news_array.search('Трамп')
print()
news_array.remove(3)
news_array.sorted()
news_array.print()
print(news_array.len)

