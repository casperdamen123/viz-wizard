# The Viz Wizard
Got some ugly flat data? And no idea know how to generate valuable insights from this flat data?

No problem, the Viz Wizard is here to provide you with some visualization magic

<img src="src/images/wiz_charts.png" alt="drawing" width="300"/>

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
managed using [Poetry](https://python-poetry.org/). A Dockerfile is provided to run the application as a 
[Docker](https://www.docker.com/) container.

### Poetry
If you would like to run the app locally, one easy option to install the dependencies would be to leverage Poetry:
- Install poetry using the [official instructions](https://python-poetry.org/docs/#installation)
- `poetry install` to create virtual environment and install requirements

### Streamlit
After installing the dependencies you can run the app locally using:
- `streamlit run main.py` 

### Docker
Another option is to use a Docker container to run the app:
- `docker build -f Dockerfile -t viz-wizard:latest .` to build container
- `docker run -p 80:80 --name viz-wizard viz-wizard:latest` to run container
