from hyperon import MeTTa

class MettaEngine:

    def __init__(self, dataset_path="backend/dataset.metta", rules_path="backend/rules.metta"):
        
        # create MeTTa instance
        self.metta = MeTTa()

        # store file paths
        self.dataset_path = dataset_path
        self.rules_path = rules_path

    def load_code(self):
        """
        Load dataset and rules from files
        """

        with open(self.dataset_path, "r") as f:
            facts = f.read()

        with open(self.rules_path, "r") as f:
            rules = f.read()

        return facts + "\n" + rules

    def query(self, query, chain_type="backward"):
        """
        Run a MeTTa query using forward or backward chaining
        """

        try:

            code = self.load_code()

            if chain_type == "backward":

                metta_query = f"""
                {code}

                !(back-chain &self (fromNumber 5) (: $ans {query}))
                """

            elif chain_type == "forward":

                metta_query = f"""
                {code}

                !(forward-chain &self (fromNumber 5) {query})
                """

            else:
                raise ValueError("Invalid chain type. Use 'backward' or 'forward'.")

            result = self.metta.run(metta_query)

            return result

        except Exception as e:
            return {"error": str(e)}