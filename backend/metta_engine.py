from hyperon import MeTTa
import os

class MettaEngine:

    def __init__(self):

        self.metta = MeTTa()

        base = os.path.dirname(__file__)

        kb = open(os.path.join(base,"metta/kb.metta")).read()
        rules = open(os.path.join(base,"metta/rules.metta")).read()
        dataset = open(os.path.join(base,"metta/dataset.metta")).read()

        self.metta.run(kb)
        self.metta.run(rules)
        self.metta.run(dataset)

    def ask(self, query):
        print("Running MeTTa query:", query)
        result = self.metta.run(query)
        return result