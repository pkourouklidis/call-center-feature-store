from datetime import timedelta

from feast import FeatureView

from dataSources import callSource
from entities import call

#Feature view
callcenterFeatures = FeatureView(
    name="callcenter",
    description="callcenter features",
    entities=[call],
    ttl=timedelta(seconds=8640000000),
    online=False,
    source=callSource,
)