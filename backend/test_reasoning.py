from hyperon import MeTTa

metta = MeTTa()

# load reasoning engine
with open("backend/kb.metta") as f:
    metta.run(f.read())

# load rules
with open("backend/rule.metta") as f:
    metta.run(f.read())

# load dataset
with open("backend/dataset.metta") as f:
    metta.run(f.read())

print("Running test query...")

result = metta.run("!(forward-chain &kb (fromNumber 4) (: FACT1 (has_parent John Mary)))")

print(result)