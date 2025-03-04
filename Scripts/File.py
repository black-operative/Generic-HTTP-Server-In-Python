class File_Reader:
    def __init__(self) -> None:
        self.__file_path__   = None
        
    def set_file_path(self, file_path : str) -> None:
        self.__file_path__ = file_path
        
    def read_file(self) -> str:
        if not self.__file_path__:
            return """"""
        try:
            with open(self.__file_path__, 'r', encoding='utf-8') as file:
                return file.read()
            
        except FileNotFoundError:
            print("File not found")
            return """"""

        