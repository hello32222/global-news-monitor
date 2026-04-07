import whisper
import os
from datetime import datetime

def transcribe_and_save():
    audio_file = "radio_capture.wav"
    
    # Controlliamo se il file audio è stato effettivamente creato
    if not os.path.exists(audio_file):
        print("Errore: Nessun audio catturato.")
        return

    # Carichiamo il modello AI (tiny è il più veloce e gratuito)
    model = whisper.load_model("tiny")
    
    # Trascrive e traduce automaticamente in inglese
    print("Analisi audio in corso...")
    result = model.transcribe(audio_file, task="translate")
    text = result['text']

    # Scriviamo il risultato nel report
    with open("RADIO_REPORT.md", "a", encoding="utf-8") as f:
        f.write(f"\n## Intercettazione del {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- **Testo rilevato:** {text}\n")
        f.write("\n---\n")

if __name__ == "__main__":
    transcribe_and_save()
