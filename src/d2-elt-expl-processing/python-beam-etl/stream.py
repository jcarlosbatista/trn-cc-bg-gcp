# https://cloud.google.com/dataflow/docs/guides/deploying-a-pipeline
# PCollection =
# PTransform =
# ParDo = Generic Parallel Processing

# import libraries
import argparse
import json
import os
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

# set logging basics
logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)

# service account key path
# topic = src-py-app-users-events-json
# subscription = df-beam-py-etl
# tables = enriched-user-events
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/luanmorenomaciel/Credentials/silver-charmer-243611-9552f50e9d25.json"
PUB_SUB_SUBSCRIPTION = "projects/silver-charmer-243611/subscriptions/df-beam-py-etl"
BIGQUERY_TABLE = "silver-charmer-243611.OneWaySolution.enriched-user-events"
BIGQUERY_SCHEMA = "id:INTEGER,first_name:STRING,last_name:STRING,gender:STRING,race:STRING,language:STRING,email:STRING,ssn:STRING,user_id:INTEGER,dt_current_timestamp:STRING"

# message body
"""
{
   "id":1,
   "first_name":"Gerick",
   "last_name":"Risley",
   "gender":"Male",
   "race":"Aleut",
   "language":"Korean",
   "email":"grisley0@washington.edu",
   "ssn":"762-14-3270",
   "user_id":190303,
   "dt_current_timestamp":"2022-11-08 13:27:24.683445"
}
"""


class CustomParsing(beam.DoFn):
    """ custom [paralleldo] class to apply a custom transformation """

    def process(self, element: bytes, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        """
        simple processing function to parse the data and add a timestamp for additional params see:
        https://beam.apache.org/releases/pydoc/2.7.0/apache_beam.transforms.core.html#apache_beam.transforms.core.DoFn
        """
        parsed = json.loads(element.decode("utf-8"))
        print(parsed)
        # parsed["timestamp"] = timestamp.to_rfc3339()
        yield parsed


# main function
def run():
    # init parser
    parser = argparse.ArgumentParser()

    # 1 = request pubsub subscription
    parser.add_argument(
        "--input_subscription",
        help='input pubSub subscription of the form "projects/<PROJECT>/subscriptions/<SUBSCRIPTION>."',
        default=PUB_SUB_SUBSCRIPTION,
    )

    # 2 = table on bigquery
    parser.add_argument(
        "--output_table", help="output bigQuery table", default=BIGQUERY_TABLE
    )

    # 3 = defined schema
    parser.add_argument(
        "--output_schema",
        help="output bigQuery schema in text format",
        default=BIGQUERY_SCHEMA,
    )

    # receive args
    known_args, pipeline_args = parser.parse_known_args()

    # creating pipeline options
    # set streaming for pub/sub
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(StandardOptions).streaming = True

    # define pipeline = dag
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | "ReadFromPubSub" >> beam.io.gcp.pubsub.ReadFromPubSub(
                subscription=known_args.input_subscription, timestamp_attribute=None
            )
            | "EnrichEvents" >> beam.ParDo(CustomParsing())
            | "WriteToBigQuery" >> beam.io.WriteToBigQuery(
                known_args.output_table,
                schema=known_args.output_schema,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            )
        )


# execute pipeline
if __name__ == "__main__":
    run()