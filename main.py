from src.load.file_loader import FileLoader
from src.template.homepage import HomePageSetup
from src.validate.data_validation import DataValidation
from src.visualize.charts import DataViz

# Setup template for homepage
home = HomePageSetup()
home.setup_home()

# Provide file uploader, save as pandas dataframe
file_loader = FileLoader()
df = file_loader.read_as_dataframe()

# Perform data requirement checks
data_validation = DataValidation(df)
validation_result = data_validation.validate_data()

# Generate visualization
if validation_result == True:
    data_viz = DataViz(df)
    data_viz.show_random_viz()
