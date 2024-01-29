import os
class FileExtension:
    @staticmethod
    def get_file_extension(file_path):
        if file_path:
            return os.path.splitext(file_path)[1][1:].upper()
        return None