import requests 
#importa la libreria requests usata per fare richieste a siti su internet.

import pandas as pd
#Importa pandas che serve per lavorare con tabelle e file CSV

import matplotlib.pyplot as plt
#Importa matplotlib che serve per creare grafici

from datetime import datetime
#Dalla libreria già esistente su python importa datetime che serve per ottenere data e ora attuali

CHIAVE_API = "b4820b2abbe3d0764b71ed2dc1f38453"
#Salva la chiave API in una variabile, questa chiave serve per poter usare i servizi meteo

def ottieni_meteo(citta):
#Definisce una funzione ottieni meteo che riceve in ingresso una citta
    url = f"http://api.openweathermap.org/data/2.5/weather?q={citta}&appid={CHIAVE_API}&units=metric&lang=it"
    #costruisce l'url per chiamare l'APi meteo
    #units=metric -> serve per avere la temperatura in gradi celsius
    #lang=it -> descrive il meteo in lingua italiana 
    
    risposta = requests.get(url)
    #Invia una richiesta get all'API
    
    dati = risposta.json()
    #converte la risposta ricevuta in formato json
    
    if risposta.status_code != 200:
    #controlla se il server ha risposto con o senza errore
    # status_code 200 sta a significare "tutto ok!"

        return None
        #se c'è errore non restituisce niente
    
    temperatura = dati["main"]["temp"]
    #Prende la temperatura dal json ricevuto
    
    descrizione = dati["weather"][0]["description"]
    #Prende la desscrizione del meteo dal json Es: soleggiato
    
    return temperatura, descrizione 