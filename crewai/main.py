# main.py
from crew import study_crew
from crewai import Task
from agents import reader, teacher, quiz_master
from utils import extract_pdf_text

# Read PDF text
pdf_text = extract_pdf_text("sample.pdf")  # Make sure sample.pdf is in the same folder

# Define tasks for CrewAI
read_task = Task(
    description=f"Extract important learning points from this content:\n{pdf_text}",
    agent=reader,
    expected_output="Key study notes"
)

teach_task = Task(
    description="Explain the extracted points in simple language.",
    agent=teacher,
    expected_output="Simplified explanation"
)

quiz_task = Task(
    description="""
Create 5 quiz questions from the explanation.
Provide one-line answers for each question.
Format:
Q1:
A1:
""",
    agent=quiz_master,
    expected_output="Quiz with one-line answers"
)

# Setup Crew with agents and tasks
from crewai import Crew

study_crew = Crew(
    agents=[reader, teacher, quiz_master],
    tasks=[read_task, teach_task, quiz_task],
    verbose=True
)

# Run the workflow
result = study_crew.kickoff()

print("\n===== GENERATED QUIZ =====\n")
print(result)

# Save output
with open("quiz_output.txt", "w", encoding="utf-8") as f:
    f.write(str(result))

print("\nQuiz saved as quiz_output.txt")