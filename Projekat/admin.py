# -*- coding: utf-8 -*-
from colorama import Back
import pocetak
import zajednickeFunkcionalnosti as zf
import baza
import matplotlib.pyplot as plt
from numpy import arange

def test():
    print(Back.GREEN + "Ulogovani ste kao administrator")
    print(Back.RESET)
    
def admin_menu(ulogovani):
    global korisnik
    korisnik = ulogovani
    print(Back.BLUE + "\n{}ODABERITE OPCIJU{}".format(">"*5, "<"*5))
    print(Back.RESET)
    print("\n1) Prikaz svih kategorija")
    print("\n2) Prikaz svih korisnika")
    print("\n3) Dodavanje proizvoda")
    print("\n4) Brisanje proizvoda")
    print("\n5) Azuriranje podataka o proizvodu(cena,akcija)")
    print("\n6) Pretraga proizvoda po kategoriji")
    print("\n7) Prikaz narudzbina")
    print("\n8) Prikaz grafika najvise porucivanih proizvoda")
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
        svi_korisnici()
    elif opcija == 3:
        dodavanje_proizvoda()
    elif opcija == 4:
        brisanje_proizvoda()
    elif opcija == 5:
        azuriranje()
    elif opcija == 6:
        zf.pretraga_proizvoda_po_kategoriji()
    elif opcija == 7:
        prikaz_svih_narudzbina()
    elif opcija == 8:
        prikaz_grafika_najvise_porucivanih_proizvoda()
    elif opcija == 9:
        zf.odjava()
    elif opcija == 10:
        pocetak.end()
    else:
        print(Back.RED + "Uneli ste pogresnu opciju. Molimo pokusajte ponovo")
        print(Back.RESET)
        admin_menu(korisnik)
        
def svi_korisnici():
    global korisnik
    korisnik = baza.svi_korisnici()
    print(Back.BLUE + "\nPrikaz svih korisnika: ")
    print(Back.RESET)
    print("RBR  | {0:<15} | {1:<20} | {2:<20} | {3:<2} | ".format("Ime", "Prezime", "Username", "Starost"))
    print("-"*80)
    rbr = 0
    if korisnik:
        for k in korisnik:
            rbr += 1
            print("{4:5}|{0:^17}|{1:^22}|{2:^22}|{3:^9}|".format(k[3], k[4], k[1], k[6],rbr))
            print("-"*80)
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 2
    
    if nazad == 0:
        admin_menu(korisnik)
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        svi_korisnici()


def dodavanje_proizvoda():
    global korisnik
    proizvod = {}
    proizvod['naziv'] = input("Unesite naziv novog proizvoda: ")
    proizvod['cena'] = eval(input("Unesite cenu novog proizvoda: "))
    proizvod['opis'] = input("Unesite opis novog proizvoda: ")
    proizvod['akcija'] = input("Unesite da li je novi proizvod na akciji(1-jeste, 0-nije): ")
    
     
    kategorije = baza.sve_kategorije()
   
    
    print("Kategorije proizvoda: \n")
    for k in kategorije:
        print('{}{} {}'.format('-', k[0], k[1]))
        
    try:
        kategorija_proizvoda = eval(input("Unesite kategoriju kojoj pripada novi proizvod: "))
    except:
        kategorija_proizvoda = 0
    
    try:
        kategorija = kategorije[kategorija_proizvoda - 1]
    except:
        print("Odabrali ste pogresnu opciju. Izaberite jednu od ponudjenih opcija! ")
        dodavanje_proizvoda()
    #print(kategorija)   
    
    try:
        baza.dodavanje_proizvoda(proizvod, kategorija[0])
        print(Back.GREEN + "Uspesno ste dodali proizvod!")
        print(Back.RESET)
    except:
        print(Back.RED + "Nesto nije u redu.Pokusajte ponovo!")
        print(Back.RESET)
        dodavanje_proizvoda()
       
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad
    
    while not nazad == 0:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        nazad = eval(input("Unesite 0 za povratak: "))
        
    admin_menu(korisnik)

    
def prikaz_svih_narudzbina():
    global korisnik
    narudzbine = baza.prikaz_svih_narudzbina()
    print(Back.BLUE + "\nPrikaz svih narudzbina: ")
    print(Back.RESET)
    rbr = 0
    print("RBR  | {0:<10} | {1:<5} | {2:<10} | ".format("Postarina", "Id proizvoda", "Id korisnika"))
    print('-'*50)
    if narudzbine:    
        for n in narudzbine:
            rbr += 1
            print("{3:5}|{0:12}|{1:^15}|{2:^14}|".format(n[2], n[4], n[3],rbr))
            print("-"*50)
        
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 2
    
    if nazad == 0:
        admin_menu(korisnik)
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        prikaz_svih_narudzbina()
    
