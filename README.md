# mcp-task-orchestrator
Secure multi-agent MCP-style task orchestrator with routing and guard validation.
# MCP Task Orchestrator

A secure, modular multi-agent task orchestration system inspired by MCP (Model Context Protocol) architecture principles.

This project demonstrates how AI agents can be routed, validated, monitored, and executed in a controlled environment — similar to how orchestration platforms like Archestra manage MCP-based agents at scale.

---

## 🚀 Overview

The MCP Task Orchestrator is a lightweight agent control system built using Python OOP principles.

It includes:

- 🔐 Guard Layer (Security Validation)
- 🎛 Intelligent Task Routing
- 🤖 Specialized Agents (Research, Summarization)
- 📊 Execution Logging
- ⏱ Performance Monitoring

The system ensures tasks are validated before execution and routed to the appropriate agent, demonstrating controlled orchestration.

---

## 🧠 Architecture

User Task  
↓  
Guard Agent (Security Check)  
↓  
Task Router  
↓  
Specialized Agent  
↓  
Execution Logger  

This mirrors how real-world MCP platforms manage agent execution with governance and observability.

---

## 🛠️ Components

### 1️⃣ BaseAgent
Abstract class defining agent behavior.

### 2️⃣ ResearchAgent
Handles research-type tasks.

### 3️⃣ SummarizerAgent
Handles summarization tasks.

### 4️⃣ GuardAgent
Validates tasks before execution and blocks unsafe requests.

### 5️⃣ TaskRouter
Routes tasks to the correct agent after security approval.

### 6️⃣ ExecutionLogger
Tracks:
- Task Type
- Result
- Execution Time

---

## 🔐 Security Layer

The GuardAgent prevents execution of unsafe or restricted tasks.

Example:
If a task contains restricted keywords (e.g., "hack"), it is blocked before reaching execution.

This simulates governance and control mechanisms found in production AI orchestration systems.

---

## 📊 Observability & Monitoring

The system logs:

- Task type
- Execution result
- Execution time

This demonstrates observability principles critical for scalable AI platforms.

---

## ▶️ How to Run

1. Clone the repository:
git clone https://github.com/harx878-beep/mcp-task-orchestrator.git

2. Navigate to the folder:

3. Run the system:

---

## 🎯 Why This Matters

Modern AI systems require:

- Centralized control
- Secure execution
- Clear routing logic
- Observability
- Scalable architecture

This project demonstrates those principles in a simplified but structured implementation.

---

## 🏁 Future Improvements

- Multi-agent parallel execution
- Dynamic task classification
- Role-based access control
- API interface
- Cloud deployment

---

## 👤 Author

Built as part of the "2 Fast 2 MCP" Hackathon challenge.

