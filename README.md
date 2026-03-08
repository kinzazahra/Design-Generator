                                AI Home Designer – Smart Layout Generator
An innovative, AI-powered web application that acts as your personal virtual architect. By leveraging the power of Google's Gemini API, this tool takes basic requirements like plot area and BHK configuration to generate creative, optimized home design layouts and structural suggestions in real-time.

Built with creativity and AI by Kinza Zahra 🏡✨

Features
AI-Powered Design Generation: Integrates seamlessly with the Google Generative AI (Gemini) to produce intelligent and highly customized room allocations, interior suggestions, and spatial planning.

Intuitive Input Parameters:

Total Area: Input your plot or flat size (e.g., 1000 sq ft).

BHK Configuration: Specify your requirement (e.g., 1 BHK, 2 BHK, 3 BHK) to get tailored results.

Real-Time Generation: Watch the AI draft your home layout concepts dynamically without needing to reload the page.

Secure & Configurable: Uses environment variables (.env) to keep your API keys secure during development.

Clean User Interface: A minimal, responsive frontend design that focuses entirely on delivering a smooth user experience.

🛠 Tech Stack
Frontend: HTML5, CSS3, Vanilla JavaScript.

Backend: Python (Flask Framework).

AI Integration: google-generativeai (Gemini API) for natural language layout generation.

Security: python-dotenv for local environment variable management.

📂 Project Structure
Plaintext
Design-Generator/
│
├── app.py              # Main Flask server and Gemini API logic
├── requirements.txt    # Python library dependencies
├── .env                # Secret environment variables (API Keys)
│
├── static/             # Frontend assets
│   ├── style.css       # Clean, modern UI styling
│   └── script.js       # Form handling and asynchronous API calls
│
└── templates/          # HTML Views
    └── index.html      # Main user interface for the AI Designer
⚙️ Installation & Setup
Clone the Repository:

Bash
git clone <your-repo-url>
cd Design-Generator
Install Dependencies:
Ensure you have Python installed, then run:

Bash
pip install -r requirements.txt
(This will install Flask, google-generativeai, and python-dotenv).

Configure the Environment:

Open the .env file in the root directory.

Add your Google Gemini API key:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
(Get your free key from Google AI Studio).

Run the Application:

Bash
python app.py
Open your browser and navigate to the local server, typically http://127.0.0.1:5000.

🚀 How to Use
Enter Details: Type in the total area of your property and select the desired number of bedrooms/halls/kitchens (BHK).

Generate: Click the "Generate" button to send your parameters to the AI.

Review Design: The Gemini model will process your constraints and return a detailed, text-based architectural breakdown of room sizes, placements, and design tips.

🔮 Future Improvements
Integration with an Image Generation AI (like Midjourney or DALL-E) to produce visual 2D/3D floor plans.

Export functionality to save the generated layout details as a PDF.

More granular inputs (e.g., Vastu/Feng Shui compliance, specific architectural styles like "Modern" or "Minimalist").

Made with ❤️ by Kinza Zahra
