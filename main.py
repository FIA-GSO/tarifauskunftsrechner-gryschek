preis_erwachsene = 5.0
preis_kinder = 2.5
preis_jugend = 3.5
preis_premium = 3.0
preis_premium_tag = 6
preis_basis = 4.0

print("                             @                                                                ")
print("       @@@@@@                                @                   @                            ")
print("       @    @@   @    @   @@@@       @@@@    @ @@@   @@     @  @@@@@@@    @@@@       @@       ")
print("       @     @   @    @      @      @        @    @@  @@   @     @       @    @@              ")
print("       @     @   @    @      @       @@@     @    @@   @  @@     @       @@@@@@@              ")
print("       @    @@   @   @@      @          @@   @    @     @@@      @       @           @        ")
print("       @@@@      @@@@ @   @@@@@@@   @@@@     @@@@@       @        @@@@    @@@@@      @@       ")
print("                                                        @                            @        ")
print("                                                     @@                                       ")
while True:
    print(" ### Tarifauskunftsrechner Museum ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    elif alter_gast > 14 and alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jugend, " Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":                                     #nested loop mit tages ticket ausgabe fehlt noch, maybe mit
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Möchten sie ein Halbtages oder Tagesticket?")
            print(" Drücken sie 'h für ein Halbtages- und 'T' für ein Tagesticket")
            antwort_ticket = input()
            if antwort_ticket == "t":
                print(" Preis: ", preis_premium_tag, " Euro ")
            elif antwort_ticket == "h":
                print(" Preis: ", preis_premium, " Euro ")
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro")
        print(" Möchten Sie für 0.75€ Aufpreis einen Sekt trinken? ")
        print(" Drücken Sie die Taste 'j' wenn Sie einen Sekt möchten. ")
        print(" Wenn Sie keinen Sekt möchten drücken Sie die Taste 'n' ")
        antwort_sekt = input()
        if antwort_sekt == "j":
                print("test ja")
        elif antwort_sekt == "n":
            print("no")
    print(" ### Viel Spaß ### ")
    print(" Wollen Sie einen weiteren Tarif abfragen? ")
    antwort_abfrage = input()
    print(" Bitte drücken Sie die Taste 'j' für ja")
    print(" Wenn sie keinen weiteren Tarif erfragen möchten drücken Sie die Taste 'n' ")
    if antwort_abfrage == "j":
        print("Starte neue Tarifabfrage")
    
    if antwort_abfrage == "n":
        endpreis = "1ticket und 1sekt "
        print(" ### Ihr Preis Beträgt ")
        break
