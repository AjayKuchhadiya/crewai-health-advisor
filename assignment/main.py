import os
import sys
from crewai import Crew, Process
from agents import HealthAdvisorAgent
from tasks import read_and_summarize_task, find_articles_task, provide_recommendations_task
from pdf_reader import extract_text_from_pdf

def main(pdf_path):
    try:
        print("Initializing Crew...")
        # Initialize the agents
        agents = HealthAdvisorAgent()
        pathologist = agents.pathologist_agent()
        researcher = agents.researcher_agent()
        doctor = agents.doctor_agent()

        # Forming the medical-focused crew with the specified agents and tasks
        crew = Crew(
            agents=[pathologist, researcher, doctor],
            tasks=[read_and_summarize_task, find_articles_task, provide_recommendations_task],
            process=Process.sequential,  # Tasks are executed one after the other
            memory=True,  # Enable memory for agents to retain context
            cache=True,   # Enable caching to speed up repeated tasks
            max_rpm=100,  # Maximum rate of requests per minute
            share_crew=True,  # Share the crew's state across tasks
        )

        print("Extracting text from PDF...")
        # Starting the task execution process with a sample blood test report file
        report_data = extract_text_from_pdf(pdf_path)

        print("Starting Crew kickoff...")
        result = crew.kickoff(inputs={'report_data': report_data})
        print('\n\n\nFinal verdict: \n', result, '\n\n\n')

    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = r'C:\Users\Owner\Desktop\wingify\crewai-health-advisor\report.pdf'
    main(pdf_path)
