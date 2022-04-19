import streamlit as st
from src.logger.schema import schema
from src.utils.get_secrets import get_gcp_secrets
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime


class EventLogging:

    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_info(
            get_gcp_secrets('https://viz-wizard.vault.azure.net/')
        )
        self.client = bigquery.Client(credentials=self.credentials)
        self.project_id = 'viz-wizard'
        self.dataset_name = f'{self.project_id}.app_logging'
        self.dataset: bigquery.Dataset = self._create_logging_dataset()
        self.table: bigquery.Table = self._create_events_table()

    def log_generated_charts(self, chart_type: str):

        date_time = datetime.now()
        row = self.client.insert_rows(self.table, [dict(event_name="chart generation",
                                                        event_info=[dict(key="chart type", value=chart_type)],
                                                        datetime=date_time
                                                        )
                                                   ]
                                      )

        return row

    def _create_logging_dataset(self) -> bigquery.Dataset:
        logging_dataset = bigquery.Dataset(self.dataset_name)
        generate_dataset = self.client.create_dataset(logging_dataset, exists_ok=True)
        return generate_dataset

    def _create_events_table(self) -> bigquery.Table:
        logging_table = bigquery.Table(f"{self.project_id}.app_logging.events", schema=schema)
        generate_table = self.client.create_table(logging_table, exists_ok=True)
        return generate_table
