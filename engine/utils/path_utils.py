from pathlib import Path


class PathUtils:

    @staticmethod
    def project_root():

        return Path(__file__).resolve().parents[2]