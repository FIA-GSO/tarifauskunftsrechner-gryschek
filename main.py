preis_erwachsene:float = 5.0
preis_erwachsene_tag:float = 10.0
preis_kinder:float = 2.5
preis_kinder_tag:float = 5.0
preis_jugend:float = 3.5
preis_jugend_tag:float = 6.0
preis_premium_tag:float = 6.0
preis_premium:float = 3.0
preis_basis:float = 4.0
preis_basis_tag:float = 8.0
sekt:float = 0.75
zwischensumme:float = 0.0
endpreis:float = 0.0

print("                             @                                                                ")
print("       @@@@@@                                @                   @                            ")
print("       @    @@   @    @   @@@@       @@@@    @ @@@   @@     @  @@@@@@@    @@@@       @@       ")
print("       @     @   @    @      @      @        @    @@  @@   @     @       @    @@              ")
print("       @     @   @    @      @       @@@     @    @@   @  @@     @       @@@@@@@              ")
print("       @    @@   @   @@      @          @@   @    @     @@@      @       @           @        ")
print("       @@@@      @@@@ @   @@@@@@@   @@@@     @@@@@       @        @@@@    @@@@@      @@       ")
print("                                                        @                            @        ")
print("                                                     @@                                       ")
print(" Press 'e' for the English menu. ")
print(" Drücke 'd' für das Deutsche Menü. ")
antwort_sprache = input()
if antwort_sprache == "d":
    while True:
        print(" ### Tarifauskunftsrechner Museum ### ")
        print(" Hallo, geben Sie bitte Ihr Alter ein.")
        alter_gast = int(input())

        if alter_gast < 14:
            print(" ### Eintritt Kinder ### ")
            print(" Möchten Sie ein Halbtages oder Tagesticket?")
            print(" Drücken Sie 'h' für ein Halbtages- und 't' für ein Tagesticket")
            antwort_ticket = input()
            if antwort_ticket == "h":
                print(" Preis: ", preis_kinder, " Euro ")
                zwischensumme += preis_kinder
            elif antwort_ticket == "t":
                print(" Preis: ", preis_kinder_tag, " Euro ")
                zwischensumme+= preis_kinder_tag
        elif 14 <= alter_gast < 18:
            print(" ### Eintritt Jugendliche ### ")
            print(" Möchten Sie ein Halbtages oder Tagesticket?")
            print(" Drücken Sie 'h' für ein Halbtages- und 't' für ein Tagesticket")
            antwort_ticket = input()
            if antwort_ticket == "h":
                print(" Preis: ", preis_jugend, " Euro ")
                zwischensumme += preis_jugend
            elif antwort_ticket == "t":
                print(" Preis: ", preis_jugend_tag, " Euro ")
                zwischensumme += preis_jugend_tag
        else:
            print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
            print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
            print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
            print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
            antwort_rabatt = input()
            if antwort_rabatt == "p":                                     
                print(" ### Eintritt Premium-Mitglied ### ")
                print(" Möchten Sie ein Halbtages oder Tagesticket?")
                print(" Drücken Sie 'h' für ein Halbtages- und 't' für ein Tagesticket")
                antwort_ticket = input()
                if antwort_ticket == "t":
                    print(" Preis: ", preis_premium_tag, " Euro ")
                    zwischensumme += preis_premium_tag
                elif antwort_ticket == "h":
                    print(" Preis: ", preis_premium, " Euro ")
                    zwischensumme += preis_premium
                print(" Möchten Sie für 0.75€ Aufpreis einen Sekt trinken? ")
                print(" Drücken Sie die Taste 'j' wenn Sie einen Sekt möchten. ")
                print(" Wenn Sie keinen Sekt möchten drücken Sie eine beliebige andere Taste. ")
                antwort_sekt = input()
                if antwort_sekt == "j":
                    print(" Sie haben einen Sekt ausgewählt.")
                    zwischensumme += sekt
                else:
                    print(" Sie haben keinen Sekt ausgewählt. ")       
            elif antwort_rabatt == "b":
                print(" ### Eintritt Basis-Mitglied ### ")
                print(" Möchten Sie ein Halbtages oder Tagesticket?")
                print(" Drücken Sie 'h' für ein Halbtages- und 't' für ein Tagesticket")
                antwort_ticket = input()
                if antwort_ticket == "t":
                    print(" Preis: ", preis_basis_tag, " Euro ")
                    zwischensumme += preis_basis_tag
                elif antwort_ticket == "h":
                    print(" Preis: ", preis_basis, " Euro ")
                    zwischensumme += preis_basis
            else:
                print(" ### Eintritt Erwachsene (voller Preis) ### ")
                print(" Möchten Sie ein Halbtages oder Tagesticket?")
                print(" Drücken Sie 'h für ein Halbtages- und 'T' für ein Tagesticket")
                antwort_ticket = input()
                if antwort_ticket == "t":
                    print(" Preis: ", preis_erwachsene_tag, " Euro ")
                    zwischensumme += preis_erwachsene_tag
                elif antwort_ticket == "h":
                    print(" Preis: ", preis_erwachsene, " Euro ")
                    zwischensumme += preis_erwachsene
        print(" Möchten Sie den Ticketpreis zur Gesamtsumme addieren? ")
        print(" Wenn Sie den Preis addieren möchten drücken sie 'j' ")
        print(" Wenn Sie den Preis nicht addieren möchten drücken sie eine beliebige andere Taste. ")
        antwort_gesammtsumme = input()     
        if antwort_gesammtsumme == "j":
            endpreis += zwischensumme       
        print(" Wollen Sie einen weiteren Tarif abfragen? ")
        print(" Bitte drücken Sie die Taste 'j' für ja ")
        print(" Wenn Sie keinen weiteren Tarif erfragen möchten drücken Sie die Taste eine beliebige andere Taste. ")
        antwort_abfrage = input()
        if antwort_abfrage == "j":
            print("Starte neue Tarifabfrage") 
        else:
            print(" ### Ihr Preis Beträgt ", endpreis," Euro ### ")
            break
        print(" ### Viel Spaß ### ")
