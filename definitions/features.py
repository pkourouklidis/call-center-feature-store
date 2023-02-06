from datetime import timedelta

from feast import FeatureView

from dataSources import callSource, sttSource
from entities import call, clip

#Feature view
callcenterFeatures = FeatureView(
    name="callcenter",
    description="callcenter features",
    entities=[call],
    ttl=timedelta(seconds=8640000000),
    online=False,
    source=callSource,
)

sttFeatures = FeatureView(
    name="stt",
    description="speech to text features",
    entities=[clip],
    ttl=timedelta(seconds=8640000000),
    online=False,
    source=sttSource,
)