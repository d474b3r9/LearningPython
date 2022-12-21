import zipfile
import pathlib


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:\\Users\\jonito\\PycharmProjects\\LearningPython\\Python_Mega_course\\APPS\\archive extractor\\compressed.zip",dest_dir="C:\\Users\\jonito\\PycharmProjects\\LearningPython\\Python_Mega_course\\APPS\\archive extractor")
