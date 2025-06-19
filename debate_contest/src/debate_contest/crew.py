from crewai import Agent, Crew, Process, Task

from crewai.project import CrewBase, agent, crew, task

from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

@CrewBase
class DebateContest():
    """DebateContest crew"""

    agents_config = 'config/agents.yaml'

    tesks_config = 'config/tasks.yaml'


    @agent
    def debator_contestant1(self) -> Agent:
        return Agent(

            config = self.agents_config['debator_contestant1'], 

            verbose = True
        )

    @agent
    def debator_contestant2(self)-> Agent:

        return Agent(
            
                     config = self.agents_config['debator_contestant2'],
                     
                     verbose = True
                     
          )    

    @agent
    def judge(self) -> Agent:

        return Agent(

            config = self.agents_config['judge'], 

            verbose = True
        )

    
    @task
    def propose_motion(self) -> Task:

        return Task(

            config = self.tasks_config['propose_motion']

        )

    @task
    def oppose_motion(self) -> Task:

        return Task(

            config = self.tasks_config['oppose_motion']
            
        )
    

    @task
    def review(self) -> Task:
    
     return Task(

        config = self.tasks_config['review']

     )

    @crew
    def crew(self) -> Crew:

        """Creates the DebateContest crew"""
        
        return Crew(

            agents=self.agents, 

            tasks=self.tasks, 

            process=Process.sequential,

            verbose=True,
            
        )
