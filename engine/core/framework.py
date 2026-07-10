from core.framework_context import FrameworkContext

from evaluators.evaluator_factory import EvaluatorFactory

from datasets.dataset_loader import DatasetLoader

from metrics.metric_engine import MetricEngine

from data_generators.summary_json_generator import SummaryJsonGenerator
from data_generators.evaluation_results_generator import EvaluationResultsGenerator

from report_generators.executive_report_generator import ExecutiveReportGenerator
from report_generators.detailed_report_generator import DetailedReportGenerator
from knowledge_sources.knowledge_source_processor import KnowledgeSourceProcessor

class EnterpriseAIQualityFramework:

    def __init__(self):

        self.context = FrameworkContext()

        self.config_loader = self.context.get_config_loader()

        self.evaluator = EvaluatorFactory.create(self.context)

        self.metric_engine = MetricEngine()

        self.summary_generator = SummaryJsonGenerator(self.context)

        self.results_generator = EvaluationResultsGenerator(self.context)
        
        
    def run(self):

        framework = self.config_loader.get_framework()
        execution = self.config_loader.get_execution()
        application = self.config_loader.get_application()
        llm = self.config_loader.get_llm()

        print("=" * 60)
        print("Enterprise AI Quality Framework")
        print("=" * 60)

        print()
        print("Framework :", framework.get("name"))
        print("Version   :", framework.get("version"))

        print()
        print("Mode      :", execution.get("mode"))
        print("Profile   :", execution.get("profile"))

        print()
        print("Application :", application.get("name"))
        print("LLM Model   :", llm.get("model"))

        # -----------------------------         
        # Load Dataset
        # -----------------------------

        knowledge_processor = KnowledgeSourceProcessor(
            self.context
        )

        knowledge_processor.process()
        
        dataset_loader = DatasetLoader(self.context)

        dataset = dataset_loader.load()

        print()
        print(f"Dataset Loaded : {len(dataset)} Questions")
        print()
        results = self.evaluator.evaluate(dataset)

        summary = self.metric_engine.calculate(results)

        self.summary_generator.generate(summary)

        self.results_generator.generate(results)

        executive_report = ExecutiveReportGenerator(self.context)

        executive_report.generate(summary)

        detailed_report = DetailedReportGenerator(self.context)

        detailed_report.generate(summary, results)

        print()

        print("=" * 60)

        print("Evaluation Summary")

        print("=" * 60)

        print(f"Total Questions     : {summary.total_questions}")
        print(f"PASS                : {summary.pass_count}")
        print(f"REVIEW              : {summary.review_count}")
        print(f"FAIL                : {summary.fail_count}")

        print()

        print(f"Overall Score       : {summary.overall_score}%")
        print(f"Average Confidence  : {summary.average_confidence}%")
        print(f"Average Latency     : {summary.average_latency} ms")
        print(f"Quality Rating      : {summary.quality_rating}")
                