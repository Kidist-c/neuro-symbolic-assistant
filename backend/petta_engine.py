from petta_engine import KnowledgeBase #stores symbolic knowledge in the form of facts and rules
from petta_engine import BackwardChainer #performs backward chaining inference to answer quieries based on the knowledgebase
from petta_engine import ForwardChainer #performs forward chaining inference to derive new facts from existing ones in the knowledgebase


class PettaEngine:
    def __init__(self,dataset_path="backend/dataset.metta" , rules_path="backend/rules.metta"):
        #create an instance of the knowledge base to store facts and rules
        self.knowledge_base = KnowledgeBase()

        # load the facts  and rules
        self.load_facts(dataset_path)
        self.load_rules(rules_path)
    def load_facts(self, path):
        """
        Load the contents of a file and add the facts to the knowledge base. """
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.knowledge_base.add_fact(line) # if the line is not empty add to the knowledge base
    def load_rules(self, path):
        """
        Load the contents of a file and add the rules to the knowledge base. """
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.knowledge_base.add_rule(line) # if the line is not empty add to the knowledge base
    def query(self, query, chain_type="backward"):
        """
        perform the inference based on the query and the specified chaining type
        and retun the results for the query
        """
        try:
            if chain_type == "backward":
                chainer = BackwardChainer(self.knowledge_base)
                result = chainer.query(query)
            elif chain_type == "forward":
                chainer = ForwardChainer(self.knowledge_base)
                result = chainer.infer(query)
            else:
                raise ValueError("Invalid chain type. Use 'backward' or 'forward'.") 
            return result
        except Exception as e:
            return {"error":str(e)}
        



        



