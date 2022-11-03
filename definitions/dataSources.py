from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource

callSource = PostgreSQLSource(
    name="callSource",
    query="select call_data.id as id, closing_time as timestamp, round(extract(seconds from pickup_time-arrival_time)) as wait_duration, round(extract(seconds from closing_time-pickup_time)) as service_duration, is_happy from call_data inner join customer on customer.id=call_data.customer_id",
    timestamp_field="timestamp",
    description="callcenter logs"
)