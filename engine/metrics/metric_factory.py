from metrics.accuracy import AccuracyMetric


class MetricFactory:

    @staticmethod
    def get_metrics():

        return [

            AccuracyMetric()

        ]