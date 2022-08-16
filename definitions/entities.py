from feast import (
    Entity,
    ValueType,
)

call = Entity(
    name="call",
    join_keys=["callID"],
    description="call id",
)