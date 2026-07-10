from pathlib import Path


class PDFLoader:

    def __init__(self, context):

        self.context = context
        self.config_loader = context.get_config_loader()

    def load(self):

        config = self.config_loader.get_knowledge_source()

        project_root = Path(__file__).resolve().parents[2]

        pdf_path = (
            project_root
            / config.get("input_file")
        )

        if not pdf_path.exists():

            raise FileNotFoundError(
                f"Knowledge Source not found:\n{pdf_path}"
            )

        print(f"Knowledge Source Found : {pdf_path.name}")

        return pdf_path