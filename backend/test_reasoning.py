from backend.metta_engine import MettaEngine


def run_tests():
    engine = MettaEngine()

    questions = [
        "Who are Chandler's children?",
        "Who are Bob's grandparents?",
        "Who are Tim's cousins?",
        "Who are Chandler's siblings?",
        "Who are Eve's uncles?"
    ]

    print("\n===== METTA ENGINE TEST =====\n")

    for q in questions:
        print(f"Question: {q}")

        result = engine.query(q)

        print(f"Answer: {result}\n")


if __name__ == "__main__":
    run_tests()