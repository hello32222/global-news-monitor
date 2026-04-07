import whisper
import os
from datetime import datetime

def process_intelligence():
    model = whisper.load_model("tiny")
    report = f"\n## 📡 Intercettazioni del {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    files = [f for f in os.listdir('.') if f.startswith("capture_") and f.endswith(".wav")]
    found_content = False

    for audio in files:
        freq = audio.split("_")[1].split(".")[0]
        try:
            print(f"Analizzando frequenza {freq} kHz...")
            # Aggiungiamo il task translate per avere tutto in inglese/italiano
            result = model.transcribe(audio, task="translate")
            text = result['text'].strip()

            if len(text) > 20 and "music" not in text.lower():
                report += f"**Frequenza {freq} kHz:** {text}\n\n"
                found_content = True
        except Exception as e:
            print(f"⚠️ Salto {freq} kHz perché il file audio è illeggibile.")
        finally:
            if os.path.exists(audio):
                os.remove(audio)

    if found_content:
        with open("RADIO_REPORT.md", "a", encoding="utf-8") as f:
            f.write(report + "---\n")
