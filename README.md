# Generatore di QR Code

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

Un'applicazione web costruita con Streamlit che permette di generare QR code personalizzati a partire da un URL.

![Generatore QR Code](https://raw.githubusercontent.com/streamlit/streamlit/master/examples/data/balloons.jpg)

## Caratteristiche

- Generazione di QR code con stili di colore diversi
- Personalizzazione della dimensione del QR code
- Download dell'immagine generata
- Interfaccia utente intuitiva e accattivante

## Requisiti

- Python 3.7 o superiore
- pip (gestore pacchetti Python)

## Installazione

1. Clona questo repository o scarica i file

2. Crea un ambiente virtuale (opzionale ma consigliato):

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

3. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

## Utilizzo

1. Avvia l'applicazione:

```bash
streamlit run app.py
```

2. Apri il browser all'indirizzo mostrato nel terminale (di solito http://localhost:8501)

3. Inserisci l'URL che desideri convertire in QR code

4. Personalizza lo stile e le dimensioni del QR code

5. Clicca "Genera QR Code"

6. Scarica l'immagine generata

## Struttura del Progetto

```
generatore-qrcode/
├── app.py                  # Applicazione principale Streamlit
├── requirements.txt        # Dipendenze Python
├── generated_qrcodes/      # Directory per i QR code generati
└── README.md               # Questo file
```

## Licenza

MIT
