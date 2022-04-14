# -*- coding: utf-8 -*-
import zajednickeFunkcionalnosti as zf
import pocetak
from colorama import Back 
import baza


def test1():
    print(Back.GREEN + "Ulogovani ste kao korisnik")
    print(Back.RESET)
    
def korisnik_menu(ulogovani):
    global korisnik
    korisnik = ulogovani
    print(Back.BLUE + "\n{}ODABERITE OPCIJU{}".format(">"*5, "<"*5))
    print(Back.RESET)
    print("\n1) Prikaz svih kategorija")
    print("\n2) Pretraga proizvoda po kategoriji")
    print("\n3) Prikaz proizvoda sortiranih po ceni")
    print("\n4) Prikaz proizvoda na akciji")
    print("\n5) Narucivanje proizvoda")
    print("\n6) Prikaz narucenih proizvoda")
    print("\n7) Dodavanje komentara")
    print("\n8) Prikaz proizvoda u nekom opsegu cena")
    print("\n9) Odjava")
    print("\n10) Zavrsi sa radom")
    izbor_opcije()

def izbor_opcije():
    global korisnik
    try:
        opcija = eval(input("Unesite zeljenu opciju: "))
    except:
        opcija = 11
    
    if opcija == 1:
        zf.sve_kategorije()
    elif opcija == 2:
        zf.pretraga_proizvoda_po_kategoriji()
    elif opcija == 3:
        proizvodi_sortirani_po_ceni()
    elif opcija == 4:
        prikaz_proizvoda_na_akciji()
    elif opcija == 5:
        narucivanje_proizvoda()
    elif opcija == 6:
        prikaz_narudzbina()
    elif opcija == 7:
        dodavanje_komentara()
    elif opcija == 8:
        prikaz_proizvoda_u_opsegu_cena()
    elif opcija == 9:
        zf.odjava()
    elif opcija == 10:
        pocetak.end()
    else:
        print(Back.RED + "Uneli ste pogresnu opciju. Molimo pokusajte ponovo")
        print(Back.RESET)
        korisnik_menu(korisnik)

def proizvodi_sortirani_po_ceni():
      global korisnik
      print(Back.BLUE + "Prikaz proizvoda sortiranih po ceni: ")
      print(Back.RESET)
      print("RBR  | {0:<10} | {1:<10} | {2:<48} | {3:<5} | ".format("Naziv", "Cena", "Opis", "Akcija"))
      print("-"*92)
      rbr = 0
      proizvodi = baza.svi_proizvodi()
      proizvodi.sort(key = lambda x: x[2])
      if proizvodi:
          for p in proizvodi:
               rbr += 1
               print("{4:5}|{0:^12}|{1:^12}|{2:^50}|{3:^8}|".format(p[1], p[2], p[3], p[4],rbr))
               print("-"*92)
      try:
        nazad = eval(input("Unesite 0 za povratak: "))
      except:
        nazad = 2
    
      if nazad == 0:
        korisnik_menu(korisnik)
      else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        proizvodi_sortirani_po_ceni()
        
def prikaz_proizvoda_na_akciji():
    global korisnik
    print(Back.BLUE + "Prikaz proizvodana akciji: ")
    print(Back.RESET)
    print("RBR  | {0:<9} | {1:<10}".format("Naziv", "Cena"))
    print('-'*30)
    rbr = 0
    proizvodi = baza.svi_proizvodi()
    for p in proizvodi:
        if(p[4] == 1):
            rbr += 1
            print("{0:5}|{1:^11}|{2:^12}".format(rbr, p[1], p[2]))
            print("-"*30)
    
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 2
    
    if nazad == 0:
        korisnik_menu(korisnik)
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        prikaz_proizvoda_na_akciji()
        
