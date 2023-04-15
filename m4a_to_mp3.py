"""This function converts files from m4a to mp3."""

import os
import subprocess

from pydub import AudioSegment
from utils import files_in_directory


def ffmpeg_convert_from_m4a_to_mp3(directory: str = "NewFOVAudioFiles") -> None:
    """
        This function converts all the m4a files in a directory to mp3 files.

        Note: I get permission errors with this!
    """
    file_paths = files_in_directory(f"{directory}")
    for file_path in file_paths:
        subprocess.call(["ffmpeg", "-i", f"{directory}/{file_path}", f"/{file_path.replace('.m4a', '.mp3')}"])


def convert_m4a_to_mp3(directory: str = "NewFOVAudioFiles") -> None:
    # Create a subdirectory called "edited" to save the converted files
    edited_dir = os.path.join(directory, "edited")
    os.makedirs(edited_dir, exist_ok=True)

    # Get all m4a files in the directory
    m4a_files = [f for f in os.listdir(directory) if f.endswith('.m4a')]

    for m4a_file in m4a_files:
        # Open the m4a file with pydub
        sound = AudioSegment.from_file(os.path.join(directory, m4a_file), format="m4a")

        # Create a new file name with mp3 extension
        mp3_file = os.path.splitext(m4a_file)[0] + '.mp3'

        # Export the sound to mp3 format and save it in the edited directory
        sound.export(os.path.join(edited_dir, mp3_file), format="mp3")


def main():
    convert_m4a_to_mp3()


if __name__ == '__main__':
    main()
