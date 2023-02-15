from datetime import timedelta

from feast import FeatureView

from dataSources import callSource, sttSource, dogsSource, creditSource
from entities import call, clip, image, customer

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

dogsFeatures = FeatureView(
    name="dogs",
    description="dogs classifier features",
    entities=[image],
    ttl=timedelta(seconds=8640000000),
    online=False,
    source=dogsSource,
)

creditFeatures = FeatureView(
    name="credit",
    description="credit classifier features",
    entities=[customer],
    ttl=timedelta(seconds=8640000000),
    online=False,
    source=creditSource,
)