from agents import ResearchAgent, SummarizerAgent, GuardAgent


class TaskRouter:
    def __init__(self):
        self.research_agent = ResearchAgent("ResearchAgent")
        self.summarizer_agent = SummarizerAgent("SummarizerAgent")
        self.guard_agent = GuardAgent("GuardAgent")

    def route(self, task_type, task):
        # Step 1: Security check
        guard_result = self.guard_agent.execute(task)

        if "blocked" in guard_result:
            return guard_result

        # Step 2: Route to correct agent
        if task_type == "research":
            return self.research_agent.execute(task)

        elif task_type == "summarize":
            return self.summarizer_agent.execute(task)

        else:
            return "Unknown task type"

