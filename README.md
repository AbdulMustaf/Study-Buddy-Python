# StudyBuddy

## Overview
**StudyBuddy** is a Python-based tool designed to help users enhance their learning experience by generating flashcards from Python code files. It automatically extracts function definitions, docstrings, and comments to create flashcards, employs spaced repetition for efficient review, and integrates text-to-speech functionality for auditory reinforcement.

---

## Features

### 1. Flashcard Generation
- Extracts function names and docstrings from `.py` files in the specified folder.
- Automatically creates flashcards with questions and answers.

### 2. Spaced Repetition
- Implements an exponential review schedule to enhance long-term memory retention.
- Dynamically schedules flashcards based on their review history.

### 3. Text-to-Speech (TTS)
- Reads questions and answers aloud for auditory learners.
- Utilizes `pyttsx3` for offline speech synthesis.

### 4. Speech Recognition
- Allows users to interact with flashcards using voice commands.
- Uses `speech_recognition` for real-time voice input.

### 5. File Operations
- **Parse Notes**: Reads Python files in the specified directory to generate flashcards.
- **Save Flashcards**: Saves flashcards as a JSON file for future use.
- **Review Flashcards**: Reviews flashcards due for the current day.

---

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - `pyttsx3`
  - `speech_recognition`
  - `datetime`
  - `re`
  - `json`

Install the dependencies using:
```bash
pip install pyttsx3 SpeechRecognition
