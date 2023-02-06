from feast import Entity

call = Entity(
    name="call",
    join_keys=["id"],
    description="call entity",
)

clip = Entity(
    name = "clip",
    join_keys=["id"],
    description="voice clip for speech to text"
)