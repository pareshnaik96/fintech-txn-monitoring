import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class EnrichTransaction(beam.DoFn):
    def process(self, element):
        txn = json.loads(element)
        txn['risk_score'] = 0.8 if txn['amount'] > 10000 or txn['location'] in ['North Korea', 'Iran'] else 0.1
        txn['suspicious'] = txn['risk_score'] > 0.5
        yield txn

pipeline_options = PipelineOptions.from_dictionary({
    'streaming': True,
    'runner': 'DirectRunner'  # Change to DataflowRunner for GCP deployment
})

with beam.Pipeline(options=pipeline_options) as p:
    (p
     | 'ReadFromKafka' >> beam.io.ReadFromText('sample_kafka_input.json')
     | 'EnrichTransaction' >> beam.ParDo(EnrichTransaction())
     | 'WriteToJSON' >> beam.io.WriteToText('output/flagged', file_name_suffix=".json")
    )