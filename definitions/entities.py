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

image = Entity(
    name = "image",
    join_keys=["id"],
    description="input image for dog classifier"
)

customer = Entity(
    name= "customer",
    join_keys=["id"],
    description="credit classification customer"
)