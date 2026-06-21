import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in environment variables")

    system_message = SystemMessage(content="You are a helpful assistant")
    user_message = HumanMessage(content="What is RAG?")

    messages = [system_message, user_message]

    
    model = init_chat_model(
        "google_genai:gemini-2.5-flash",
        api_key=api_key
    )

    
    response = model.invoke(messages)

    print(response.content)


if __name__ == "__main__":
    main()