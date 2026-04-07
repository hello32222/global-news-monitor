import whisper
import os
from datetime import datetime
from fpdf import FPDF

def create_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="RAPPORTO INTELLIGENCE ONDE CORTE", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Generato il: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True, align='C')
    pdf.ln(10)

    for freq, text in data.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, txt=f"FREQUENZA: {freq} kHz", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 5, txt=text)
        pdf.ln(5)
    
    pdf.output("REPORT_RADIO.pdf")

def process_intelligence():
    model = whisper.load_model("tiny")
    results_dict = {}
    
    files = [f for f in os.listdir('.') if f.startswith("capture_") and f.endswith(".wav")]
    
    for audio in files:
        freq = audio.split("_")[1].split(".")[0]
        try:
            # Whisper analizza l'audio
            result = model.transcribe(audio, task="translate")
            text = result['text'].strip()

            if len(text) > 15: # Solo se ha senso
                results_dict[freq] = text
        except Exception as e:
            print(f"Errore su {freq}: {e}")
        finally:
            os.remove(audio)

    if results_dict:
        create_pdf_report(results_dict)
        print("✅ PDF Generato con successo!")
    else:
        print("⚠️ Nessun dato utile per il PDF.")

if __name__ == "__main__":
    process_intelligence()
