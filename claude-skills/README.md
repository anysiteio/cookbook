# Claude Code Skills

Custom skills for Claude Code that extend its capabilities with specialized workflows.

## Available Skills

### vc-analyst

Universal VC investor analysis and outreach agent for founders.

**What it does:**
- Onboards your startup (website, pitch deck, stage, round size)
- Scores investors 0-100 based on stage fit, thesis match, portfolio relevance
- Detects portfolio conflicts with your competitors
- Generates personalized outreach messages

**How to use:**

1. Download the `vc-analyst` folder
2. Place it in your `.claude/skills/` directory
3. Run `/vc-analyst` in Claude Code

**Requirements:**
- Claude Code CLI
- Anysite MCP server for LinkedIn data (optional but recommended)

[Full documentation](vc-analyst/SKILL.md)

## Installation

**Option 1: Download packaged skill**
```bash
# Download the .skill file
curl -LO https://github.com/anysiteio/cookbook/raw/main/claude-skills/vc-analyst.skill

# Install (unzip to your skills folder)
unzip vc-analyst.skill -d ~/.claude/skills/
```

**Option 2: Clone and copy**
```bash
# Clone this repo
git clone https://github.com/anysiteio/cookbook.git

# Copy skill to your Claude config
cp -r cookbook/claude-skills/vc-analyst ~/.claude/skills/
```

## About Anysite.io

We build agent-first infrastructure for the web — turning any website into a self-healing API in 60 seconds so AI agents can access the entire internet.

- Website: https://anysite.io
- MCP Server: https://mcp.anysite.io/mcp
