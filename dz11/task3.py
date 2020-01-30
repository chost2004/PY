'''
Реализовать класс, описывающий новостную ленту. 
Класс должен содержать: 
- массив новостей; 
- get-свойство, которое возвращает количество новостей; 
- метод для вывода на экран всех новостей; 
- метод для добавления новости; 
- метод для удаления новости; 
- метод для сортировки новостей по дате (от последних новостей до старых); 
- метод для поиска новостей по тегу (возвращает массив новостей, в которых указан переданный в метод тег). 

Продемонстрировать работу написанных методов.
'''
from datetime import *
class News:
    def __init__(self, news):
        self.news = news

    @property
    def len(self):
        return len(self.news)
    def print(self):
        for n in self.news: print(n[1])
    def add(self,new_news):
        self.news.append(new_news)
    def remove(self,n):
        del self.news[n]
    def search(self, text):
        for n in self.news:
            if text in n:
                print(n[1])
    def sorted(self):
        self.news = sorted(self.news, reverse=True, key = lambda d : datetime.strptime(d[0], '%d.%m.%Y'))

news1 = ['20.11.2019', 'Адвокат Трампа вызвал скандал своим аргументом против импичмента', 'Трамп']
news2 = ['25.11.2019', 'Большинство шотландцев поддержали независимость - опрос YouGov', 'Шотландия']
news3 = ['18.10.2019', 'Видео из Австралии показывает скорость распространения пожаров', 'Пожар']
news4 = ['30.01.2020', 'Миллиардер передумал: никто из 28 000 девушек не полетит к Луне', 'Луна']
news5 = ['18.01.2020', 'Ученые обнаружили неожиданно большой источник парниковых газов', 'Ученые']
news = [news1, news2, news3, news4]

obj = News(news)
obj.print()
print('-' * 50)
obj.add(news5)
obj.print()
print('-' * 50)
obj.remove(1)
obj.print()
print('-' * 50)
obj.search('Луна')
print('-' * 50)
obj.sorted()
obj.print()
print('-' * 50)
