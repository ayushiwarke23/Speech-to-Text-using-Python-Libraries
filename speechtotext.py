import speech_recognition as sr

def transcribe_from_file(file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Processing WAV audio file...")
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        print("\nTranscribed Text:")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    file_path = input("Enter WAV audio file path: ").strip().strip('\"\'')
    transcribe_from_file(file_path)
