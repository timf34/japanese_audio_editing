import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

PATH_TO_AUDIO = "audio_files/sound.m4a"

# Load your audio.
sound = AudioSegment.from_file(PATH_TO_AUDIO, format="m4a")

# Split the audio file on silence.
audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-40)
print("here are the audio chunks: ", audio_chunks)

# Loop over the chunks and export them.
for i, chunk in enumerate(audio_chunks):
    out_file = f"chunk{i}.wav"
    print("exporting", out_file)
    chunk.export(out_file, format="wav")

print("I think we are done:)")

