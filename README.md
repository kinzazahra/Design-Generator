# 🏡 AI Home Designer – Smart Layout Generator

An innovative, AI-powered web application that acts as your **personal virtual architect**.
By leveraging the power of **Google's Gemini API**, this tool takes basic requirements like plot area and BHK configuration to generate **creative, optimized home design layouts** and structural suggestions in real-time.

✨ Built with creativity and AI by **Kinza Zahra**

---

## 🚀 Features

### 🤖 AI-Powered Design Generation

* Seamlessly integrates with **Google Generative AI (Gemini)**
* Generates intelligent:

  * Room allocations
  * Interior suggestions
  * Spatial planning layouts

### 🧾 Intuitive Input Parameters

* **Total Area** → e.g., `1000 sq ft`
* **BHK Configuration** → e.g., `1 BHK`, `2 BHK`, `3 BHK`

### ⚡ Real-Time Generation

* Instant AI-generated layouts
* No page reload required

### 🔐 Secure & Configurable

* Uses `.env` file for API key security
* Keeps sensitive data safe during development

### 🎨 Clean User Interface

* Minimal and responsive design
* Focused on smooth user experience

---

## 🛠 Tech Stack

| Layer    | Technology                        |
| -------- | --------------------------------- |
| Frontend | HTML5, CSS3, Vanilla JavaScript   |
| Backend  | Python (Flask)                    |
| AI       | Google Generative AI (Gemini API) |
| Security | python-dotenv                     |

---

## 📂 Project Structure

```plaintext
Design-Generator/
│
├── app.py              # Main Flask server and Gemini API logic
├── requirements.txt    # Python dependencies
├── .env                # API keys (not pushed to GitHub)
│
├── static/
│   ├── style.css       # UI styling
│   └── script.js       # Frontend logic & API calls
│
└── templates/
    └── index.html      # Main UI
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd Design-Generator
```

### 2️⃣ Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create or open the `.env` file and add:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

👉 Get your API key from **Google AI Studio**

---

### 4️⃣ Run the Application

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧑‍💻 How to Use

1. **Enter Details**

   * Input total property area
   * Select desired BHK configuration

2. **Click Generate**

   * Sends data to the AI

3. **View Results**

   * AI returns:

     * Room sizes
     * Layout suggestions
     * Design insights

---

## 🔮 Future Improvements

* 🖼️ AI-generated **2D/3D floor plans** (DALL·E / Midjourney integration)
* 📄 Export layouts as **PDF**
* 🧭 Add **Vastu / Feng Shui** compliance
* 🏗️ Support architectural styles:

  * Modern
  * Minimalist
  * Traditional

---

## ❤️ Credits

Made with love by **Kinza Zahra**
