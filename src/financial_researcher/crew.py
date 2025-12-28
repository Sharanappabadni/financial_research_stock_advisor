from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv


load_dotenv(override=True)
api_key = os.getenv("OPENROUTER_API_KEY")
serper_key = os.getenv("SERPERDEV_API_KEY")

@CrewBase
class FinancialResearcher():
    """FinancialResearcher crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            llm=LLM(
                model="openrouter/meta-llama/llama-3.3-70b-instruct:free",
                api_key=api_key,
            ),
            verbose=True,
            tools=[SerperDevTool(api_key=serper_key)]
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst"],
            llm=LLM(
                model="openrouter/openai/gpt-oss-120b",
                api_key=api_key,
            ),
            verbose=True,
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            llm=LLM(
                model="openrouter/openai/gpt-oss-120b",
                api_key=api_key,
            ),
            verbose=True,
        )
    
    @agent
    def decision_maker(self) -> Agent:
        return Agent(
            config=self.agents_config["decision_maker"],
            llm=LLM(
                model="openrouter/meta-llama/llama-3.3-70b-instruct:free",
                api_key=api_key,
            ),
            verbose=True,
        )


    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def analyst_task(self) -> Task:
        return Task(config=self.tasks_config["analyst_task"])

    @task
    def report_task(self) -> Task:
        return Task(config=self.tasks_config["report_task"])
    
    @task
    def decision_task(self) -> Task:
        return Task(config=self.tasks_config["decision_task"])


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
