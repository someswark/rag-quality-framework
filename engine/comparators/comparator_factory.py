from comparators.semantic_comparator import SemanticComparator


class ComparatorFactory:

    @staticmethod
    def create():

        return SemanticComparator()