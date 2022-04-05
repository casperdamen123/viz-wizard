# The Viz Wizard
Got some ugly flat data? And no idea know how to generate valuable insights from this flat data? 

No problem, the Viz Wizard is here to provide you with some visualization magic

![alt text](src/images/wiz_charts.png)

## General instructions

### Upload your data
Provide the wizard with your own data file
- `csv`: Comma separated format
- `xlsx`: Excel tabular file
- `txt`: Text file with tab separation

### Validate tabular format
Check the data preview to see if data is loaded correctly. The minimum requirements of the dataset are:
- At least 3 numeric columns
- At least 2 text/string columns

### Generate visualizations 
Leverage the Wiz Magic by clicking on the Viz Magic button, the wizard will generate random visualization for you.

## Technical details
This application was build using [Streamlit](https://streamlit.io/). Python package dependencies are 
managed using [Poetry](https://python-poetry.org/).

### Poetry
- Install poetry using the [official instructions](https://python-poetry.org/docs/#installation)
- Use `poetry install` to create virtual environment and install requirements

## Streamlit
- Use `streamlit run main.py` to deploy application locally
