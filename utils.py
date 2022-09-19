import os


def remove_spaces_from_files_in_dir(dir_path: str) -> None:
    """
        This function removes spaces from files in a directory.
    """
    files = os.listdir(dir_path)
    for file in files:
        new_file_name = file.replace(" ", "_")
        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_file_name))


def main():
    remove_spaces_from_files_in_dir("audio_files")


if __name__ == '__main__':
    main()
