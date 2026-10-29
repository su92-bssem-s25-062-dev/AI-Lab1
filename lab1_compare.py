
def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"


def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"


cases = [
    ("Complete high", 82, True, 0.81),
    ("Complete low", 68, True, 0.74),
    ("Incomplete high", 91, False, 0.88),
    ("Boundary", 70, True, 0.70)
]

print("CASE | SYMBOLIC | PROBABILITY | DISAGREEMENT")
print("-" * 55)

for name, score, complete, probability in cases:
    symbolic_result = symbolic(score, complete)
    probability_result = threshold(probability)
    disagreement = symbolic_result != probability_result

    print(
        f"{name} | {symbolic_result} | "
        f"{probability_result} | {disagreement}"
    )
