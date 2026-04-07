import feedparser
import pandas as pd
from datetime import datetime

# Fonti RSS focalizzate su Geopolitica ed Economia
FEEDS = {
    'Reuters_World': 'https://www.reutersagency.com/feed/?best-sectors=foreign-policy-and-international-relations&post-type=best-of',
    'IMF_News': 'https://www.imf.org/en/News/RSS',
    'BBC_World': 'http://feeds.bbci.co.uk/news/world/rss.xml'
}

# Parole chiave per il filtro
KEYWORDS = ['war', 'sanctions', 'central bank', 'inflation', 'treaty', 'border', 'energy', 'nato', 'brics']

def fetch_news():
    news_list = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title.lower()
            # Filtro: se una delle parole chiave è nel titolo, salviamo
            if any(key in title for key in KEYWORDS):
                news_list.append({
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'source': source,
                    'title': entry.title,
                    'link': entry.link
                })
    return news_list

def save_report(news):
    if not news:
        return
    df = pd.DataFrame(news)
    # Crea un file Markdown leggibile su GitHub
    with open("MONITOR.md", "w") as f:
        f.write("# 🌍 Global Geopolitical Monitor\n\n")
        f.write(f"Ultimo aggiornamento: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for _, item in df.iterrows():
            f.write(f"### {item['title']}\n")
            f.write(f"- **Fonte:** {item['source']}\n")
            f.write(f"- [Leggi di più]({item['link']})\n\n")

if __name__ == "__main__":
    data = fetch_news()
    save_report(data)
    print("Monitor aggiornato con successo!")
