import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

CHIAVE_API = "b4820b2abbe3d0764b71ed2dc1f38453"

def ottieni_emoji(descrizione):
    """Semplice funzione per associare un'emoji alla descrizione del meteo"""
    descrizione = descrizione.lower()
    if "sole" in descrizione or "sereno" in descrizione or "chiaro" in descrizione:
        return "☀️"
    elif "nuvolo" in descrizione or "nubi" in descrizione or "coperto" in descrizione:
        return "☁️"
    elif "pioggia" in descrizione or "pioviggine" in descrizione:
        return "🌧️"
    elif "temporale" in descrizione:
        return "⛈️"
    elif "neve" in descrizione:
        return "❄️"
    elif "nebbia" in descrizione or "foschia" in descrizione:
        return "🌫️"
    else:
        return "🌍" 

def ottieni_meteo(citta):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={citta}&appid={CHIAVE_API}&units=metric&lang=it"
    risposta = requests.get(url)
    dati = risposta.json()

    if risposta.status_code != 200:
        return None

    temperatura = dati["main"]["temp"]
    descrizione = dati["weather"][0]["description"]
    
    # Recuperiamo l'emoji giusta usando la nostra funzione interna
    emoji = ottieni_emoji(descrizione)

    return temperatura, descrizione, emoji

def salva_dati(citta, temperatura):
    tempo = datetime.now().strftime("%Y-%m-%d %H:%M") # Formattiamo il tempo per renderlo leggibile

    dataframe = pd.DataFrame([[citta, tempo, temperatura]],
                             columns=["citta", "tempo", "temperatura"])

    dataframe.to_csv("dati.csv", mode="a", header=False, index=False)

def mostra_grafico(citta):
    try:
        dataframe = pd.read_csv("dati.csv", names=["citta", "tempo", "temperatura"])
    except:
        print("Nessun dato salvato in CSV. Cerca prima una città per salvare i dati!")
        return

    dataframe = dataframe[dataframe["citta"] == citta]

    if dataframe.empty:
        print(f"Nessun dato registrato nel CSV per la città di: {citta}")
        return

    # Creazione del grafico (lasciato semplice come il tuo)
    plt.plot(dataframe["tempo"], dataframe["temperatura"], marker="o", color="blue")
    plt.title(f"Andamento temperatura - {citta}")
    plt.xlabel("Tempo (Data e Ora)")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("aura.png")
    plt.show() # Mostra il grafico a schermo oltre a salvarlo