telefonkatalog = [] # listformat ["fornavn", "etternavn", "telefonnummer"]


def printMeny():
    print("telefonkatalog")
    print("| 1. legg til ny person |") 
    print("| 2. søk opp person eller telefonnummer |")
    print("| 3. vis alle personer |")
    print("| 4. avslutt|")
    print ("")
    menyvalg = input ("skriv inn tall for å velge fra menyen: ")
    utefoermenyvalg(menyvalg)


def utefoermenyvalg(valgtTall):
    if valgtTall == "1": # input returnerer string, derfor "1"
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif  valgtTall == "3":
        visAllePersoner()
    elif  valgtTall == "4":
        bekreftelese = input ("Er du sikker på at du vil avslutte? J/N")
        if (bekreftelese == "J" or bekreftelese == "j"):  # sjekker bare for ja
             exit()
        else:
             nyttForsoek = input ("ugyldig valg. Velg et tall mellom 1-4: ")
             utefoermenyvalg(nyttForsoek)


def registrerPerson(): 
    fornavn = input ("skriv inn fornavn: ")
    etternavn = input ("skriv inn etternavn: ")
    telefonnummer = input ("skriv inn telefonnummer: ")

    nyRegistrering = [fornavn, etternavn, telefonnummer]
    telefonkatalog .append(nyRegistrering)

    print("{0} {1} er registret med telefonnummer {2}"
          .format (fornavn, etternavn, telefonnummer ))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()


def visAllePersoner():
    if not telefonkatalog:
        print ("Det er ingen registrete personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else:
        print("")
        
        for personer in telefonkatalog: 
            print("* Fornavn: {:15s} etternavn: {:15s} Telefonnummer: {:8s}"
            .format(personer[0], personer[1], personer [2]))
        print("")

        input("Trkk en tast for å gå tilbake til menyen")
        printMeny()


def sokPerson ():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else:
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
    if sokefelt == "1":
        sokeTekst = input ("Fornavn: ")
        finnPerson ("fornavn", sokeTekst)
    elif sokefelt == "2":
        sokeTekst = input ("Etternavn: ")
        finnPerson("etternavn", sokeTekst)
    elif sokefelt == "3":
        sokeTekst = input("Telefonnummer: ")
        finnPerson("telefonnummer", sokeTekst)
    elif sokefelt == "4":
        printMeny()
    else:
        print("ugyldig valg. Velg et tall mellom 1-4: ")
        sokPerson()


# typeSok angir om man søker på fornavn, etternavn, eller telefonnummer
def finnPerson(typeSok, sokeTekst):
    for personer in telefonkatalog:
        if typeSok == "fornavn":
                if personer [0] == sokeTekst:
                    print("{0} {1} har telefonnummer {2}"
                          .format(personer[0], personer [1], personer [2]))
                else:
                    print("Finner ingen personer med fornavn" + sokeTekst)
                    sokPerson()
        elif typeSok == "etternavn":
                 if personer[1] == sokeTekst:
                    print("{0} {1} har telefonnummer{2}"
                      .format (personer[0], personer[1], personer[2]))
                 else:
                    print ("Finner ingen personer med etternavn" + sokeTekst)
                    sokPerson()
        elif typeSok == "etternavn":
                    if personer [1] == sokeTekst:
                        print ("{0} {1} har telefonnummer {2}"
                                 .format(personer[0], personer[1], personer[2]))
        elif typeSok == "telefonnummer":
                    if personer [2] == sokeTekst:
                        print ("Telefonnummer {0} tilhører {1} {2}"
                               .format(personer[2], personer[0], personer[1]))
                    else: 
                        print("telefonnummer" + sokeTekst + " er ikke registrert. /n")
                    

printMeny()  # Starter programmet ved å skrive menyen første gang