import time
from router import TaskRouter
from logger import ExecutionLogger


def main():
    router = TaskRouter()
    logger = ExecutionLogger()

    # Change these to test
    task_type = "research"
    task_content = "Impact of AI in DevOps"
    # Try: "How to hack a server"

    start_time = time.time()

    result = router.route(task_type, task_content)

    end_time = time.time()
    execution_time = end_time - start_time

    logger.log(f"Task Type: {task_type}")
    logger.log(f"Result: {result}")
    logger.log(f"Execution Time: {execution_time:.6f} seconds")

    print(result)
    print("\nExecution Logs:")
    logger.show_logs()


if __name__ == "__main__":
    main()
