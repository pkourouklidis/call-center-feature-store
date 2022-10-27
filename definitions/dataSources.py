from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource

callSource = PostgreSQLSource(
    name="callSource",
    query="select id, arrival_time as timestamp, round(extract(seconds from pickup_time-arrival_time)) as waitDuration, round(extract(seconds from closing_time-pickup_time)) as serviceDuration from call_data",
    timestamp_field="timestamp",
    description="callcenter logs"
)