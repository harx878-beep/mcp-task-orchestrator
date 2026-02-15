class BaseAgent:
    def __init__(self, name):
        self.name = name

    def execute(self, task):
        raise NotImplementedError("Subclasses must implement execute method")


class ResearchAgent(BaseAgent):
    def execute(self, task):
        return f"[ResearchAgent] Researched: {task}"


class SummarizerAgent(BaseAgent):
    def execute(self, task):
        return f"[SummarizerAgent] Summary of: {task}"


class GuardAgent(BaseAgent):
    def execute(self, task):
        if "hack" in task.lower():
            return "[GuardAgent] Task blocked due to security policy."
        return "[GuardAgent] Task approved."
