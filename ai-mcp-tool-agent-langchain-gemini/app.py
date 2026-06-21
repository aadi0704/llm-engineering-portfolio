import os
import asyncio
import requests
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.tools import tool
from langchain.agents import create_agent

api_key = os.getenv("GEMINI_API_KEY")
composio_api_key = os.getenv("COMPOSIO_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
rapidapi_key = os.getenv("RAPIDAPI_KEY")

model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=api_key
)

client = MultiServerMCPClient(
    {
        "mcp_tavily": {
            "transport": "http",
            "url": "https://backend.composio.dev/v3/mcp/7efbf1f7-80c7-4154-ab51-1dfcfe654a34/mcp?user_id=pg-test-f11cda97-4769-44a6-8001-62692b9d28f7",
            "headers": {"x-api-key": composio_api_key}
        }
    }
)

@tool
def search_jobs(skill: str, location: str):
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": f"{skill} in {location}",
        "page": "1",
        "country": "in",
        "employment_types": "INTERN,FULLTIME",
        "job_requirements": "no_experience,under_3_years_experience"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    jobs = data.get("data", [])

    return [
        {
            "title": j.get("job_title"),
            "company": j.get("employer_name"),
            "location": j.get("job_city"),
            "apply_link": j.get("job_apply_link")
        }
        for j in jobs
    ]

system_prompt = """
You are a Skill-to-Career Mapping assistant.

You help students:
- Understand skill demand in industry
- Find job opportunities
- Use tools when needed

Be clear, structured, and helpful.
"""

async def skill_map_agent():
    mcp_tools = await client.get_tools()
    tools = mcp_tools + [search_jobs]

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt
    )

    query = "What's the demand for generative AI in India and show job openings"

    response = await agent.ainvoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })

    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(skill_map_agent())