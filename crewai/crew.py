from crewai import Crew, Process
from agents import reader, teacher, quiz_master
from tasks import read_task, teach_task, quiz_task

study_crew = Crew(
    agents=[reader, teacher, quiz_master],
    tasks=[read_task, teach_task, quiz_task],
    process=Process.sequential,  # Ensures correct order
    verbose=True
)