import evaluate
from google import genai
from google.genai import types
import os

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

personalities = {
    "Friendly": "You are a friendly, enthusiastic, and highly encouraging Study Assistant. Your goal is to break down concepts simply and clearly.",
    "Academic": "You are a strict academic professor who gives detailed, structured, and precise explanations."
}

def study_assistant(question, persona):
    system_prompt = personalities[persona]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        ),
        contents=question
    )
    return response.text


def evaluate_text_generation(predictions, references):
    bleu = evaluate.load("bleu")
    bleu_score = bleu.compute(
        predictions=predictions,
        references=[[r] for r in references],
        max_order=2
    )

    bertscore = evaluate.load("bertscore")
    bert_result = bertscore.compute(
        predictions=predictions,
        references=references,
        lang="en"
    )

    return {
        "bleu": bleu_score["bleu"],
        "bert_precision": sum(bert_result["precision"]) / len(bert_result["precision"]),
        "bert_recall": sum(bert_result["recall"]) / len(bert_result["recall"]),
        "bert_f1": sum(bert_result["f1"]) / len(bert_result["f1"])
    }


def run_evaluation():
    test_data = [
        {
            "question": "What is a variable in programming?",
            "reference": "A variable is a container that stores data values."
        },
        {
            "question": "What are LLMs?",
            "reference": "LLMs are large language models trained on vast text data."
        }
    ]

    predictions = []
    references = []

    for item in test_data:
        answer = study_assistant(item["question"], "Friendly")
        predictions.append(answer)
        references.append(item["reference"])

    results = evaluate_text_generation(predictions, references)
    print(results)


if __name__ == "__main__":
    run_evaluation()