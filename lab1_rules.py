
def scholarship_check(score, documents_complete,
                     statement_submitted, eligibility_confirmed):

    if (documents_complete and score >= 70
            and statement_submitted and eligibility_confirmed):
        return "Review"

    return "Hold"


test_cases = [
    ("Successful application", (80, True, True, True), "Review"),
    ("Statement missing", (80, True, False, True), "Hold"),
    ("Eligibility not confirmed", (80, True, True, False), "Hold"),
    ("Boundary score", (70, True, True, True), "Review")
]

for name, inputs, expected in test_cases:
    actual = scholarship_check(*inputs)

    print("Test:", name)
    print("Input:", inputs)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Result:", "PASS" if actual == expected else "FAIL")
    print("-" * 40)
