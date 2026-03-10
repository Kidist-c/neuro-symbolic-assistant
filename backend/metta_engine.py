# metta_engine.py
from hyperon import MeTTa
import re

class MettaEngine:
    def __init__(self, dataset_path="backend/dataset.metta", rules_path="backend/rules.metta"):
        self.metta = MeTTa()
        self.dataset_path = dataset_path
        self.rules_path = rules_path
        self.load_code()

    def load_code(self):
        """Load facts and rules into MeTTa"""
        code = ""
        for path in [self.dataset_path, self.rules_path]:
            with open(path, "r") as f:
                code += f.read() + "\n"
        self.code = code

    def nl_to_metta_atom(self, question: str) -> str:
        """
        Convert simple natural language query into MeTTa atom.
        For example:
        - "Who are Bob's grandparents?" -> (grandparent $x Bob)
        - "Who are Chandler's children?" -> (Parent Chandler $x)
        """
        question = question.lower()
        # Example patterns
        if "grandparent" in question:
            m = re.search(r"(\w+)'s grandparent", question)
            if m:
                person = m.group(1).capitalize()
                return f"(grandparent $x {person})"
        elif "children" in question:
            m = re.search(r"(\w+)'s children", question)
            if m:
                person = m.group(1).capitalize()
                return f"(Parent {person} $x)"
        elif "cousin" in question:
            m = re.search(r"(\w+)'s cousins", question)
            if m:
                person = m.group(1).capitalize()
                return f"(cousin $x {person})"
        elif "siblings" in question or "brothers" in question or "sisters" in question:
            m = re.search(r"(\w+)'s siblings", question)
            if m:
                person = m.group(1).capitalize()
                return f"(sibling $x {person})"
        elif "uncles" in question:
            m = re.search(r"(\w+)'s uncles", question)
            if m:
                person = m.group(1).capitalize()
                return f"(uncle $x {person})"
        elif "aunts" in question:
            m = re.search(r"(\w+)'s aunts", question)
            if m:
                person = m.group(1).capitalize()
                return f"(aunt $x {person})"
        else:
            # fallback: return the question as-is for neural
            return question

    def query(self, question: str, chain_type="backward"):
        """Run MeTTa query (backward or forward)"""
        atom_query = self.nl_to_metta_atom(question)
        if not atom_query:
            return "Unable to convert question to symbolic query."

        if chain_type == "backward":
            metta_query = f"{self.code}\n!(back-chain &self (fromNumber 5) (: $ans {atom_query}))"
        elif chain_type == "forward":
            metta_query = f"{self.code}\n!(forward-chain &self (fromNumber 5) ({atom_query}))"
        else:
            return "Invalid chain type"

        result = self.metta.run(metta_query)
        return result