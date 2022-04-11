from google.cloud import bigquery

schema = [
    bigquery.SchemaField(
        "event_name",
        "STRING",
        mode="required",
        description="Name of the event"
    ),
    bigquery.SchemaField(
        "event_info",
        "RECORD",
        mode="REPEATED",
        description="Event details",
        fields=[
            bigquery.SchemaField("key",
                                 "STRING",
                                 mode="required",
                                 description="Event key"
                                 ),
            bigquery.SchemaField("value",
                                 "STRING",
                                 mode="NULLABLE",
                                 description="Event value"
                                 ),
        ],
    ),
    bigquery.SchemaField(
        "datetime",
        "DATETIME",
        mode="required",
        description="Datetime of event"
    )
]
