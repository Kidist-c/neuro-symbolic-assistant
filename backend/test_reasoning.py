# test_metta_engine.py
from backend.metta_engine import MettaEngine

# Initialize engine
engine = MettaEngine(dataset_path="backend/dataset.metta", rules_path="backend/rule.metta")

# Test queries
queries = [
    "Who are Chandler's children?",
    "Who are Bob's grandparents?",
    "Who are Tim's cousins?",
    "Who are Chandler's siblings?",
    "Who are Eve's uncles?"
]

for q in queries:
    print(f"\nQuestion: {q}")
    # Backward chaining
    backward_result = engine.query(q, chain_type="backward")
    print("Backward chain result:", backward_result)

    # Forward chaining
    forward_result = engine.query(q, chain_type="forward")
    print("Forward chain result:", forward_result)