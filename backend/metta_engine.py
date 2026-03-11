from hyperon import MeTTa
import re


class MettaEngine:
    """
    Interface between Python and MeTTa knowledge base.
    Loads the KB and executes reasoning queries.
    """

    def __init__(self, kb_path="backend/kb.metta"):
        self.metta = MeTTa()
        self.kb_path = kb_path
        self._load_kb()

    def _load_kb(self):
        """Load the MeTTa knowledge base file."""
        with open(self.kb_path, "r") as f:
            self.kb_code = f.read()

    # -------------------------------
    # Natural language → MeTTa query
    # -------------------------------

    def nl_to_metta(self, question: str):
        question = question.lower()

        if "children" in question:
            m = re.search(r"(\w+)'s children", question)
            if m:
                return f"(Parent {m.group(1).capitalize()} $x)"

        if "grandparent" in question:
            m = re.search(r"(\w+)'s grandparent", question)
            if m:
                return f"(grandparent $x {m.group(1).capitalize()})"

        if "siblings" in question:
            m = re.search(r"(\w+)'s siblings", question)
            if m:
                return f"(sibling $x {m.group(1).capitalize()})"

        if "cousins" in question:
            m = re.search(r"(\w+)'s cousins", question)
            if m:
                return f"(cousin $x {m.group(1).capitalize()})"

        if "uncles" in question:
            m = re.search(r"(\w+)'s uncles", question)
            if m:
                return f"(uncle $x {m.group(1).capitalize()})"

        return None

    # -------------------------------
    # Run reasoning query
    # -------------------------------

    def query(self, question: str, depth=5):

        atom = self.nl_to_metta(question)

        if atom is None:
            return {"error": "Could not convert question to symbolic query"}

        metta_query = f"""
        {self.kb_code}

        !(back-chain &kb (fromNumber {depth}) (: $ans {atom}))
        """

        # DEBUG PRINT
        print("\n===== METTA QUERY =====")
        print(metta_query)

        result = self.metta.run(metta_query)

        # DEBUG PRINT
        print("\n===== RAW RESULT =====")
        print(result)

        return self._parse_result(result)

    # -------------------------------
    # Parse MeTTa output
    # -------------------------------

    def _parse_result(self, result):

        answers = []

        for outer in result:
            for item in outer:
                text = str(item)

                matches = re.findall(r'\(\w+\s+\w+\s+(\w+)\)', text)

                answers.extend(matches)

        return list(set(answers))