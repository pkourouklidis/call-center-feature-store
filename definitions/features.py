from datetime import timedelta

from feast import FeatureView

from dataSources import callLogs
from entities import call

#Feature view
callFeatures = FeatureView(
    name="callFeatures",
    description="call features",
    entities=[call],
    ttl=timedelta(seconds=8640000000),
    online=False,
    source=callLogs,
)