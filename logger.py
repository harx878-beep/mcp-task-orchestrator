class ExecutionLogger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)

    def show_logs(self):
        for log in self.logs:
            print(log)
