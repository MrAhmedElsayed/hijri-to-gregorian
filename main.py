import pathlib


class ConvertFromFile:
    """
    this class uses hijri-converter
    docs: https://hijri-converter.readthedocs.io/en/stable/
    """

    def __init__(self, file_dir):
        self.dates = []
        self.file_dir = file_dir
        self.allowed_files = [".xlsx", ".xls", ".csv", ".txt"]
        self.file_extension = self.specify_file_extension()
        self.outfile = ''

    def specify_file_extension(self):
        """Determine the file type from the file path"""
        ext = self.file_extension = pathlib.Path(self.file_dir).suffix
        return ext

    def get_dates(self):
        """
        read dates file (.xlsx, .xls, .csv, .txt)
        and excludes characters and standardizes date formats
        """
        if self.file_extension.lower() in self.allowed_files:
            if self.file_extension.lower() == '.txt':
                self.read_txt()

            if self.file_extension.lower() == '.csv':
                self.read_csv()

            if self.file_extension.lower() == '.xls' or self.file_extension.lower() == '.xlsx':
                self.read_excel()

    def hijri_to_gregorian(self):
        pass

    def gregorian_to_hijri(self):
        pass

    def read_txt(file):
        print("text file")

    def read_csv(file):
        print("csv file")

    def read_excel(file):
        print("excel file")


if __name__ == "__main__":
    conv = ConvertFromFile(
        r"C:\Users\Ahmed\Desktop\Github repositories clean up\python-convert-from-hijri-to-gregorian-and-vv\dates.csv")
    conv.specify_file_extension()
    print(conv.file_extension)
    conv.get_dates()
