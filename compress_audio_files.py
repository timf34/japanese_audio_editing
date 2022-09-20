import pydub

from utils import files_in_directory


def compress_audio_file(path: str) -> None:
    """
        This function compresses an audio file.
    """
    sound = pydub.AudioSegment.from_file(f"{path}", format="mp3")
    path = path.replace("audio_files_to_be_compressed/", "")
    sound.export(f"compressed_audio_files/{path}", format="mp3", bitrate="64k")

# TODO: I need a cleaner way to manage all of the different directories


def main():
    file_paths = files_in_directory("audio_files_to_be_compressed")
    for file_path in file_paths:
        compress_audio_file(f"audio_files_to_be_compressed/{file_path}")


if __name__ == '__main__':
    main()
