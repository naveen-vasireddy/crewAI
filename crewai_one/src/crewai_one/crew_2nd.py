from crewai import Agent, Task, Crew, Process
from crewai_one.crew import llm  # Match the name the LLM is trying to use

# Agents
researcher = Agent(
    role='Researcher',
    goal='Find and summarize the latest AI news',
    backstory='Experienced data analyst with a knack for uncovering trends.',
    verbose=True,
    llm=llm
)

writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passionate about technical storytelling.',
    verbose=True
)

# Tasks
research_task = Task(
    description='First: Find and summarie the latest AI news',
    expected_output='A bullet list summary of the top 5 AI news',
    agent=researcher,
)

write_task = Task(
    description='Later: Write an engaging article based on the research',
    expected_output='A well-structured article about AI trends',
    agent=writer
)

# Try SEQUENTIAL
crew_sequential = Crew(
    agents=[ writer, researcher],
    tasks=[ write_task, research_task],
    process=Process.sequential
)

# Try HIERARCHICAL (requires manager_llm)
crew_hierarchical = Crew(
    agents=[ writer , researcher],
    tasks=[ write_task , research_task],
    process=Process.hierarchical,
    manager_llm=llm
)

# Run either one
# result = crew_sequential.kickoff()  # or crew_hierarchical.kickoff()