elif antwort_sprache == "e":
    while True:
        print(" ### Ticketcalculator Museum ### ")
        print(" Hello, please enter your age.")
        alter_gast = int(input())

        if alter_gast < 14:
            print(" ### Entry Children ### ")
            print(" Would you like a day or halfday pass? ")
            print(" Press 'd' for a day and 'h' for a halfday pass. ")
            antwort_ticket = input()
            if antwort_ticket == "h":
                print(" Price: ", preis_kinder, " Euro ")
                zwischensumme += preis_kinder
            elif antwort_ticket == "d":
                print(" Price: ", preis_kinder_tag, " Euro ")
                zwischensumme+= preis_kinder_tag
        elif 14 <= alter_gast < 18:
            print(" ### Entry Teenager ### ")
            print(" Would you like a day or halfday pass? ")
            print(" Press 'd' for a day and 'h' for a halfday pass. ")
            antwort_ticket = input()
            if antwort_ticket == "h":
                print(" Price: ", preis_jugend, " Euro ")
                zwischensumme += preis_jugend
            elif antwort_ticket == "d":
                print(" Price: ", preis_jugend_tag, " Euro ")
                zwischensumme += preis_jugend_tag
        else:
            print(" Do you own a Duisburg Museum Membership? (Verification needed) ")
            print(" If you are a premium member, press 'p'.")
            print(" If you are a basic member, press'b'.")
            print(" If you do not own a membership press any other button. ")
            antwort_rabatt = input()
            if antwort_rabatt == "p":                                     
                print(" ### EiEntry Premium-Member ### ")
                print(" Would you like a day or halfday pass? ")
                print(" Press 'd' for a day and 'h' for a halfday pass. ")
                antwort_ticket = input()
                if antwort_ticket == "d":
                    print(" Price: ", preis_premium_tag, " Euro ")
                    zwischensumme += preis_premium_tag
                elif antwort_ticket == "h":
                    print(" Prices: ", preis_premium, " Euro ")
                    zwischensumme += preis_premium
                print(" Would you like a glass of sparkling wine for 0.75 Euro additional charge? ")
                print(" Press 'y' if you want a glass of sparkling wine. ")
                print(" If you do not want a glass of sparkling wine press any other button. ")
                antwort_sekt = input()
                if antwort_sekt == "y":
                    print(" You chose a glass of sparkling wine.")
                    zwischensumme += sekt
                else:
                    print(" You did not choose a glass of sparkling wine. ")       
            elif antwort_rabatt == "b":
                print(" ### Entry Basic-Member ### ")
                print(" Would you like a day or halfday pass? ")
                print(" Press 'd' for a day and 'h' for a halfday pass. ")
                antwort_ticket = input()
                if antwort_ticket == "d":
                    print(" Price: ", preis_basis_tag, " Euro ")
                    zwischensumme += preis_basis_tag
                elif antwort_ticket == "h":
                    print(" Price: ", preis_basis, " Euro ")
                    zwischensumme += preis_basis
            else:
                print(" ### Entry Adults (full Price) ### ")
                print(" Would you like a day or halfday pass? ")
                print(" Press 'd' for a day and 'h' for a halfday pass. ")
                antwort_ticket = input()
                if antwort_ticket == "d":
                    print(" Price: ", preis_erwachsene_tag, " Euro ")
                    zwischensumme += preis_erwachsene_tag
                elif antwort_ticket == "h":
                    print(" Price: ", preis_erwachsene, " Euro ")
                    zwischensumme += preis_erwachsene
        print(" Would you like to add your ticketprice to the total? ")
        print(" If you want to add it to the total press 'y' ")
        print(" If you do not want to add it to the total press any other button. ")
        antwort_gesammtsumme = input()     
        if antwort_gesammtsumme == "y":
            endpreis += zwischensumme       
        print(" Would you like to start another ticket calculation? ")
        print(" Press 'y' for yes")
        print(" If you do not want to start a new calculation press any other button. ")
        antwort_abfrage = input()
        if antwort_abfrage == "y":
            print("Starte neue Tarifabfrage") 
        else:
            print(" ### Your total is ", endpreis," Euro ### ")
            break
        print(" ### Have a nice day ### ")