def azuriranje():
    global korisnik 
    proizvodi = baza.svi_proizvodi()
    
    print(Back.BLUE + "Proizvodi: \n")
    print(Back.RESET)
    
    print("{0:<5} | {1:<10} | {2:<10} | {3:<10}".format("Id", "Naziv", "Cena", "Akcija"))
    
    for p in proizvodi:
        print('='*50)
        print('{:^6}| {:<10} | {:<10} | {:^10}'.format(p[0], p[1], p[2], p[4]))
        
    print("\nOdaberite opciju za azuriranje: ")
    print("\n1) azuriranje cene ")
    print("\n2) azuriranje akcije ")
    
    try:
        opc = eval(input("Unesite zeljenu opciju: "))
    except:
        opc = 3
    
    if opc == 1:
        id_proizvod = eval(input("Unesite id proizvoda koji zelite da azurirate: "))
        cena = eval(input("Unesite novu cenu proizvoda: "))
        baza.azuriraj_cenu(id_proizvod, cena)
        print(Back.GREEN + "Uspesno azuriranje")
        print(Back.RESET)
    elif opc == 2:
        id_proizvod = eval(input("Unesite id proizvoda koji zelite da azurirate: "))
        akcija = eval(input("Promenite trenutno stanje akcije(1-jeste, 0-nije!): "))
        baza.azuriraj_akciju(id_proizvod,akcija)
        print(Back.GREEN + "Uspesno azuriranje")
        print(Back.RESET)
    else:
        print(Back.RED  + "Uneli ste pogresnu opciju! Pokusajte ponovo")
        print(Back.RESET)
        azuriranje()
       
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 2
    
    if nazad == 0:
        admin_menu(korisnik)
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        azuriranje()


def brisanje_proizvoda():
    global korisnik 
    proizvodi = baza.svi_proizvodi()
    
    print(Back.BLUE + "Proizvodi: \n")
    print(Back.RESET)
    
    print("{0:<5} | {1:<10} | {2:<10} | {3:<10}".format("Id", "Naziv", "Cena", "Akcija"))
    
    for p in proizvodi:
     print('='*50)
     print('{:^6}| {:<10} | {:<10} | {:^10}'.format(p[0], p[1], p[2], p[4]))
        
    try:
       id_proizvoda = eval(input("Unesite id proizvoda koji zelite da izbrisete: "))
    except:
       id_proizvoda = 0 
        
        
    try:
       if baza.nadji_proizvod(id_proizvoda) != None:
          baza.brisanje_proizvod(id_proizvoda)
          print(Back.GREEN + "Uspesno brisanje proizvoda! ")
          print(Back.RESET)
       else:
           print(Back.RED + "Nesto nije u redu! ")
           print(Back.RESET)
           brisanje_proizvoda()
    except:
       print(Back.RED + "Nesto nije u redu! ")
       print(Back.RESET)
       brisanje_proizvoda()
    try:
       nazad = eval(input("Unesite 0 za povratak: "))
    except:
       nazad = 1
    
    while not nazad == 0:
      print(Back.RED + "Pogresno ste uneli opciju")
      print(Back.RESET)
      nazad = eval(input("Unesite 0 za povratak: "))
        
    admin_menu(korisnik)

def prikaz_grafika_najvise_porucivanih_proizvoda():
    global korisnik   
    recnik = baza.najvise_porucivani_proizvod()
    sortirani_recnik = dict()
    sortirani = sorted(recnik, key=recnik.get, reverse = True)
    
    sortirani = sortirani[:3]
    
    for p in sortirani:
        sortirani_recnik[p] = recnik[p]

    naziv_proizvoda = []
    for p in sortirani_recnik:
        tmp = baza.nadji_proizvod(p)
        naziv_proizvoda.append(tmp[1])
        
    x = list(naziv_proizvoda)
    y = list(sortirani_recnik.values())
    
    plt.bar(x, y)
    plt.xlabel("Nazivi proizvoda")
    plt.ylabel("Proizvodi koju su porucivani najveci broj puta")
    plt.yticks(arange(0, max(y)+1, 1.0))
    
    plt.pause(10)
    
    admin_menu(korisnik)
     
   