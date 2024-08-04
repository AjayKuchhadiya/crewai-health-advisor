import os
from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools import web_search_tool

load_dotenv()

class HealthAdvisorAgent():
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )

    def pathologist_agent(self):
        return Agent(
            role='Pathologist',
            goal='Carefully analyze and summarize the provided blood test report. Ensure to include relevant numerical values for key metrics such as hemoglobin levels, white blood cell count, platelet count, cholesterol levels, and any other significant parameters present in the report.',
            verbose=True,
            memory=True,
            backstory=(
                "You are an expert in understanding and analyzing blood test reports. "
                "Your task is to summarize the report including all the important points."
            ),
            allow_delegation=True,
            llm=self.llm
        )

    def researcher_agent(self):
        return Agent(
            role='Medical Researcher',
            goal='Find relevant health-related articles based on the summarized blood test report.',
            verbose=True,
            memory=True,
            backstory=(
                "You are a medical researcher tasked with finding articles that are relevant to a blood test report summary. "
                "You use advanced web search tools to locate the best information available online which matches the patient's condition."
            ),
            tools=[web_search_tool],
            allow_delegation=False,
            llm=self.llm
        )

    def doctor_agent(self):
        return Agent(
            role='Doctor',
            goal='Provide health recommendations to the patient based on article content and blood test report analysis.',
            verbose=True,
            memory=True,
            backstory=(
                "You are a medical professional with expertise in providing insights and health recommendations "
                "based on the results of blood tests and relevant medical articles."
            ),
            tools=[web_search_tool],
            allow_delegation=False,
            llm=self.llm
        )
