from model import MathQuestionModel

def generate_batch(level: int, batch_size: int = 3):

    model = MathQuestionModel(model_repo= "mistralai/Mistral-7B-Instruct-v0.3", local_dir="Mistral-7B-Instruct-v0.3")
    questions = []

    for i in range(batch_size):
        q = model.generate_question(level)
        questions.append(q)

    return questions


if __name__ == "__main__":
    level = int(input("Enter difficulty level (1-10): "))
    questions = generate_batch(level)

    print("\nGenerated Questions:")
    for i, q in enumerate(questions, start=1):
        print(f"{i}.\n {q}")
