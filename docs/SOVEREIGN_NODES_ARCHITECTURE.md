# A.I.M. Swarm Architecture: The Sovereign Nodes Model (V3 - Persistent Fractal Teams)

## Executive Summary
The `aim-swarm` repository is an independent, modular Multi-Agent orchestration framework. It allows an A.I.M. Orchestrator to hire, manage, and collaborate with a permanent roster of specialized AI colleagues.

The core architectural principle is **"Persistent Fractal Exoskeletons."**

---

## 1. The Paradigm: Spawn Once, Wake Up Often
Unlike ephemeral agent frameworks that delete the workspace after a task is completed, A.I.M. Swarm treats agents as **Persistent Team Members**. 

*   **Fractal Clones:** Each Swarm Agent is a full, independent installation of the A.I.M. operating system living in a totally air-gapped directory.
*   **Persistent Memory:** Because the agent's folder is permanent, it accumulates its own unique experiences over months of work. Its background Subconscious Daemon builds a highly specialized `wiki/` of domain patterns, and its `archive/` retains a permanent history of past projects.

---

## 2. The Architecture: Blueprints vs. The Roster

### The `agents/` Directory (Blueprint Library)
This folder contains the "DNA" for different specialized roles (e.g., `python-developer/`, `frontend-artist/`). It is just a template library.
A Blueprint Contains:
*   `GEMINI.md`: The strict persona and operational boundaries.
*   `engrams/`: Pre-compiled domain knowledge to seed the agent's brain upon creation (e.g., `python_troubleshooting.engram`).

### The `teams/` Directory (The Active Roster)
This is where the actual, living A.I.M. installations reside.
When you "hire" a Python Developer, the factory script:
1. Performs a full `git clone` of the A.I.M. core repository into `teams/python-developer/`.
2. Runs a Clean Sweep to wipe the generic brain.
3. Transplants the Blueprint (`GEMINI.md` and seed `engrams/`) into the clone.
4. The agent is now a permanent employee.

---

## 3. Communication & Execution
The Orchestrator interacts with the Roster using hybrid communication:

1. **Synchronous Pings (Tmux Injection):** The Orchestrator can split a `tmux` pane, boot the agent's local `gemini` CLI, and inject real-time commands using the `paste-buffer` protocol. The agent can reply directly to the Orchestrator's `tmux` session ID.
2. **Asynchronous Drops (Aim-Chalkboard):** For longer tasks, the Orchestrator asks the agent to use the `aim-chalkboard` GitOps post office. The agent drops markdown files into team inboxes without blocking terminal UI threads.

## Conclusion
By preserving the Swarm Nodes permanently, we create a team of AI Principal Engineers that actually learn, adapt, and specialize over time, protected by the strict GitOps and memory frameworks of the A.I.M. Exoskeleton.
