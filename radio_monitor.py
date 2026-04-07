import whisper
import os
from datetime import datetime

def process_intelligence():
    # Carichiamo il modello AI
    model = whisper.load_model("tiny")
    report = f"\n## 📡 Intercettazioni del {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    
    # Cerchiamo i file audio creati dallo scanner
    files = [f for f in os.listdir('.') if f.startswith("capture_")]
    found_content = False

    for audio in files:
        freq = audio.split("_")[1].split(".")[0]
        print(f"Analizzando frequenza {freq} kHz...")
        
        # Whisper trascrive e traduce
        result = model.transcribe(audio, task="translate")
        text = result['text'].strip()

        # Filtro: Lunghezza minima e no musica
        if len(text) > 20 and "music" not in text.lower():
            report += f"**Frequenza {freq} kHz:** {text}\n\n"
            found_content = True
        
        # Elimina il file audio per pulizia
        os.remove(audio)

    # Scrittura del report finale
    if found_content:
        with open("RADIO_REPORT.md", "a", encoding="utf-8") as f:
            f.write(report + "---\n")
        print("✅ Report aggiornato.")
    else:
        print("⚠️ Nessun contenuto rilevante trovato in questa sessione.")

if __name__ == "__main__":
    process_intelligence()
