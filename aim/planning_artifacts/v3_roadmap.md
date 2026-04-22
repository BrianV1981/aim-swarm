# Roadmap: V3 - Persistent Fractal Teams (Fractal Exoskeletons)

## Objective
Transition from ephemeral agent directories to permanent, specialized "Fractal Exoskeletons" using full A.I.M. installations for each agent.

---

## Ticket 1: The Blueprint Library
**Title:** Implement the `agents/` Blueprint Library  
**Context:** Implementing the 'agents/' directory for the V3 Fractal Teams model.  
**Failure:** Currently lacks a centralized library for specialized agent templates (AGENTS.md, TOOLS.md, engrams/).  
**Intent:** Establish a 'python-developer' template in 'agents/' to serve as the DNA for new fractal clones.  

### Implementation Steps
1. Create `/home/kingb/aim-swarm/agents/` directory.
2. Create `agents/python-developer/` template.
3. Populate `agents/python-developer/AGENTS.md` with specialized Python role instructions.
4. Populate `agents/python-developer/TOOLS.md` with Python-specific tool definitions.
5. Create `agents/python-developer/engrams/` for initial RAG seeding.

---

## Ticket 2: The Fractal Factory
**Title:** Update `aim_spawn.py` to support Fractal Cloning  
**Context:** The current factory script only creates directories and basic templates.  
**Failure:** V3 requires each agent to be a full A.I.M. OS clone with its own isolated environment.  
**Intent:** Overhaul `aim_spawn.py` to clone the A.I.M. core, run clean sweeps, and inject blueprints.  

### Implementation Steps
1. Update `aim_spawn.py` to accept blueprint selection from `agents/`.
2. Implement full `git clone` of the A.I.M. core into the target `teams/` node.
3. Add a headless "Clean Sweep" procedure to reset the clone's cognitive state.
4. Implement Blueprint Injection: copy files from `agents/<blueprint>/` into the new clone.
5. Add cloning of a local `aim-chalkboard` repository into the node's workspace for asynchronous GitOps communication.

---

## Ticket 3: The Orchestrator Protocol
**Title:** Enhance `aim_team.py` with Tmux-to-Tmux Communication  
**Context:** Orchestrator-Agent communication currently lacks structured two-way terminal feedback.  
**Failure:** Agents don't know the Orchestrator's session ID, hindering direct terminal responses.  
**Intent:** Update `aim_team.py` to pass the Orchestrator's tmux session ID during agent initialization.  

### Implementation Steps
1. Update `aim_team.py` to capture its own `tmux` session name/ID.
2. Modify the `gemini boot` command sent to agent panes to include an `--orchestrator-session-id` flag.
3. Verify that agents can successfully "ping" or send keys back to the Orchestrator's session.

---

## Verification & Testing
1. **Blueprint Validation:** Ensure `agents/python-developer/` contains all required DNA files.
2. **Factory Test:** Run `./aim_spawn.py --blueprint python-developer test-agent` and verify a full A.I.M. install exists in `teams/test-agent_node/`.
3. **Orchestration Test:** Run `./aim_team.py` and verify agents receive the Orchestrator session ID in their boot logs.
