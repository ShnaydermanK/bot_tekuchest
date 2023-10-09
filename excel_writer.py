import pandas as pd

class ExcelWriter:
    def __init__(self, file_path):
        self.writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

    def save_and_close(self):
        self.writer.book.close()
