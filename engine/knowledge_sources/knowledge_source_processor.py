from knowledge_sources.pdf_loader import PDFLoader
from knowledge_sources.pdf_text_extractor import PDFTextExtractor
from knowledge_sources.text_chunker import TextChunker
from knowledge_sources.golden_dataset_generator import GoldenDatasetGenerator

class KnowledgeSourceProcessor:

    def __init__(self, context):

        self.context = context
        self.config_loader = context.get_config_loader()

    def process(self):

        #config = self.config_loader.get_knowledge_source()
        
        
        config = self.context.get_config_loader().get_knowledge_source()

        if not config.get("enabled", False):

            print()
            print("=" * 60)
            print("Knowledge Source Processing")
            print("=" * 60)
            print("Mode        : Mock")
            print("Status      : Disabled")
            print("Using existing Golden Dataset")
            print()

        return
        
        
        

        if not config.get("enabled"):

            print("Knowledge Source : Disabled")

            return

        if not config.get("regenerate_dataset"):

            print("Golden Dataset Generation : Skipped")

            return

        print()

        print("=" * 60)
        print("Knowledge Source Processing")
        print("=" * 60)

        print(f"Mode        : {config.get('mode')}")
        print(f"Input File  : {config.get('input_file')}")

        loader = PDFLoader(self.context)

        pdf = loader.load()
        
        extractor = PDFTextExtractor()

        text = extractor.extract(pdf)
        
        self.context.set_document_text(text)

        self.context.set_document_metadata({

            "source_file": pdf.name,

            "characters": len(text)

        })

        print(f"Characters Extracted : {len(text):,}")

        print()
        
        chunker = TextChunker()

        chunks = chunker.chunk(text)
        
        
        generator = GoldenDatasetGenerator(
            self.context
        )

        generator.generate(chunks)

        print(f"Chunks Created : {len(chunks)}")
        
        
        print()

        print("=" * 60)
        print("First Chunk Preview")
        print("=" * 60)

        print(chunks[0][:500])

        print()
        
        