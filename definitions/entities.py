from feast import Entity

call = Entity(
    name="call",
    join_keys=["id"],
    description="call entity",
)