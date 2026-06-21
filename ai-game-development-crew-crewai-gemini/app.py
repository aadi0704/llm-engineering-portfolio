import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

gemini_api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=gemini_api_key
)

search_tool = SerperDevTool(api_key=serper_api_key)

game_designer = Agent(
    role="Creative Game Designer",
    goal="Come up with fun, feasible game concepts and detailed mechanics based on user idea",
    backstory="You are an experienced game designer who converts ideas into simple playable 2D games",
    verbose=True,
    llm=llm
)

senior_engineer = Agent(
    role="Senior Python Game Developer",
    goal="Write clean Pygame code for the designed game",
    backstory="You are a senior Python game developer specialized in Pygame",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

qa_engineer = Agent(
    role="QA Engineer & Code Reviewer",
    goal="Review and improve game code for correctness and playability",
    backstory="You are a meticulous QA engineer who ensures code quality and gameplay correctness",
    verbose=True,
    llm=llm
)

task_design = Task(
    description="Take the user's game idea: {game_idea} and design a simple 2D game with objective, controls, mechanics, and entities",
    expected_output="Game Design Document",
    agent=game_designer
)

task_code = Task(
    description="Using the game design, write a complete runnable Pygame script. No missing parts.",
    expected_output="Pygame Python code",
    agent=senior_engineer,
    context=[task_design]
)

task_review = Task(
    description="Review and improve the Pygame code and return final corrected version",
    expected_output="Final improved Python game code",
    agent=qa_engineer,
    context=[task_design, task_code]
)

game_crew = Crew(
    agents=[game_designer, senior_engineer, qa_engineer],
    tasks=[task_design, task_code, task_review],
    process=Process.sequential,
    verbose=True
)

def main():
    game_idea = "A fun endless runner where a character jumps over obstacles"
    result = game_crew.kickoff(inputs={"game_idea": game_idea})
    print(result)

if __name__ == "__main__":
    main()