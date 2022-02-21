CREATE DATABASE shop;

CREATE TABLE Uzytkownik (
    Id_uzytkownika INT NOT NULL,
    Imie VARCHAR(50) NOT NULL,
    Nazwisko VARCHAR(50) NOT NULL,
    PRIMARY KEY(Id_uzytkownika)
)


CREATE TABLE Zamowienie (
    Id_zamowienia INT NOT NULL,
    Numer_zamowienia VARCHAR(50) NOT NULL,
    Wartosc_zamowienia INT NOT NULL,
    PRIMARY_KEY(Id_zamowienia)
    Id_uzytkownika INT NOT NULL,
    Id_produktu INT NOT NULL,
    FOREIGN KEY (Id_uzytkownika) references Uzytkownik(Id_uzytkownika),
    FOREIGN KEY (Id_produktu) references Produkt(Id_produktu)
)


CREATE TABLE Produkt (
    Id_produktu INT NOT NULL,
    Nazwa_produktu VARCHAR(30) NOT NULL,
    Cena_produktu INT NOT NULL,
    PRIMARY_KEY(Id_produktu)

)


INSERT INTO Uzytkownik VALUES (1,'Adam', 'Adamowski');
INSERT INTO Uzytkownik VALUES (2, 'Beata', 'Betowska');
INSERT INTO Uzytkownik VALUES (3, 'Jan', 'Pawel');


INSERT INTO Produkt VALUES (1, 'Koszulka', '50');
INSERT INTO Produkt VALUES (2, 'Spodnie', '150');
INSERT INTO Produkt VALUES (3, 'Kremówka', '21');


INSERT INTO Zamowienie VALUES (1, '01/2022', 71, 1, 2);
INSERT INTO Zamowienie VALUES (2, '02/2022', 200, 2, 2);
INSERT INTO Zamowienie VALUES (3, '03/2022', 221, 3, 2);


SELECT * FROM Zamowienie