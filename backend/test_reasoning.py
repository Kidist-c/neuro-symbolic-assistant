# test_reasoning.py
from backend.metta_engine import MettaEngine

# Initialize Metta engine
engine = MettaEngine()

# Query examples
chandler_children = engine.query("(child $x Chandler)", chain_type="match")
bob_grandparents = engine.query("(grandparent $x Bob)", chain_type="backward")
all_grandparents = engine.query("(grandparent $x $y)", chain_type="forward")
tim_cousins = engine.query("(cousin $x Tim)", chain_type="forward")
chandler_siblings = engine.query("(sibling $x Chandler)", chain_type="forward")
eve_uncles = engine.query("(uncle $x Eve)", chain_type="forward")

# Print results
print("Chandler's children:", chandler_children)
print("Bob's grandparents:", bob_grandparents)
print("All grandparent facts:", all_grandparents)
print("Tim's cousins:", tim_cousins)
print("Chandler's siblings:", chandler_siblings)
print("Eve's uncles:", eve_uncles)