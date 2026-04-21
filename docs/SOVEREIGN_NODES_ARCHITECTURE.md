# A.I.M. Swarm Architecture: The Sovereign Nodes Model (V2 - Fractal Exoskeletons)

## Executive Summary
The `aim-swarm` repository is designed as an independent, modular Multi-Agent framework. It is fundamentally decoupled from the core single-agent A.I.M. Operating System. 

It is completely optional. When an A.I.M. operator (like the `leaddeed-aim` project) needs a dedicated team of experts (not just lightweight subagents sharing the root directory), they clone `aim-swarm` into their `workspace/` folder.

The core architectural principle of `aim-swarm` is the **"Fractal Exoskeleton"** model.

---

## 1. The Distinction: Subagents vs. Sovereign Agents
*   **Subagents (Native Gemini CLI):** Fast, token-efficient, and run in the background. However, they share the primary agent's root directory and file system. They are prone to Git collisions and memory bleeding if asked to perform massive, multi-file architectural overhauls concurrently.
*   **Sovereign Agents (A.I.M. Swarm):** Full, independent clones of the A.I.M. operating system. They operate in totally air-gapped directories. They have their own SQLite memory databases, their own Git histories, their own `aim pulse` distillation pipelines, and their own specialized `.engram` cartridges.

---

## 2. The Architecture: The `agents/` Blueprint Library
The `aim-swarm` repository does not contain active agents. It acts as a **Factory** and a **Library**.

Inside the repository is an `agents/` folder. This folder contains the "DNA" or blueprints for hundreds of specialized Sovereign Agents (e.g., `python-architect/`, `web3-auditor/`, `qa-automation/`).

**A Blueprint Contains:**
*   `GEMINI.md`: The agent's strict persona and operational boundaries.
*   `TOOLS.md`: Custom tool definitions specific to that agent's role.
*   `engrams/`: Pre-compiled domain knowledge (e.g., `react_docs.engram`).

### The Spawning Process
When the Orchestrator needs a Python Architect:
1. It runs the `aim_spawn.py` factory script.
2. The script creates a new, isolated directory (e.g., `teams/python-architect-1/`).
3. **The Fractal Clone:** It performs a full `git clone` of the core A.I.M. repository into that directory and runs a headless `setup.sh`.
4. **The Brain Wipe:** It performs a "Clean Sweep" (`aim init`), severing the original A.I.M. Git history and creating a fresh, empty brain.
5. **The Brain Transplant:** It copies the custom `GEMINI.md`, `TOOLS.md`, and `engrams/` from the `agents/python-architect/` blueprint into the new clone.
6. The new Sovereign Agent is now a fully weaponized, highly-specialized A.I.M. instance, ready to work.

---

## 3. Communication & Execution (The Tmux Injection Protocol)
The Swarm is coordinated by the Orchestrator using **Tmux Injection**.

1. **Instantiation:** The Orchestrator reads a `SWARM_MANIFEST.json` and spins up a detached `tmux` session with multiple panes.
2. **Isolation:** In Pane 1, it changes directories to `teams/python-architect-1/` and boots the agent using its localized A.I.M. alias (or the raw `gemini` CLI wrapped in the A.I.M. ecosystem).
3. **The "Return Address":** When the Orchestrator issues a command to a Sovereign Agent, it explicitly provides its own `tmux` session ID.
   *(e.g., `[Primary Orchestrator (Session: leaddeed-aim)]: Implement the auth module. Reply to this session when complete.`)*
4. **Asynchronous Ping-Back:** When the Sovereign Agent finishes, it uses the `tmux paste-buffer` trick to inject a message *back* into the Orchestrator's chat box, completely eliminating the need for fragile polling loops.

## Conclusion
By treating every Swarm Node as a full A.I.M. installation rather than a dumb terminal, we grant the Swarm unprecedented power. They are not just LLMs chatting; they are autonomous Principal Engineers collaborating, each protected by the strict GitOps and memory frameworks of the A.I.M. Exoskeleton.
