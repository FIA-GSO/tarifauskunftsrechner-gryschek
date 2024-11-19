float preis_erwachsene = 5.0
float preis_erwachsene_tag = 10
float preis_kinder = 2.5
float preis_kinder_tag = 5
float preis_jugend = 3.5
float preis_jugend_tag = 6 
float preis_premium = 3.0
float preis_premium_tag = 6
float preis_basis = 4.0
float preis_basis_tag =
float sekt = 0.75
float zwischensumme = 0
float endpreis = 0

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
        if antwort_rabatt == "p":                                     #preise noch eintragen un vriablen erstellen für tagestickets
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Möchten sie ein Halbtages oder Tagesticket?")
            print(" Drücken sie 'h für ein Halbtages- und 'T' für ein Tagesticket")
            antwort_ticket = input()
            if antwort_ticket == "t":
                print(" Preis: ", preis_premium_tag, " Euro ")
            elif antwort_ticket == "h":
                print(" Preis: ", preis_premium, " Euro ")
            print(" Möchten Sie für 0.75€ Aufpreis einen Sekt trinken? ")
            print(" Drücken Sie die Taste 'j' wenn Sie einen Sekt möchten. ")
            print(" Wenn Sie keinen Sekt möchten drücken Sie eine beliebige andere Taste. ")
            antwort_sekt = input()
            if antwort_sekt == "j":
                    print("test ja")
                    zwischensumme += sekt
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro")

    print(" ### Viel Spaß ### ")
    print(" Wollen Sie einen weiteren Tarif abfragen? ")
    antwort_abfrage = input()
    print(" Bitte drücken Sie die Taste 'j' für ja")
    print(" Wenn sie keinen weiteren Tarif erfragen möchten drücken Sie die Taste 'n' ")
    if antwort_abfrage == "j":
        print("Möchten Sie den Ticketpreis zur Gesamtsumme addieren?")
        antwort_gesammtsumme = input()
        if antwort_gesammtsumme == "j":
            endpreis += zwischensumme
        print("Starte neue Tarifabfrage") 
    
    if antwort_abfrage == "n":
        endpreis
        print(" ### Ihr Preis Beträgt var(endpreis)")
        break
