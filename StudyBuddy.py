import os
import re
import json
import pyttsx3
import speech_recognition as sr
from datetime import datetime, timedelta


class StudyBuddy:
    def __init__(self, notes_folder):
        self.notes_folder = notes_folder
        self.flashcards = []
        self.review_schedule = {}
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def parse_notes(self):
        print(f"Looking for Python files in: {self.notes_folder}")
        for filename in os.listdir(self.notes_folder):
            if filename.endswith(".py"):
                filepath = os.path.join(self.notes_folder, filename)
                print(f"Parsing file: {filename}")
                with open(filepath, "r") as file:
                    content = file.read()
                self.extract_flashcards(content, filename)
        if not self.flashcards:
            print("No flashcards were generated. Check your .py files.")

    def extract_flashcards(self, content, filename):
        """Extract function definitions and comments as flashcards."""
        functions = re.findall(r"def\s+(\w+)\((.*?)\):", content)
        docstrings = re.findall(r'\"\"\"(.*?)\"\"\"', content, re.DOTALL)

        if not functions:
            print(f"No functions found in {filename}.")
        for i, func in enumerate(functions):
            question = f"What does the function {func[0]}({func[1]}) do?"
            answer = docstrings[i] if i < len(docstrings) else "No description provided."
            self.flashcards.append({"filename": filename, "question": question, "answer": answer})
            print(f"Generated flashcard - Question: {question}, Answer: {answer}")

    def spaced_repetition_schedule(self):
        now = datetime.now()
        print("\nSpaced Repetition Schedule:")
        print(f"{'Flashcard Question':<50} | {'Review Date':<20}")
        print("-" * 75)
        for i, flashcard in enumerate(self.flashcards):
            review_time = now + timedelta(days=2**i)  # Exponential spacing
            self.review_schedule[flashcard["question"]] = review_time
            print(f"{flashcard['question']:<50} | {review_time.strftime('%Y-%m-%d %H:%M:%S')}")


    def save_flashcards(self, output_file):
        """Save flashcards to a JSON file."""
        with open(output_file, "w") as file:
            json.dump(self.flashcards, file, indent=4)
        print(f"Flashcards saved to {output_file}")

    def review_flashcards(self):
        """Review flashcards due today."""
        print("\nReviewing Flashcards:")
        today = datetime.now()
        due_flashcards = [q for q, t in self.review_schedule.items() if t.date() <= today.date()]

        if not due_flashcards:
            print("No flashcards are due for review today.")
            return

        for question in due_flashcards:
            self.text_to_speech(question)
            print(f"Question: {question}")
            input("Press Enter to reveal the answer...")
            answer = next(flashcard["answer"] for flashcard in self.flashcards if flashcard["question"] == question)
            print(f"Answer: {answer}\n")
            self.text_to_speech(answer)

    def text_to_speech(self, text):
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def speech_to_text(self):
        """Recognize speech input for flashcard interaction."""
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Speech recognition service is unavailable.")


# Example usage
if __name__ == "__main__":
    notes_folder = "./class_notes"
    output_file = "flashcards.json"

    # Ensure the notes folder exists
    if not os.path.exists(notes_folder):
        print(f"The folder '{notes_folder}' does not exist. Creating it now...")
        os.makedirs(notes_folder)

    study_buddy = StudyBuddy(notes_folder)

    print("Parsing notes...")
    study_buddy.parse_notes()

    print("\nGenerating spaced repetition schedule...")
    study_buddy.spaced_repetition_schedule()

    print(f"\nSaving flashcards to {output_file}...")
    study_buddy.save_flashcards(output_file)

    print("\nReviewing flashcards...")
    study_buddy.review_flashcards()
