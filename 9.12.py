'''i = 0
while i < 5:
    print("Warunek spełniony")
    i+=1

try:
    x = input("Wprowadź liczbę całkowitą: ")
    x_num = int(x)
    print(f'Liczba Całkowita: {x_num}')
    # Pobierze od urzytkownika tylko liczby całkowite, inaczej zwróci
except ValueError:
    print('Wprowadzona wartość nie jest liczbą całkowitą!')
    print('Program zostanie wyłączony!')
    exit(-1)'''

#zad1
class Czlowiek:
    def __init__(self,imie,nazwisko,wiek,plec,wzrost,waga):
        self.imie=imie
        self.nazwisko=nazwisko
        self.wiek=wiek
        self.plec=plec
        self.wzrost=wzrost
        self.waga=waga
        self.okupacja=None

    def obudzSie(self):
        print(f"{self.imie} {self.nazwisko} budzi się")
    def zjedz(self,coJe):
        return f"{self.imie} {self.nazwisko} je {coJe}"
    def idzDo(self,miejsce):
        return f"{self.imie} {self.nazwisko} idz do {miejsce}"
    def spij(self):
        print(f"{self.imie} {self.nazwisko} idzie spać")
    def __str__(self):
        return f"[{self.plec}] {self.imie} {self.nazwisko} ({self.wiek}): waga: {self.waga}, wzrost: {self.wzrost}, okupacja: {self.okupacja}"

ziomek=Czlowiek('Ewa','Zielinska','20','Kobieta','165','60')
ziomek.obudzSie()
print(ziomek.zjedz('zupę'))
ziomek.idzDo('domu')
ziomek.spij()

# ctrl+znakZapytania
# robi hashtagi
# do calego zaznaczonego fragmentu


#zad2
class Student(Czlowiek):
    def __init__(self,imie,nazwisko,wiek,plec,wzrost,waga):
        super().__init__(imie,nazwisko,wiek,plec,wzrost,waga)
        self.okupacja='Student'
    def studiuje(self, kierunek):
        return f"{self.okupacja} {self.imie} {self.nazwisko} studiuje {kierunek}"
    def pije(self, napoj):
        print(f"{self.okupacja} {self.imie} {self.nazwisko} siedzi na lawce i pije {napoj}")

class Wykladowca(Czlowiek):
    def __init__(self,imie,nazwisko,wiek,plec,wzrost,waga):
        super().__init__(imie,nazwisko,wiek,plec,wzrost,waga)
        self.okupacja='Wykladowca'
    def wyklada(self, przedmiot):
        return f"{self.okupacja} {self.imie} {self.nazwisko} wyklada {przedmiot}"
    def pije(self, napoj):
        print(f"{self.okupacja} {self.imie} {self.nazwisko} siedzi sam na lawce i pije {napoj}")
    def egzamin(self):
        print(f'{self.okupacja} {self.imie} {self.nazwisko} przeprowadza egzamin')

if __name__=='__main__':
    student=Student('Kuba','Król',20,'mężczyzna','180',60)
    doktor=Wykladowca('Marek','Kosa',69,'mezczyzna',200,100)
    from time import sleep
    doktor.obudzSie()
    print(doktor.zjedz('śniadanie: chleb ze smalcem'))
    print(doktor.idzDo("kołchoz"))
    sleep(5) #na 5 sekund zatrzymuje sie program
    student.obudzSie()
    print(student.zjedz('monsterek'))
    print(student.idzDo('Uniwerek'))
    sleep(5)
    doktor.egzamin()
    student.pije('piwo')
#ta czesc printujemy z terminalu przy pomocy funkcji py



