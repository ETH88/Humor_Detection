from utils import PreProcess

class Normalize(PreProcess):
    """
    Pre-processing rule - normalize text
    """
    def __init__(self):
        self._enabled = False

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def apply(self, data: list): #TODO: IMPLEMENT (not yet implemented)
        return {'data': data}