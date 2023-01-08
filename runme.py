from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)
# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
#wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# Text to speech to a file
#tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")

# Running a single speaker model
# Open the file in read mode
with open('file.txt', 'r') as file:
  # Read the contents of the file into a list of strings
  file_contents = file.read()


OUTPUT_PATH = "Spoken_Outpu_1.wav"

# Init TTS with the target model name
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=True, gpu=True)
# Run TTS
tts.tts_to_file(text=file_contents, file_path=OUTPUT_PATH)
