# Importiamo le funzioni dal modulo che abbiamo creato noi
import funzioni_meteo

def main():
    """Funzione principale che contiene il ciclo del menù"""
    while True:
        print("\n==============================")
        print("      METEO & INFO CITTÀ      ")
        print("==============================")
        print("1. Cerca meteo")
        print("2. Mostra grafico delle temperature")
        print("3. Esci dal programma")
        print("==============================")

        scelta = input("Seleziona un'opzione (1-3): ")

        if scelta == "1":
            citta = input("\nInserisci il nome della città: ")

            # Richiamiamo la funzione dal nostro modulo funzioni_meteo
            risultato = funzioni_meteo.ottieni_meteo(citta)

            if risultato is None:
                print("❌ Errore: Città non trouvata. Controlla come l'hai scritta.")
            else:
                temperatura, descrizione, emoji = risultato

                print(f"\n🌍 Città: {citta.capitalize()}")
                print(f"🌡️ Temperatura: {temperatura}°C")
                print(f"{emoji} Condizioni: {descrizione}")

                # Salviamo i dati nel file CSV
                funzioni_meteo.salva_dati(citta, temperatura)
                print("\n💾 Dati salvati correttamente nel file CSV!")

        elif scelta == "2":
            citta = input("\nInserisci la città di cui vuoi vedere il grafico: ")
            print(f"Generazione del grafico per {citta} in corso...")
            funzioni_meteo.mostra_grafico(citta)

        elif scelta == "3":
            print("\nGrazie per aver usato la nostra applicazione. Arrivederci!")
            break

        else:
            print("⚠️ Scelta non valida. Inserisci un numero tra 1 e 3.")

# Questo è il controllo che hai chiesto: avvia il programma solo se esegui DIRETTAMENTE questo file
if __name__ == "__main__":
    main()