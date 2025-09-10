from crewai import Crew,Process
from tasks import research_task,write_task
from agents import researchagent,newsWriter

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[researchagent,newsWriter],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback
def userquery(topic):
    result=crew.kickoff(inputs={"topic":topic})
    final_output = result.raw  
    return final_output