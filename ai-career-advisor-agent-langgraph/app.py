import os
import requests
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent



TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")


if not all([TAVILY_API_KEY, RAPIDAPI_KEY, GOOGLE_API_KEY]):
    raise ValueError("Missing one or more API keys in environment variables")


skill_demand_tool = TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=TAVILY_API_KEY,
)



@tool
def search_jobs(skill: str, location: str) -> list:
    """
    Search for jobs requiring a specific skill using JSearch API.
    """
    print("\nCalling search_jobs tool")
    print(f"Searching jobs for: {skill} in {location}")

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
    }

    params = {
        "query": f"{skill} in {location}",
        "page": "1",
        "num_pages": "1",
        "country": "in",
        "employment_types": "INTERN,FULLTIME",
        "job_requirements": "no_experience,under_3_years_experience",
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    jobs = data.get("data", [])

    print(f"Found {len(jobs)} jobs\n")

    return [
        {
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "apply_link": job.get("job_apply_link"),
        }
        for job in jobs
    ]


SYSTEM_PROMPT = """
You are a Skill-to-Career Mapping assistant that helps students understand skill demand
and find matching job opportunities.

You have access to:
- skill_demand_tool: industry demand, salary insights, career trends
- search_jobs: real job listings based on skills and location

Always format output in clean plain text (no markdown).
Include all job details with apply links.
"""



model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=GOOGLE_API_KEY,
)


checkpointer = InMemorySaver()
config = {"configurable": {"thread_id": "1"}}



agent = create_react_agent(
    model=model,
    tools=[skill_demand_tool, search_jobs],
    checkpointer=checkpointer,
)



def main():
    user_query = (
        "What's the demand for generative AI in the industry "
        "and show me related job openings in India"
    )

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_query}]},
        config=config,
    )

    print("\nFINAL RESPONSE:\n")
    print(response["messages"][-1].content)

    
    follow_up = "Tell me more about the second job you showed"

    response = agent.invoke(
        {"messages": [{"role": "user", "content": follow_up}]},
        config=config,
    )

    print("\nFOLLOW-UP RESPONSE:\n")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()