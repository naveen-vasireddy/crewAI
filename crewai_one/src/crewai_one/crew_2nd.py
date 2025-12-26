from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from crewai_one.crew import llm
# Tools
search_tool = SerperDevTool()

# Agents
researcher = Agent(
    role='Researcher',
    goal='Find and summarize the latest AI news',
    backstory='Experienced data analyst with a knack for uncovering trends.',
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passionate about technical storytelling.',
    verbose=True
)

# Tasks
research_task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 AI news',
    agent=researcher,
    tools=[search_tool]
)

write_task = Task(
    description='Write an engaging article based on the research',
    expected_output='A well-structured article about AI trends',
    agent=writer
)

# Try SEQUENTIAL
crew_sequential = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

# Try HIERARCHICAL (requires manager_llm)
crew_hierarchical = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.hierarchical,
    manager_llm=llm
)

# Run either one
# result = crew_sequential.kickoff()  # or crew_hierarchical.kickoff()