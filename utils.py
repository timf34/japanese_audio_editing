import os
from typing import List

def remove_spaces_from_files_in_dir(dir_path: str) -> None:
    """
        This function removes spaces from files in a directory.
    """
    files = os.listdir(dir_path)
    for file in files:
        new_file_name = file.replace(" ", "_")
        new_file_name = new_file_name.replace("-", "")
        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_file_name))


def files_in_directory(dir_path: str) -> List[str]:
    """
        This function returns a list of the paths to files in a directory.
    """
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

def main():
    remove_spaces_from_files_in_dir("audio_files")


if __name__ == '__main__':
    main()
