from core.config_loader import ConfigLoader


class FrameworkContext:

    def __init__(self):

        self.config_loader = ConfigLoader()

        self.document_text = None

        self.document_metadata = {}

    def get_config_loader(self):

        return self.config_loader

    # -----------------------------------------
    # Document Context
    # -----------------------------------------

    def set_document_text(self, text):

        self.document_text = text

    def get_document_text(self):

        return self.document_text

    # -----------------------------------------
    # Document Metadata
    # -----------------------------------------

    def set_document_metadata(self, metadata):

        self.document_metadata = metadata

    def get_document_metadata(self):

        return self.document_metadata