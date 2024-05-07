class movie():
    def __init__(self, title, director, year, genre, stok):
        self.title=title
        self.director=director
        self.year=year
        self.genre=genre
        self.stok= stok

    def stokda (self):
        if self.stok > 0:
            return f"{self.title} filmini izləyə bilərsiniz. "
        else:
            return f" {self.title} filmini tarixi bitib."
        
        
inc=movie("Inception", "Christopher Nolan", 2010, "Science Fiction", 10)
the=movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 5)
dark=movie("The Dark Knight", "Christopher Nolan", 2008, "Action", 0)
pulp=movie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime", 1)


print(f"{inc.title}  adlı filmin qurucusu - {inc.director} və film {inc.year} ildə çəkilib. { inc.stokda()}")    
print(f"{the.title} adlı filmin qurucusu - {the.director} və film {the.year} ildə çəkilib. { the.stokda()}")
print(f"{dark.title} adlı filmin qurucusu - {dark.director} və film{dark.year} ildə çəkilib.{ dark.stokda()}")
print(f"{pulp.title} adlı filmin qurucusu - {pulp.director} və film {pulp.year} ildə çəkilib. {pulp.stokda()}")