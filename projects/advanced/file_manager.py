class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        with open(self.filename, "w") as file:
            file.write(content)
        return True

    def read_file(self):
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            return None

    def delete_file(self):
        import os

        if os.path.exists(self.filename):
            os.remove(self.filename)
            return True
        return False