from petta_engine import PettaEngine
engine = PettaEngine()
result = engine.query("(grandparent Kebede $x)", "backward")
print(result)