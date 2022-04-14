# -*- coding: utf-8 -*-
from colorama import Back
import baza as baza
import admin as admin
import korisnik as kor
import zajednickeFunkcionalnosti as zf

def start():
    print("\n{}PRODAJA NAMESTAJA SIPOR DOO VRANJE{}\n".format("*"*5, "*"*5))
    print("{}".format("Kratak opis kompanije \n"))
    print("-"*80)
    print("Sipor je jedna od prvoosnovanih Simpovih"
          + " porodičnih fabrika. Radi uspešno od 7. septembra 1993."
          + "godine. Sipor posluje po kriterijumima kompanije Simpo."
          + "Sipor raspolaže opremom i mobilnim ekipama za rad na terenu (na licu mesta)")
    print("-"*80 + "\n"*3)
    
    '''uloge = baza.sve_uloge()
    for u in uloge:
        print("{}".format(u[1]))'''
   
    odabir_opcije()
    

def odabir_opcije():

    print("{}START{}\n".format("-"*20, "-"*20))
    print("1) Uloguj se \n2) Registruj se \n3) Zavrsi sa radom\n")
    try: 
        opcija = eval(input("Odaberite jednu od ponudjenih opcija: "))
    except:
        opcija = 4
    
    if opcija == 1:
        login()
    elif opcija == 2:
        register()
    elif opcija == 3:
        end()
    else:
        print("\n" + Back.RED + "UNETA OPCIJA JE POGRESNA, MOLIMO VAS UNESITE ISPRAVNU OPCIJU!\n")
        print(Back.RESET)
        odabir_opcije()
  
def register():
    username = input("Unesite korisnicko ime: ")
    while baza.pronadji_username(username):
        print( Back.RED + "Postoji korisnik sa tim username-om molimo Vas pokusajte ponovo")
        print(Back.RESET)
        username = input("Unesite korisnicko ime: ")
    
    
    password = input("Unesite lozinku: ")
    while not password[0].isupper() or not sadrzi_broj(password):
        print(Back.RED + "Prvo slovo lozinke mora biti velikim slovom. Lozinka mora da sadrzi i broj! \n")
        print(Back.RESET)
        password = input("Unesite lozinku: ")
    
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    adresa = input("Unesite adresu: ")
    starost = eval(input("Unesite Vase godine: "))
    baza.registracija(username, password, ime, prezime, adresa, starost)
    print(Back.GREEN + "Uspesno ste se registrovali. Dobrodosli!")
    print(Back.RESET)
    odabir_opcije()

def sadrzi_broj(password):
        for c in password:
            if c.isdigit():
                return True
        return False
    
def login():
    global ulogovani
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    ulogovani = baza.pronadji_ulogu(username, password)
    
    #print(ulogovani)
    if ulogovani:
        uloga = ulogovani[7]
        if uloga == 1:
            admin.test()
            zf.inicijalizacija_korisnika(ulogovani)
            admin.admin_menu(ulogovani)
        elif uloga == 2:
            kor.test1()
            zf.inicijalizacija_korisnika(ulogovani)
            kor.korisnik_menu(ulogovani)
    else:
        print(Back.RED + "Ne postoji korisnik sa tim username-om i password-om!")
        print(Back.RESET)
        odabir_opcije()
        
def end():
    print(Back.MAGENTA + "Program je zavrsio sa radom. Dovidjenja")
    print(Back.RESET)
    
    
