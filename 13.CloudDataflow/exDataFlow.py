from __future__ import print_function
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

pipeline_options = PipelineOptions(
    project ='mysecont',
    runner = 'dataflow',
    temp_location = 'gs://dataflow-sample-test/temp',
    region = 'asia-northeast3'
)

with beam.Pipeline(options = pipeline_options) as p:
    p | 'Read' >> beam.io.ReadFromText("gs://dataflow-sample-test/UptownFunk.txt") \
        | 'Extract' >> beam.FlatMap(lambda s: re.split("\\W+", s)) \
        | 'Count' >> beam.combiners.Count.PerElement() \
        | 'Map' >> beam.Map(lambda w: "%s: %d" % w) \
        | 'Save' >> beam.io.textio.WriteToText("gs://dataflow-sample-test/input1.txt")

