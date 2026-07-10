from metrics.metric_factory import MetricFactory
from models.evaluation_summary import EvaluationSummary


class MetricEngine:

    PASS_SCORE = 100
    REVIEW_SCORE = 70
    FAIL_SCORE = 40
    
    
    def evaluate(self, expected_answer, generated_answer):

        metrics = MetricFactory.get_metrics()

        result = {}

        for metric in metrics:

            metric_result = metric.calculate(
                expected_answer,
                generated_answer
            )

            result[
                metric_result["metric"].lower()
            ] = metric_result

        return result
        
    def calculate_overall_score(self, metric_results):

        if not metric_results:

            return 0

        total = 0

        count = 0

        for metric in metric_results.values():

            total += metric["score"]

            count += 1

        return round(total / count)  



    def determine_status(self, confidence):

        if confidence >= 90:

            return "PASS"

        elif confidence >= 70:

            return "REVIEW"

        return "FAIL"    



    def calculate(self, results):

        total = len(results)

        pass_count = 0
        review_count = 0
        fail_count = 0

        confidence_total = 0
        latency_total = 0
        weighted_score = 0

        for result in results:

            confidence_total += result.confidence
            latency_total += result.latency_ms

            if result.status == "PASS":

                pass_count += 1
                weighted_score += self.PASS_SCORE

            elif result.status == "REVIEW":

                review_count += 1
                weighted_score += self.REVIEW_SCORE

            else:

                fail_count += 1
                weighted_score += self.FAIL_SCORE

        overall_score = (
            round(weighted_score / total, 2)
            if total else 0
        )

        average_confidence = (
            round(confidence_total / total, 2)
            if total else 0
        )

        average_latency = (
            round(latency_total / total, 2)
            if total else 0
        )

        if overall_score >= 95:
            quality_rating = "Excellent"
        elif overall_score >= 85:
            quality_rating = "Good"
        elif overall_score >= 70:
            quality_rating = "Fair"
        else:
            quality_rating = "Needs Improvement"

        return EvaluationSummary(

            total_questions=total,

            pass_count=pass_count,

            review_count=review_count,

            fail_count=fail_count,

            overall_score=overall_score,

            average_confidence=average_confidence,

            average_latency=average_latency,

            quality_rating=quality_rating

        )
