# -*- coding: utf-8 -*-

import mysql.connector
import datetime

db = mysql.connector.connect(host='localhost',user='root', password='Sandra99.', database='mydb')
kursor = db.cursor()

def sve_uloge():
    kursor.execute('select * from Uloga')
    return kursor.fetchall()


def pronadji_ulogu(username, password):
    vrednosti = (username, password)
    kursor.execute("select * from Korisnik where username like %s and password like %s", vrednosti)
    korisnik = kursor.fetchall()
    if korisnik:
        return korisnik[0]
    return 0

def pronadji_username(username):
    vrednosti = (username, )
    kursor.execute("select * from Korisnik where username like %s", vrednosti)
    korisnik = kursor.fetchall()
    if korisnik:
        return True
    return False 

def registracija(username, password, ime, prezime, adresa, starost):
    vrednosti = (username, password, ime, prezime, adresa, starost, 2)
    kursor.execute("insert into Korisnik (username, password, ime, prezime, adresa, starost, Uloga_idUloga) \
                     values (%s, %s, %s, %s, %s, %s, %s)", vrednosti)
    db.commit()
    
def sve_kategorije():
    kursor.execute('select * from Kategorija')
    return kursor.fetchall()

def svi_korisnici():
    kursor.execute('select * from Korisnik where Uloga_idUloga not like 1')
    return kursor.fetchall()

def svi_proizvodi():
    kursor.execute('select * from Proizvod')
    return kursor.fetchall()

def dodavanje_proizvoda(proizvod, kategorija):
    vrednosti = (proizvod['naziv'], proizvod['cena'], proizvod['opis'], proizvod['akcija'], kategorija)
    kursor.execute('insert into Proizvod (naziv, cena, opis, akcija, Kategorija_idKategorija) values(%s, %s, %s, %s, %s)', vrednosti)
    db.commit()
   
def narucivanje_proizvoda(proizvod, korisnik, postarina = 300):
    vrednosti = (datetime.datetime.now(), postarina, korisnik, proizvod)
    kursor.execute('insert into Narudzbina (datum, postarina, Korisnik_idKorisnik, Proizvod_idProizvod) values (%s, %s, %s, %s)', vrednosti)
    db.commit()    

def narucene(idKorisnika):
    vrednost = (idKorisnika,)
    kursor.execute('select * from Narudzbina where Korisnik_idKorisnik like %s', vrednost)
    return kursor.fetchall()

def nadji_proizvod(idProizvod):
    vrednost = (idProizvod, )
    kursor.execute('select * from Proizvod where idProizvod like %s', vrednost)
    proizvod = kursor.fetchall()
    if proizvod:
        return proizvod[0]
    return None
    
def prikaz_svih_narudzbina():
    kursor.execute("select * from Narudzbina")
    return kursor.fetchall()

def dodavanje_komentara(korisnik,proizvod, tekst):
    vrednosti = (datetime.datetime.now(), tekst, korisnik, proizvod)
    kursor.execute('insert into Komentar(datum, tekst, Korisnik_idKorisnik, Proizvod_idProizvod) values (%s, %s, %s, %s)', vrednosti)
    db.commit()

def azuriraj_cenu(idProizvod, cena):
    vrednost = (cena, idProizvod)
    kursor.execute('update Proizvod set cena = %s where idProizvod = %s', vrednost)
    db.commit()

def azuriraj_akciju(idProizvod, akcija):
    vrednost = (akcija, idProizvod)
    kursor.execute('update Proizvod set akcija = %s where idProizvod = %s', vrednost)
    db.commit()

def nadji_kategoriju(naziv):
    vrednosti = (naziv, )
    kursor.execute('select * from Kategorija where naziv like %s', vrednosti)
    return kursor.fetchall()

def nadji_proizvod_po_kategoriji(idKategorija):
    vrednosti = (idKategorija, )
    kursor.execute('select * from Proizvod where Kategorija_idKategorija like %s',vrednosti)
    return kursor.fetchall()
 
def brisanje_proizvod(idProizvod):
    vrednosti = (idProizvod, )
    kursor.execute('select * from Komentar where Proizvod_idProizvod like %s ', vrednosti)
    komentari = kursor.fetchall()
    if komentari:
        kursor.execute('delete from Komentar where Proizvod_idProizvod like %s', vrednosti)
        db.commit()  
    kursor.execute('select * from Narudzbina where Proizvod_idProizvod like %s', vrednosti)
    narudzbine = kursor.fetchall()
    if narudzbine:
        kursor.execute('delete from Narudzbina where Proizvod_idProizvod like %s', vrednosti)
        db.commit()
    kursor.execute('delete from Proizvod where idProizvod like %s', vrednosti)
    db.commit()
    return True

def najvise_porucivani_proizvod():
    try:
        kursor.execute('select distinct Proizvod_idProizvod from Narudzbina')
        proizvod = kursor.fetchall()
    except:
        print("Greska prilikom trazenja proizvoda! ")
    recnik = dict()
    if proizvod:
        for p in proizvod:
            try:
                kursor.execute('select count(Proizvod_idProizvod) from Narudzbina where Proizvod_idProizvod like %s', p)
                recnik[p[0]] = kursor.fetchall()[0][0]
                # print(recnik[p[0]])
            except:
                 print("Greska prilikom trazenja proizvoda! ") 
    return recnik