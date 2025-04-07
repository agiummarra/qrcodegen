# Generatore di QR Code

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

Un'applicazione web costruita con Streamlit che permette di generare QR code personalizzati a partire da un URL.

## Preview dell'applicazione

![Preview del Generatore QR Code](preview.png)

## Caratteristiche

- Generazione di QR code con stili di colore diversi (colore unico o gradienti)
- Personalizzazione completa dei colori con color picker visuale
- Opzione per inserire un logo personalizzato al centro del QR code
- Controllo della dimensione del QR code
- Download immediato dell'immagine generata
- Interfaccia utente intuitiva e responsive

## Esempi di QR code generabili

L'applicazione permette di creare QR code con diversi stili:

- **Colore Unico:** QR code monocromatico personalizzabile
- **Orizzontale:** Gradiente orizzontale tra due colori
- **Verticale:** Gradiente verticale tra due colori
- **Radiale:** Gradiente che si diffonde dal centro verso l'esterno
- **Quadrato:** Gradiente quadrato con colore centrale e colore esterno

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
