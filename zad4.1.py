# zad1: Napisz program wyświetlający tylko liczby podzielne przez 3 i niepodzielne przez 5, z zakresu od 0 do 150, z wykorzystaniem pętli for. Jeśli liczba jest parzysta, niech obok liczby wyświetli sie informacja "parzysta". Jeśli liczba jest nieparzysta, niech obok liczby wyświetli sie informacja "nieparzysta".
# for i in range(0,151):
#     if i %3 == 0 and i %5 != 0:
#         print(i)
#         if i %2 ==0:
#             print("parzysta")
#         elif i %2 !=0:
#             print("nieparzysta")
        
#Zad 3Napisz program wyświetlający 4 wiersz tabliczki mnożenia (4,8,...,40) za pomoca pętli (dowolnej). Użyj mnożenia i pętli do wyznaczenia kolejnych elementów.
# print("Czwarty wiersz tabliczki mnożenia")
# cyfra = 1
# while cyfra != 11:
#     print(cyfra*4)
#     cyfra +=1

# zad 2: Napisz program, który pobierze od użytkownika liczbę i wypisze jej wszystkie dzielniki (czyli liczby, przez które dzieli się bez reszty).

while True:
    print("Podaj liczbę")
    liczba = int(input())
    if liczba %1==0:
        print("Ta liczba jest podzielna przez 1")
    if liczba %2==0:
        print("Ta liczba jest podzielna przez 2")
    if liczba %3==0:
        print("Ta liczba jest podzielna przez 3")
    if liczba %4==0:
        print("Ta liczba jest podzielna przez 4")
    if liczba %5==0:
        print("Ta liczba jest podzielna przez 5")
    if liczba %6==0:
        print("Ta liczba jest podzielna przez 6")
    if liczba %7==0:
        print("Ta liczba jest podzielna przez 7")
    if liczba %8==0:
        print("Ta liczba jest podzielna przez 8")
    if liczba %9==0:
        print("Ta liczba jest podzielna przez 9")

#Zad 4
# while True:
#     print("Aby wyświetlić informacje o autorze wciśnij \"i\"")
#     print("Aby wyświetlić wykonane zadania wciśnij \"t\"")
#     print("Aby zakoczyć program wciśnij \"q\"")
#     znak = input()
#     if znak == "i":
#         print("Bianka Kaczmarek\nstudentka kognitywistyki\npierwszy rok")
#     elif znak == "t":
#         print("Zostały wykonane zadania\n1\n2\n3\nAby zobaczyć wciśnij odpowiednią cyfrę")
#         cyfra = int(input())
#         if cyfra == 1:
#             print("Napisz program wyświetlający tylko liczby podzielne przez 3 i niepodzielne przez 5, z zakresu od 0 do 150, z wykorzystaniem pętli for. Jeśli liczba jest parzysta, niech obok liczby wyświetli sie informacja ""parzysta"". Jeśli liczba jest nieparzysta, niech obok liczby wyświetli sie informacja ""nieparzysta"".")
#         elif cyfra == 2:
#             print("Napisz program, który pobierze od użytkownika liczbę i wypisze jej wszystkie dzielniki (czyli liczby, przez które dzieli się bez reszty).")
#         elif cyfra ==3:
#             print("Napisz program wyświetlający 4 wiersz tabliczki mnożenia (4,8,...,40) za pomoca pętli (dowolnej). Użyj mnożenia i pętli do wyznaczenia kolejnych elementów.")
#     elif znak == "q":
#         break
#Zmiana
#Zmiana2



    


