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
[Docker](https://www.docker.com/) container. [Bicep files](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep) and [Azure pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-get-started?view=azure-devops) files can be found in the infra module to deploy the application using Azure cloud resources

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
- `docker run -p 8501:8501 --name viz-wizard viz-wizard:latest` to run container

### Azure resources
To deploy the needed resources on Azure, run the following command using the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/)
- `az deployment sub create --template-file infra/main.bicep --location 'eastus' --parameters environmentType=prod dockerImagePushed=False`

Upon prompt you are asked for admin password for the SQL server.

After the initial deployment of resources, connect the azure-pipelines.yml file to your Devops account. This pipeline will build and push the docker image to the Azure Container Registry. Before running the pipeline it is important to configure the Azure Service Connection and Docker Registry Service Connection in Devops. Instructions on configuring the service connection can be found [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml)

When the image is build and pushed, you can run the command from above but this time use `dockerImagePushed=True`. The admin password for the SQL database will change again and afterwards your web app should be deployed!!

After updating the docker image, and pushing it using the Azure pipeline, it's advised to restart the web app in the Azure UI to load the new image. Restarting may take a while as the image will be pulled again from the registry.