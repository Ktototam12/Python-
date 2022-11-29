class Artist:
    def __init__(self, name : str, surname : str):
        ''' Инициализурет объект художник '''
        self.name = name 
        self.surname = surname
        
    def __str__(self):
        return 'Artist ' + str(self())
    
    def __call__(self):
        return 'Name ' + self.name
    
class Painting(Artist):
    def __init__(self, name : str, artist : str, year : int):
        ''' Инициализурет объект painting '''
        super().__init__(name, 'Title ') 
        self.year = year
    
    def __call__(self):
        return self.year
    
    def __repr__(self) -> str:
        return f'Painting (title = "{self.name}", artist = {artist}, year = {self.year})'

class Exhibition(Artist):
    def __init__(self, name : str, place : str):
        super().__init__(name, 'Perm')
    
artist = Artist('Salvador', 'Dali')
artist()

exhibition = Exhibition('Dali 2022', 'London')
print(exhibition)
exhibition()

exhibition = Exhibition('Stars', 'Milan')
print(exhibition)

painting = Painting('Пейзаж близ Фигераса', 'dali', 1911)
print(painting)

str(painting)

painting.__str__()

painting.__repr__()
  
newPainting = Painting(name = "Time", artist = 'Ван Гог', year= 1918)
print(newPainting.name)
print(newPainting)       
