from src.load.file_loader import FileLoader
from src.interface.homepage import HomePageSetup

home = HomePageSetup()
file_loader = FileLoader()

home.setup_home()
file_loader.read_as_dataframe()
