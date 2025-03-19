# from TTS.api import TTS

# # Initialize the TTS model
# # Replace "tts_models/en/ljspeech/tacotron2-DDC" with any available model from Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# # Define the text you want to convert to speech
# text = "Hello, this is a test of the Coqui Text-to-Speech engine."

# # Generate speech and save it to a file
# output_path = "coqui_tts_output.wav"
# tts.tts_to_file(text=text, file_path=output_path)

# print(f"Speech synthesis complete. The audio has been saved to {output_path}.")


import time
from TTS.api import TTS
from playsound import playsound
import os

# Initialize the TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# Define the meditation script
script = {
    "phrases": [
        {"text": "Welcome to this Breath Awareness Meditation.", "pause": 10000},
        {"text": "Find a comfortable position, sitting or lying down.", "pause": 10000},
        {"text": "Close your eyes gently and take a deep breath in.", "pause": 10000},
        # {"text": "Hold that breath for a moment.", "pause": 10000},
        # {"text": "Now, exhale slowly and fully.", "pause": 10000},
        # {"text": "With each breath, allow yourself to relax deeper.", "pause": 10000},
        # {"text": "Focus on the sensation of your breath entering and leaving your body.", "pause": 10000},
        # {"text": "As thoughts arise, gently acknowledge them and return your focus to your breath.", "pause": 10000},
        # {"text": "Breathe in calm, and breathe out tension.", "pause": 10000},
        # {"text": "You are capable and competent.", "pause": 10000},
        # {"text": "Continue this rhythm, in and out, at your own pace.", "pause": 10000},
        # {"text": "As you breathe, visualize a calming light surrounding you.", "pause": 10000},
        # {"text": "Feel this light washing over you, bringing peace and clarity.", "pause": 10000},
        # {"text": "When you're ready, start to bring your awareness back to the room.", "pause": 10000},
        # {"text": "Wiggle your fingers and toes gently.", "pause": 10000},
        # {"text": "Open your eyes slowly, returning to the present moment.", "pause": 10000},
        # {"text": "Thank you for taking this time to nurture yourself.", "pause": 10000},
    ]
}

# Directory to save the audio files
output_dir = "meditation_audio"
os.makedirs(output_dir, exist_ok=True)

# Process each phrase in the script
for i, phrase in enumerate(script["phrases"]):
    text = phrase["text"]
    pause = phrase["pause"] / 1000  # Convert pause to seconds
    output_file = os.path.join(output_dir, f"phrase_{i+1}.wav")
    
    # Generate speech for the phrase
    tts.tts_to_file(text=text, file_path=output_file)
    print(f"Generated speech for: {text}")
    
    # Play the audio file
    playsound(output_file)
    print(f"Played: {output_file}")
    
    # Pause after the phrase
    time.sleep(pause)

print("Meditation audio playback complete.")
