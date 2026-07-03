from core.framework_context import FrameworkContext
from evaluators.evaluator_factory import EvaluatorFactory
from datasets.dataset_loader import DatasetLoader


class EnterpriseAIQualityFramework:

    def __init__(self):

        self.context = FrameworkContext()

        self.config_loader = self.context.get_config_loader()

        self.evaluator = EvaluatorFactory.create(self.context)
        
        
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

        dataset_loader = DatasetLoader(self.context)

        dataset = dataset_loader.load()

        print()
        print(f"Dataset Loaded : {len(dataset)} Questions")
        print()

        self.evaluator.evaluate(dataset)