from core.config_loader import ConfigLoader


class FrameworkContext:

    def __init__(self):

        self.config_loader = ConfigLoader()

    def get_config_loader(self):

        return self.config_loader