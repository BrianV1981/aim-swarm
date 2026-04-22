# A.I.M. Swarm Issue Ledger

## 🟢 OPEN ISSUES (Actionable)

- [ ] **TKT-003: The Fractal Factory**
  - **Context:** The current factory script only creates directories and basic templates.
  - **Failure:** V3 requires each agent to be a full A.I.M. OS clone with its own isolated environment.
  - **Intent:** Overhaul `aim_spawn.py` to clone the A.I.M. core, run clean sweeps, and inject blueprints.

- [ ] **TKT-004: The Orchestrator Protocol**
  - **Context:** Orchestrator-Agent communication currently lacks structured two-way terminal feedback.
  - **Failure:** Agents don't know the Orchestrator's session ID, hindering direct terminal responses.
  - **Intent:** Update `aim_team.py` to pass the Orchestrator's tmux session ID during agent initialization.

## 🔴 COMPLETED ISSUES (Historical)

- [x] **TKT-005: Project Organization & Role Sealing**
  - **Context:** `aim-swarm` needs to be organized for self-hosting.
  - **Intent:** Moved custom scripts to `swarm/` folder and wrote a tailored `AGENTS.md` defining the role of **Swarm Architect** (Agent who creates agents).

- [x] **TKT-001: Architect and implement the Swarm Subagent System (Sovereign Nodes)**
  - **Context:** `aim-swarm` must be modular and independent. 
  - **Intent:** Initial V2 implementation of aim_spawn and aim_team (now superseded by V3).
ntralized library for specialized agent templates (AGENTS.md, TOOLS.md, engrams/).
  - **Intent:** Establish a 'python-developer' template in 'agents/' to serve as the DNA for new fractal clones.

- [x] **TKT-005: Project Organization & Role Sealing**
  - **Context:** `aim-swarm` needs to be organized for self-hosting.
  - **Intent:** Moved custom scripts to `swarm/` folder and wrote a tailored `AGENTS.md` defining the role of **Swarm Architect** (Agent who creates agents).

- [x] **TKT-001: Architect and implement the Swarm Subagent System (Sovereign Nodes)**
  - **Context:** `aim-swarm` must be modular and independent. 
  - **Intent:** Initial V2 implementation of aim_spawn and aim_team (now superseded by V3).
