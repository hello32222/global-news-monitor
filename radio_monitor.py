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

if found_content:
        with open("RADIO_REPORT.md", "a", encoding="utf-8") as f:
            f.write(report + "\n---\n")
            f.flush()
            os.fsync(f.fileno())
        print("✅ Report scritto e salvato correttamente.")
    else:
        # Crea comunque il file se non esiste, così GitHub lo vede "disponibile"
        if not os.path.exists("RADIO_REPORT.md"):
            with open("RADIO_REPORT.md", "w") as f:
                f.write("# 📡 Monitor Radio Onde Corte\n")
        print("Wait: Nessun parlato rilevato in questo turno.")
