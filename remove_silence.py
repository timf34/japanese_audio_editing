from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

from typing import List


def files_in_directory(dir_path: str) -> List[str]:
    """
        This function returns a list of the paths to files in a directory.
    """
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]


def chcek_files_in_directory():
    dir_path = "audio_files"
    print("files in directory: ", files_in_directory(dir_path))


def remove_silence(audio_file_path: str, output_dir: str):
    """
        This function takes an audio file path and removes the silence from the audio file.
        It then saves the audio file in the output directory.
    """
    # Load your audio.
    sound = AudioSegment.from_file(f"audio_files/{audio_file_path}", format="m4a")

    # Split the audio file on silence.
    audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-40)

    if len(audio_chunks) == 0:
        print(f"No audio chunks found in {audio_file_path}")
        return

    # Remove directory from audio_file_path
    audio_file_name = audio_file_path.split("/")[-1].replace(".m4a", "")

    # Loop over the chunks and export them.
    for i, chunk in enumerate(audio_chunks):
        # Convert chunk from stereo to mono
        chunk = chunk.set_channels(1)
        out_file = f"edited_audio_files/{audio_file_name}_{i}.wav"
        chunk.export(out_file, format="wav")
        print(f"exported {out_file} to {output_dir}")


def convert_from_wav_to_mp3():
    """
        This function converts all the wav files in a directory to mp3 files.
    """
    file_paths = files_in_directory("edited_audio_files")
    for file_path in file_paths:
        sound = AudioSegment.from_file(f"edited_audio_files/{file_path}", format="wav")
        sound.export(f"edited_audio_files/{file_path.replace('.wav', '.mp3')}", format="mp3")


def main():
    # file_paths = files_in_directory("audio_files")
    # for file_path in file_paths:
    #     remove_silence(file_path, "output")
    convert_from_wav_to_mp3()


if __name__ == '__main__':
    main()
