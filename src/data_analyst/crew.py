from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from data_analyst.tools.csv_info_tool import CSVInfoTool


@CrewBase
class DataAnalyst:
    """DataAnalyst crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["data_analyst"],
            tools=[CSVInfoTool()],
            verbose=True
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer"],
            verbose=True
        )

    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["data_analysis_task"],
        )

    @task
    def report_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_writing_task"],
            output_file="report2.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DataAnalyst crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )