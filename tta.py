from gtts import gTTS
from googletrans import Translator
import os

# Initialize the translator
translator = Translator()

# Get text input from the user
text = input("Enter the text you want to convert to speech: ")

# Get language input from the user
language = input("Enter the language code (e.g., 'en' for English, 'hi' for Hindi, 'fr' for French, 'mr' for Marathi, 'de' for German): ")

# Detect the language of the input text
detected_language = translator.detect(text).lang

# Translate the text if the input language is different from the output language
if detected_language != language:
    translated_text = translator.translate(text, src=detected_language, dest=language).text
else:
    translated_text = text

# Print the translated text
print(f"Translated text ({language}): {translated_text}")

# Create a gTTS object
tts = gTTS(text=translated_text, lang=language, slow=False)

# Save the audio file
tts.save("output.mp3")

# Play the audio file (works on most systems)
os.system("start output.mp3")  # For Windows
# os.system("afplay output.mp3")  # For macOS
# os.system("mpg321 output.mp3")  # For Linux
