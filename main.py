# Online Examination System

def login():
    print("===== Online Examination System =====")
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    return name


if __name__ == "__main__":
    candidate = login()