# 🧠 AI News Assistant

An AI-powered news reader built with **Django, TailwindCSS, and HuggingFace Transformers** that aggregates news from RSS feeds and adds intelligent AI features like **article summarization and contextual question answering**.

---

## 🚀 Features

📰 **News Aggregation**
Fetches the latest articles using RSS feeds (TechCrunch currently).

📖 **Full Article Reader**
Extracts full article content from external sources and displays it inside the website.

🤖 **AI Article Summarizer**
Generate a concise AI summary of any article using a local language model.

💬 **AI Chatbot for Articles**
Ask questions about the article and get intelligent responses based on its content.

🎨 **Modern UI**
Clean interface built with **TailwindCSS**.

---

## 🏗 Tech Stack

**Backend**

* Django
* Python

**AI / NLP**

* HuggingFace Transformers
* FLAN-T5 Language Model
* PyTorch

**Web Scraping**

* feedparser
* newspaper3k
* BeautifulSoup

**Frontend**

* TailwindCSS
* JavaScript (Fetch API)

---

## ⚙️ How It Works

```
RSS Feed
   ↓
News List
   ↓
Article Scraper
   ↓
Full Article Display
   ↓
AI Features
   ├── Summarize Article
   └── Ask AI Questions
```

The AI reads the article text and can generate summaries or answer questions based on the article context.

---

## 📦 Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-news-assistant.git
cd ai-news-assistant
```

Create a virtual environment:

```
python -m venv .venv
```

Activate it:

Windows:

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🤖 AI Model

The project uses the **FLAN-T5 Small model** from HuggingFace for:

* Article summarization
* Question answering about articles

The model downloads automatically on first run.

---

## 📸 Example Features

**AI Summary**

```
Click "Summarize Article"
→ AI generates a short summary of the news.
```

**AI Chat**

```
User: What happened in this article?
AI: The article discusses...
```

---

## 📂 Project Structure

```
ai-news-assistant
│
├── blog/                # Django project settings
├── news/                # Main application
│   ├── views.py
│   ├── scraper.py
│   ├── article_parser.py
│   ├── ai_utils.py
│
├── templates/           # HTML templates
├── requirements.txt
├── manage.py
└── README.md
```

---

## 💡 Future Improvements

* Multi-source news aggregation
* Sentiment analysis for articles
* AI topic classification
* User-specific news recommendations
* Deploy the AI model with GPU acceleration

---

## 👨‍💻 Author

**Aditya Parmar**

Built as a learning project exploring:

* AI-powered web applications
* Natural Language Processing
* Full-stack Django development
