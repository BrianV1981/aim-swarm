# A.I.M. Swarm

A synchronous, terminal-native multi-agent orchestration framework built for `tmux` and the Gemini CLI.

## The Philosophy
While the native A.I.M. architecture relies on background Subagents for deep, invisible delegation, **A.I.M. Swarm** brings the team to the foreground.

By orchestrating agents directly within a `tmux` grid, human operators can visually monitor parallel agent reasoning, dynamically interject into the conversation streams, and physically watch the collaborative process unfold in real-time.

## The Core Mechanisms
1. **Tmux Pane Grids:** Specialized agents operate in isolated terminal panes.
2. **Buffer Injection:** Swarm commands are safely loaded into the `tmux` clipboard (`set-buffer`) and pasted instantly (`paste-buffer`), preventing multiline race conditions.
3. **The Subconscious Escape (`BTab Enter`):** Prompts are officially submitted using `Shift+Tab` followed by `Enter` to escape the Gemini CLI's interactive UI.
4. **Git Worktree Isolation:** (Coming Soon) Each pane will operate within its own `git worktree` to prevent file system collisions when multiple agents attempt to modify the codebase simultaneously.

## Usage
`python3 aim_swarm.py --help`
