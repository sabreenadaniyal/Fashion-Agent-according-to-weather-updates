# 👗 Weather-Based Fashion Stylist

## 📌 About the Project

This is a smart fashion assistant built with **Streamlit** and **AI (Gemini LLM)**. It gives outfit suggestions based on the **current weather** and your selected **event or occasion**. 
Whether it's a sunny gym day or a cloudy office morning, this tool will help you dress perfectly for the day.

---

## 🧠 What Can It Do?

* Check the **current weather** using the Open-Meteo API.
* Take your **city name** and **occasion** (like party, work, gym, etc.).
* Give you **AI-powered outfit suggestions** with style tips and emojis 👚👞👜.

---

## 🛠️ Technologies Used

* **Streamlit** – for creating the user interface
* **Python** – for backend logic
* **Gemini LLM** – for natural language AI responses
* **Open-Meteo API** – for getting real-time weather data
* **dotenv** – to safely load secret API keys

---

## 💡 How It Works

### 🧍 User Input

You enter:

* City (e.g., Karachi, Tokyo, London)
* Occasion (e.g., party, casual, work, gym)

### ☁️ Weather Tool

* The tool checks the weather using Open-Meteo based on your city (or defaults to Karachi).

### 🎨 AI Outfit Suggestions

* Gemini LLM understands both the weather and the occasion.
* It gives you outfit tips like:

  * "Wear a light cotton kurta if it's hot and you're going to a party."
  * "Choose layered outfits and boots if it's cold and formal."

---

## 🚀 How to Run

1. Clone the repo

```bash
git clone https://github.com/sabreenadaniyal/weather-fashion-stylist.git
```

2. Navigate into the folder

```bash
cd weather-fashion-stylist
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Add your API key to a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

5. Run the app

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
📦 weather-fashion-stylist
 ┣ 📜 app.py
 ┣ 📜 .env
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## 🤝 Credits

* Created by **Sabreena**
* Powered by **Gemini LLM** and **Open-Meteo**

---

## 🌐 Live Demo

Coming soon on Streamlit Share or Hugging Face 🤗

---

## 📬 Feedback

Found a bug or want to suggest a feature?
Create an issue or email at: `sabreenazahid04@gmail.com`

---

Stay trendy and smart — whatever the weather! ☀️🌧️☃️
