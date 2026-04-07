import requests
import time
import os

def scan_and_capture():
    ranges = [6060, 9420, 13600, 4625] 
    
    for f in ranges:
        print(f"📡 Tentativo su {f} kHz...")
        # Cambiamo leggermente l'URL per forzare un formato più stabile
        url = f"http://websdr.ewi.utwente.nl:8901/~~sample?f={f}&m=am&s=0"
        
        try:
            # Aumentiamo il timeout per dare tempo al server di rispondere
            r = requests.get(url, stream=True, timeout=15)
            if r.status_code == 200:
                with open(f"capture_{f}.wav", "wb") as f_out:
                    start = time.time()
                    for chunk in r.iter_content(chunk_size=4096):
                        f_out.write(chunk)
                        if time.time() - start > 20: # 20 secondi di audio
                            break
                # Controlliamo se il file è almeno 10KB (se è più piccolo è solo rumore o errore)
                if os.path.getsize(f"capture_{f}.wav") < 10000:
                    os.remove(f"capture_{f}.wav")
                    print(f"⚠️ File {f} troppo piccolo, scartato.")
                else:
                    print(f"✅ Segnale catturato su {f} kHz.")
        except Exception as e:
            print(f"❌ Errore su {f}: {e}")

if __name__ == "__main__":
    scan_and_capture()
