from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    PostgreSQLSource,
)

callSource = PostgreSQLSource(
    name="callSource",
    query="select call_data.id as id, closing_time as timestamp, round(extract(seconds from pickup_time-arrival_time)) as wait_duration, round(extract(seconds from closing_time-pickup_time)) as service_duration, is_solved::int, is_happy::int, is_predicted_to_be_happy::int as happiness_prediction from call_data inner join customer on customer.id=call_data.customer_id",
    timestamp_field="timestamp",
    description="callcenter logs",
)

sttSource = PostgreSQLSource(
    name="sttSource",
    query="select id, ts as timestamp, input, prediction, label from stt",
    timestamp_field="timestamp",
    description="speech to text logs",
)

dogsSource = PostgreSQLSource(
    name="dogsSource",
    query="select id, ts as timestamp, input as dog_input, prediction as dog_prediction, label as dog_label from dogs",
    timestamp_field="timestamp",
    description="Dogs image classification data",
)