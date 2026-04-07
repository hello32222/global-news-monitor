import requests
import time

def scan_and_capture():
    # Frequenze "calde" dove di solito c'è attività geopolitica/militare
    # Invece di una lista fissa, potresti espanderla a tutta la banda HF
    ranges = [4625, 6060, 11175, 15480, 13600] 
    
    for f in ranges:
        print(f"📡 Sintonizzazione su {f} kHz...")
        # Usiamo 'usb' per filtrare la musica e sentire solo voci/dati
        url = f"http://websdr.ewi.utwente.nl:8901/~~sample?f={f}&m=usb&s=0"
        
        try:
            r = requests.get(url, stream=True, timeout=5)
            with open(f"capture_{f}.wav", "wb") as f_out:
                start = time.time()
                for chunk in r.iter_content(chunk_size=1024):
                    f_out.write(chunk)
                    if time.time() - start > 20: # Registra 20 secondi
                        break
            print(f"✅ Segnale catturato.")
        except:
            print(f"❌ Salto frequenza {f}")

if __name__ == "__main__":
    scan_and_capture()
