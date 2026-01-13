# AnySite ICP Builder

> Build data-driven Ideal Customer Profiles from LinkedIn data using AnySite MCP

## Overview

Transform manual ICP creation into an automated, data-driven workflow:

1. **Analyze** existing customers' LinkedIn profiles via AnySite MCP
2. **Extract** common patterns (industries, company sizes, titles, skills)
3. **Generate** scoring criteria and ICP documentation
4. **Find** lookalike prospects matching the ICP

## Features

🎯 **ICP-Driven Research**: Analyze real customer data, not assumptions
🤖 **AI-Powered Discovery**: Automated pattern extraction from LinkedIn
📊 **Smart Scoring**: 100-point algorithm prioritizes prospects by fit
🔗 **Native AnySite Integration**: Uses AnySite MCP for all LinkedIn data
📁 **Multiple Outputs**: Markdown reports + JSON configs + Prospect lists

## Prerequisites

- [Claude Code](https://claude.ai/code) or Claude AI with skills support
- [AnySite MCP](https://anysite.io) server connected
- LinkedIn URLs of 5-15 existing customers

## Installation

### Option 1: Claude Code Plugin (Recommended)

```bash
# Add as plugin
/plugin marketplace add anysite/icp-builder

# Or install manually
/plugin add /path/to/anysite-icp-builder
```

### Option 2: Manual Installation

```bash
# Clone or download the skill
git clone https://github.com/anysite/icp-builder.git

# Copy to Claude skills directory
cp -r anysite-icp-builder ~/.claude/skills/

# Copy command
cp -r anysite-icp-builder/commands/* ~/.claude/commands/
```

### Option 3: Claude.ai Upload

1. Go to Claude.ai → Settings → Skills
2. Click "Upload Custom Skill"
3. Select the `anysite-icp-builder` folder
4. Skill will auto-activate when relevant

## Usage

### Quick Start

```
User: Help me build an ICP from my customers

Claude: I'll help you build an Ideal Customer Profile. Please share LinkedIn URLs 
of 5-15 of your best customers (profiles or company pages).

User: https://linkedin.com/in/customer1, https://linkedin.com/company/acme

Claude: [Fetches data via AnySite MCP, analyzes patterns, generates ICP]
```

### Slash Command

```
/icp-build https://linkedin.com/in/cust1, https://linkedin.com/in/cust2
```

### Detailed Workflow

1. **Provide customer URLs**: LinkedIn profile or company URLs
2. **Answer context questions**: Product, deal size, geography
3. **Review patterns**: Claude shows extracted patterns for validation
4. **Get ICP document**: Full report with scoring model
5. **Optional: Find prospects**: Discover lookalike companies/people

## Output Files

| File | Description |
|------|-------------|
| `icp-report-[company]-[date].md` | Full ICP report with scoring model |
| `icp-config-[company]-[date].json` | Machine-readable ICP configuration |
| `prospects-[company]-[date].json` | Scored prospect list |

## AnySite MCP Tools Used

| Tool | Purpose |
|------|---------|
| `get_linkedin_profile` | Extract full profile data |
| `get_linkedin_company` | Company details, size, industry |
| `get_linkedin_company_employees` | Key contacts at company |
| `get_linkedin_user_posts` | Activity and content interests |
| `search_linkedin_users` | Find lookalike decision makers |
| `search_linkedin_companies` | Discover target companies |

## Scoring Model

### Company Fit (50 points)
- Industry exact match: 20 pts
- Company size in range: 15 pts
- Geographic match: 10 pts
- Tech stack match: 5 pts

### Contact Fit (30 points)
- Title exact/similar: 15/8 pts
- Seniority match: 10 pts
- Function match: 5 pts

### Engagement Signals (20 points)
- Recent activity: 10 pts
- Skill overlap: 5 pts
- Content relevance: 5 pts

### Tiers
| Score | Tier | Action |
|-------|------|--------|
| 80-100 | 🔥 Hot | Prioritize outreach |
| 60-79 | 🌡️ Warm | Add to nurture |
| 40-59 | ❄️ Cool | Monitor for signals |
| <40 | ⬇️ Low | Deprioritize |

## File Structure

```
anysite-icp-builder/
├── SKILL.md              # Main skill instructions
├── README.md             # This file
├── commands/
│   └── icp-build.md      # Slash command definition
├── scripts/
│   └── icp_analyzer.py   # Python analysis tools
├── templates/
│   ├── icp-report-template.md
│   └── prospect-list-schema.json
└── resources/
    └── industry-keywords.json
```

## Examples

### Example ICP Output

```markdown
# Ideal Customer Profile: AnySite

## Executive Summary
AnySite's ideal customer is a Series A-C B2B SaaS company with 50-500 employees, 
primarily in AI/ML or developer tools space, led by technical founders.

## Company Criteria

### Must-Have
| Criterion | Requirement | Weight |
|-----------|-------------|--------|
| Industry | AI/ML, Developer Tools, Data Infrastructure | 25% |
| Size | 50-500 employees | 20% |
| Stage | Series A-C | 15% |

## Decision Maker Profile
**Title**: VP Engineering, CTO, Head of Data
**Seniority**: VP or C-level
**Function**: Engineering, Data
```

## Best Practices

1. **Sample Size**: Analyze at least 5 customers for reliable patterns
2. **Quality over Quantity**: Focus on "best" customers (highest ACV, fastest close)
3. **Regular Updates**: Refresh ICP quarterly
4. **Validate with Sales**: Cross-check patterns with team knowledge
5. **Start Broad**: Narrow criteria based on conversion data

## Troubleshooting

**Issue**: Not enough patterns detected
**Solution**: Add more customer URLs, include adjacent customers

**Issue**: Patterns too generic
**Solution**: Focus only on "best" customers (top 20%)

**Issue**: No prospects found
**Solution**: Relax secondary criteria, expand geography

## Contributing

Contributions welcome! Ideas:
- Additional scoring factors
- Industry-specific templates
- CRM integration
- Automated monitoring

## License

MIT License - see LICENSE file

## Credits

Built for [AnySite](https://anysite.io) - Internet for AI Agents

Based on patterns from:
- [claude-code-exa-gtm](https://github.com/peterkaplan/claude-code-exa-gtm)
- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

---

*AnySite ICP Builder v1.0 - January 2026*
