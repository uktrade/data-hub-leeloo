import functools
import itertools
import os
from collections import namedtuple, OrderedDict
from logging import getLogger

import boto3

from django.apps import apps

from . import etl
from . import utils
from . import spec


logger = getLogger(__name__)


s3 = boto3.resource(
    's3',
    region_name='eu-west-2',
    aws_access_key_id=os.environ['CDMS_DUMP_S3_KEY_ID'],
    aws_secret_access_key=os.environ['CDMS_DUMP_S3_KEY'],
)
s3_bucket = s3.Bucket(os.environ['CDMS_DUMP_S3_BUCKET'])

model_deps = utils.fkey_deps(set(mapping.ToModel for mapping in spec.mappings))

def transform(mapping, data):
    for item in data:
        yield etl.transform(mapping, item)

for depth in list(model_deps.keys())[1:]:  # skip metadata
    for Model in model_deps[depth]:
        mapping = spec.get_mapping(Model)
        data = etl.extract(s3_bucket, mapping.from_entitytype)
        data_transformed = transform(mapping, data)
        for item in data_transformed:
            etl.load(mapping.ToModel, item)
