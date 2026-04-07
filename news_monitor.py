import whisper
import os
import datetime

# --- CONFIGURAZIONE ---
# Esempio: 4625 kHz (The Buzzer) o 15480 kHz (Radio Free Europe)
FREQUENCY = "15480" 
MODE = "usb" # usb, lsb, am, cw

def transcribe_audio(file_path):
    print("Caricamento modello AI Whisper (modello tiny)...")
    model = whisper.load_model("tiny")
    
    # Task 'translate' trascrive E traduce in inglese automaticamente
    result = model.transcribe(file_path, task="translate")
    return result['text']

def update_github_report(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("RADIO_REPORT.md", "a") as f:
        f.write(f"\n## Intercettazione del {timestamp}\n")
        f.write(f"- **Frequenza:** {FREQUENCY} kHz\n")
        f.write(f"- **Trascrizione/Traduzione:** {text}\n")
        f.write("\n---\n")

if __name__ == "__main__":
    # NOTA: Per scaricare l'audio reale da Twente serve un client dedicato.
    # Per ora simuliamo il processo per assicurarci che l'AI funzioni.
    # In un ambiente GitHub, useremo un comando 'curl' nel workflow per catturare l'audio.
    
    audio_file = "radio_capture.wav"
    
    if os.path.exists(audio_file):
        translation = transcribe_audio(audio_file)
        update_github_report(translation)
        print("Trascrizione completata!")
    else:
        print("Nessun file audio trovato. In attesa di cattura...")
