# Online Examination System

def login():
    print("===== Online Examination System =====")
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    return name


def display_results(candidate, score, total):
    incorrect = total - score
    percentage = (score / total) * 100 if total > 0 else 0
    status = "PASSED" if percentage >= 50 else "FAILED"

    print("\n" + "=" * 40)
    print("         EXAM RESULT SUMMARY")
    print("=" * 40)
    print(f"Candidate Name   : {candidate}")
    print(f"Total Questions  : {total}")
    print(f"Correct Answers  : {score}")
    print(f"Incorrect Answers: {incorrect}")
    print(f"Final Score      : {percentage:.1f}%")
    print(f"Status           : {status}")
    print("=" * 40)


if __name__ == "__main__":
    candidate = login()
    display_results(candidate, 4, 5)