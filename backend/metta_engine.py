from hyperon import MeTTa
import os

class MettaEngine:

    def __init__(self):

        self.metta = MeTTa()

        base_dir = os.path.dirname(__file__)
        kb = open(os.path.join(base_dir,"kb.metta")).read()
        rules = open(os.path.join(base_dir,"rule.metta")).read()
        dataset = open(os.path.join(base_dir,"dataset.metta")).read()
        self.metta.run(kb)
        self.metta.run(rules)
        self.metta.run(dataset)
        print("MeTTa knowledge base loaded")
    def query(self,query):

        print("Running symbolic query:",query)
        result = self.metta.run(query)
        return result