def narucivanje_proizvoda():
    global korisnik
    proizvodi = baza.svi_proizvodi()
    
    print(Back.BLUE + "Proizvodi: \n")
    print(Back.RESET)
    
    print("{0:<5} | {1:<10} | {2:<10} | {3:<48}".format("Id", "Naziv", "Cena", "Opis"))
    
    for p in proizvodi:
        print('='*85)
        print('{:^6}| {:<10} | {:<10} | {:^48}'.format(p[0], p[1], p[2], p[3]))
        
    try:
        id_proizvoda = eval(input("Unesite id proizvoda koji zelite da porucite: "))
    except:
        id_proizvoda = 0

    
    try:
        baza.narucivanje_proizvoda(id_proizvoda,korisnik[0], postarina = 300)
        print(Back.GREEN + "Uspesno ste porucili proizvod!")
        print(Back.RESET)
    except:
        print(Back.RED + "Nesto nije u redu.Pokusajte ponovo!")
        print(Back.RESET)
        narucivanje_proizvoda()
    
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad
    
    while not nazad == 0:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        nazad = eval(input("Unesite 0 za povratak: "))
        
    korisnik_menu(korisnik)
    
def prikaz_narudzbina():
    global korisnik
    narucene = baza.narucene(korisnik[0])
    if narucene:
        suma_proizvoda = 0
        rbr = 0
        print("\nVasa narudzbina: ")
        for p in narucene:
            proizvod = baza.nadji_proizvod(p[4])
            if proizvod:
                rbr+=1
                print("{:^8}|{:<15}|{}".format(rbr,proizvod[1], proizvod[2]))
                print('-'*40)
                suma_proizvoda += proizvod[2]
        print("{}{}".format("Ukupan iznos svih narucenih proizvoda: ", suma_proizvoda))
    
    else:
        print(Back.RED + "Niste nista narucili!")
        print(Back.RESET)        
  
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 2
    
    if nazad == 0:
        korisnik_menu(korisnik)
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        prikaz_narudzbina()    
            
def dodavanje_komentara():
    global korisnik
    proizvodi = baza.svi_proizvodi()
    
    print(Back.BLUE + "Proizvodi: \n")
    print(Back.RESET)
    
    print("{0:<5} | {1:<10} | {2:<10} | {3:<48}".format("Id", "Naziv", "Cena", "Opis"))
    
    for p in proizvodi:
        print('='*85)
        print('{:^6}| {:<10} | {:<10} | {:^48}'.format(p[0], p[1], p[2], p[3]))
        
    try:
        id_proizvoda = eval(input("Unesite id proizvoda za koji zelite da dodate komentar: "))
    except:
        id_proizvoda = 0
    
    
    tekst = input("Unesite komentar: ")
    try:
        baza.dodavanje_komentara(korisnik[0], id_proizvoda, tekst)
        print(Back.GREEN + "Uspesno ste uneli komentar!")
        print(Back.RESET)
    except:
        print(Back.RED + "Nesto nije u redu.Pokusajte ponovo!")
        print(Back.RESET)
        dodavanje_komentara()
    
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad
    
    while not nazad == 0:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        nazad = eval(input("Unesite 0 za povratak: "))
        
    korisnik_menu(korisnik)


def prikaz_proizvoda_u_opsegu_cena():
      minCena = eval(input("Unesite minimalnu cenu proizvoda: "))
      maxCena = eval(input("Unesite maksimalnu cenu proizvoda: "))
      print(Back.BLUE + "\nPrikaz proizvoda u opsegu cena: ")
      print(Back.RESET)
      print("RBR  | {0:<10} | {1:<10} | {2:<48} | {3:<5} | ".format("Naziv", "Cena", "Opis", "Akcija"))
      print("-"*92)
      rbr = 0
      proizvodi = baza.svi_proizvodi()
      proizvodi = (filter(lambda x: x[2]>=minCena and x[2]<=maxCena, proizvodi))
      if proizvodi:
          for p in proizvodi:
               rbr += 1
               print("{4:5}|{0:^12}|{1:^12}|{2:^50}|{3:^8}|".format(p[1], p[2], p[3], p[4],rbr))
               print("-"*92)
      try:
        nazad = eval(input("Unesite 0 za povratak: "))
      except:
        nazad = 2
    
      if nazad == 0:
        korisnik_menu(korisnik)
      else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        prikaz_proizvoda_u_opsegu_cena()