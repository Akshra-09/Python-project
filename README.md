#  Jarvis - Python Voice Assistant

##  About the Project

Jarvis is a Python-based personal voice assistant developed to automate common computer tasks using voice commands.

The project combines speech recognition, text-to-speech, browser automation and API-based information retrieval to create an interactive assistant.

## Motivation

I built Jarvis to apply my Python programming knowledge to a practical project and understand how multiple Python libraries and APIs can be integrated into a single application.

##  Features

-  Voice command input
-  Text-to-speech responses
- Opens websites using voice commands
- Plays music based on user commands
-  Retrieves news through an API
-  Performs automated computer tasks
-  Handles user commands using Python logic

##  Technologies Used

- **Python**
- **SpeechRecognition** ” speech-to-text
- **PyAudio** ” microphone/audio input
- **pyttsx3** ” text-to-speech
- **Webbrowser** ” browser automation
- **News API** ” news retrieval
- Python modules and functions for organizing the application

##  How It Works

```text
User speaks
     â†“
Microphone captures voice
     â†“
SpeechRecognition processes the command
     â†“
Jarvis identifies the requested task
     â†“
Corresponding Python function is executed
     â†“
Jarvis responds using text-to-speech
```

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Akshra-09/Python-project.git
```

### 2. Open the project

```bash
cd Python-project
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project folder and add your API keys there.

Example:

```text
OPENAI_API_KEY=your_key_here
```

Do **not** upload the `.env` file to GitHub.

### 6. Run Jarvis

```bash
python main.py
```

## What I Learned

Through this project, I learned how to:

- Work with external Python libraries
- Integrate multiple components into one application
- Work with APIs
- Handle voice input and audio output
- Debug errors during development
- Organize Python code into modules
- Build a practical application rather than isolated coding exercises

##  Future Improvements

Possible future improvements include:

- More natural language command processing
- Better error handling
- Improved modular code structure
- A graphical user interface
- More personalized commands
- Integration with an AI/LLM system
- Support for a wider range of tasks

## » Author

**Akshra Jain**

B.Tech Bioinformatics Student
Amity University Rajasthan

GitHub: [Akshra-09](https://github.com/Akshra-09)
