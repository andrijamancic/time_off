# time_off
ITBC Final project
Aplikacija za zakazivanje odmora

Aplikacija koja bi omogućila pracenje odsustva zaposlenima u firmama. 
Radinici imaju mogucnost da posalju zahtev za odobrenje koriscenja godisnjeg odmora ili neplacenog odustva.
Takodje postoji mogucnost evidencije bolovanja. Zahtev za odsustvo odobrava nadredjeni. Takodje postoji kaledar koji sluzi 
za koordinaciju odsustva izmenju kolega. Aplikacija unosi u evidenciju I neradne dane (verske I drzavne praznike) 
koji su definisani po razlicitim grupama kako bi se praznici mogli prilagoditi razlcitim nacionalnostima I razlictim 
veroispovestima koji je veoma bitan deo u multi etnickim radnim okruzenjima koja se cesto srecu kada je u pitanju remote rada od kuce.
Program ogranicava radnike u pogledu broja dana godisnjeg odmora koje je radnik u mogucnosti da uzme u jednoj godini.  


Entiteti :

1.	employees
Zaposleni: svaki zaposleni će biti registrovan u aplikaciji sa svojim licnim podacima, kao što su ime, prezime, e-mail adresa, država….
Zaposleni takodje ima definisanog nadredjenog koji je jedan od zaposlenih. Nadredjeni ne mora postojati(moze biti NULL) u situaciji 
kada je zaposleni glavni u firmi (npr. Direktor/vlasnik) i odobrava sam sebi odsustva

2.	requests
Zahtevi za odusustvo. svaki zaposleni moze uputiti zahtev za ostustvo gde se definise datum I 
vrsta osustva: placeno, neplaceno, bolovanje. Zahtev moze da se odobri od strane nadredjenog u 
slucaju da zahtev salje radnik koji nema nadredjenog(director), zahtev se automatski smatra odobrenim.
-- Type ENUM(odmor, bolovanje, neplaceno)
-- Cancelled Bool(True u slucaju da zaposleni otkaze, default je False)

3.	requestDates
Dan odsustva na zahtevu. Mora postojati kao poseban entitet zbog prisustva one-to-many relacije u odnosu na zahtev. 
Jedan zahtev ima vise datuma(dana) 
-- Status ENUM(dozvoljeno, odbijeno) 

4.	holidayGroups
Grupe praznika, neradnih dana: aplikacija sadri grupe praznika koje se dodelju radnicima pripadjuce nacionalnosti I veroispovesti. 

5.	holidayGroupsDates
Dani praznika grupe. Svaka grupa sadzi vise dana praznika gde su definisani datum I ime praznika. 




DUMP BAZE PODATAKA SE NALAZI U init_db DIREKTORIJUMU



admin user: admin@itbc.rs

admin pass: Admin123





Endpoints:

1.	Dodavanje radnika
2.	Azuriranje podataka radnika
3.	Brisanje radnika

4.	Dodavanje grupe odmora
5.	Azuriranje grupe odmora
6.	Brisanje grupe odmora

7.	Dodavanja dana na grupi odmora
8.	Azuriranje dana na grupi odmora
9.	Brisanje dana na grupi odmora

10.	Slanje zahteva za odsustvo

11.	Slanje zahteva za svaki dan pojedinacno u okviru zahteva za odsustvo
12.	Odobravanje zahteva za dane pojedinacno od strane superior-a
13.	Otkazivanje zahteva za odsustvo od strane samog korisnika samo ako je datum pre prvog dana zatrazenog odsustva
14.	Listanje dana odsustva po radniku
15.	Listanje kalendara svih odsutnih radnika
16.	Lista odsutnih radnika danas

Dodatne funkcionalnosti:

•	Endpoints (12 I 13) - Nadređeni može da odobri deo zatraženih dana u zahtevu. U tom slučaju, uputilac zahteva ima pravo da otkaže zahtev, ali samo ukoliko je datum otkazivanja pre datuma početka odsustva koji je zahtevao (može da otkaže samo te koji su delimično odobreni, ove regularne ne može).
  
•	Imejl se šalje sa servera podnosiocu zahteva u trenutku kada mu se odobri odsustvo, kako bi bio obavešten o tome.

