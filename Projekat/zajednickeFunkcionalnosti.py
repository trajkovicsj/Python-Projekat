# -*- coding: utf-8 -*-
import baza as baza
import korisnik as kor
from colorama import Back
import pocetak
import admin

def sve_kategorije():
    global korisnik
    print(Back.BLUE + "\nPrikaz svih kategorija: ")
    print(Back.RESET)
    print("RBR  | {0:^15}".format("Naziv"))
    print("-"*25)
    rbr = 0
    kategorije = baza.sve_kategorije()
    for k in kategorije:
        rbr += 1
        print("{0:^5}|{1:^20} ".format(rbr, k[1]))
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 1
        
    if nazad == 0:
        if korisnik[7] == 1:
            admin.admin_menu(korisnik)
            return
        else:
            kor.korisnik_menu(korisnik)
            return
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        sve_kategorije()

def pretraga_proizvoda_po_kategoriji():
    global korisnik
    print(Back.BLUE + "\nPrikaz svih kategorija: ")
    print(Back.RESET)
    print("RBR  | {0:^15}".format("Naziv"))
    print("-"*25)
    rbr = 0
    kategorije = baza.sve_kategorije()
    for k in kategorije:
        rbr += 1
        print("{0:^5}|{1:^20} ".format(rbr, k[1]))
    kategorije = input("Unesite naziv kategorije za koju zelite da prikazete proizvode: ")
    kat = baza.nadji_kategoriju(kategorije)
    
    if kat:
        proizvodi = baza.nadji_proizvod_po_kategoriji(kat[0][0])
        if proizvodi:
            print(Back.BLUE + "Proizvodi: \n")
            print(Back.RESET)
    
            print("{0:<5} | {1:<10} | {2:<10} | {3:<48}".format("Id", "Naziv", "Cena", "Opis"))
    
            for p in proizvodi:
                print('='*85)
                print('{:^6}| {:<10} | {:<10} | {:^48}'.format(p[0], p[1], p[2], p[3]))
        else:
            print(Back.RED + "Ne postoji takav proizvod")
            print(Back.RESET)
            pretraga_proizvoda_po_kategoriji()
            
    else:
        print(Back.RED + "Nemamo tu kategoriju probajte ponovo!")
        print(Back.RESET)
        pretraga_proizvoda_po_kategoriji()
    
    try:
        nazad = eval(input("Unesite 0 za povratak: "))
    except:
        nazad = 1
        
    if nazad == 0:
        if korisnik[7] == 1:
            admin.admin_menu(korisnik)
            return
        else:
            kor.korisnik_menu(korisnik)
            return
    else:
        print(Back.RED + "Pogresno ste uneli opciju")
        print(Back.RESET)
        pretraga_proizvoda_po_kategoriji()
    
    
def odjava():
    pocetak.start()

def inicijalizacija_korisnika(kor):
    global korisnik
    korisnik = kor
    
        
        