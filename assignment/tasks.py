from crewai import Task
from agents import HealthAdvisorAgent
from tools import web_search_tool

agents = HealthAdvisorAgent()
pathologist = agents.pathologist_agent()
researcher = agents.researcher_agent()
doctor = agents.doctor_agent()

# Task 1: Reading and summarizing the blood test report
read_and_summarize_task = Task(
    description="Extract relevant data from the provided blood test report and summarize it.",
    expected_output="A simplified summary of the blood test results.",
    tools=[],
    agent=pathologist,
    async_execution=False,
    output_file='blood_report_summary.txt'
)

# Task 2: Finding relevant health articles based on the summary
find_articles_task = Task(
    description="Search for health-related articles based on the summarized blood test report findings.",
    expected_output="A list of URLs to relevant health articles.",
    tools=[web_search_tool],
    agent=researcher,
    async_execution=False,
    output_file='health_articles_urls.txt'
)

# Task 3: Providing health recommendations based on article content
provide_recommendations_task = Task(
    description="Read the relevant articles and provide health recommendations based on their content.",
    expected_output="Health recommendations informed by the latest medical articles.",
    tools=[web_search_tool],
    agent=doctor,
    async_execution=False,
    output_file='health_recommendations.txt'
)
