from crewai import Task
from agents import reader, teacher, quiz_master
from utils import extract_pdf_text

pdf_text = extract_pdf_text("sample.pdf")

read_task = Task(
    description=f"""
Extract important learning points from this content:

{pdf_text}
""",
    agent=reader,
    expected_output="Structured key study notes in bullet points"
)

teach_task = Task(
    description="""
Explain the extracted points in simple language.
Make it beginner friendly.
""",
    agent=teacher,
    expected_output="Simplified explanation of concepts",
    context=[read_task]  # 👈 Ensures output flows
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
    expected_output="Quiz with one-line answers",
    context=[teach_task]  # 👈 Proper chaining
)