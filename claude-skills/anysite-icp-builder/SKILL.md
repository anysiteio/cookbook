---
name: anysite-icp-builder
description: Build and refine Ideal Customer Profiles (ICP) using real LinkedIn data via AnySite MCP. Analyzes existing customers, identifies patterns, generates scoring criteria, and finds lookalike prospects. Use when user mentions ICP, ideal customer profile, customer analysis, prospect research, LinkedIn analysis, target audience, or customer profiling.
---

# AnySite ICP Builder

Build data-driven Ideal Customer Profiles from LinkedIn data using AnySite MCP tools.

## Overview

This skill transforms manual ICP creation into an automated, data-driven workflow:
1. **Analyze** existing customers' LinkedIn profiles
2. **Extract** common patterns (industries, company sizes, titles, skills)
3. **Generate** scoring criteria and ICP documentation
4. **Find** lookalike prospects matching the ICP

## When to Use This Skill

- Building or refining an Ideal Customer Profile
- Analyzing LinkedIn profiles of existing customers
- Finding common patterns among best customers
- Creating prospect scoring criteria
- Discovering lookalike companies/people
- Researching target market segments

## Prerequisites

- AnySite MCP server connected with LinkedIn access
- List of existing customer LinkedIn URLs (profiles or companies)

---

## Phase 1: ICP Discovery Interview

Ask the user these questions to gather context:

### Required Questions (ask first)
1. **Customer URLs**: "Please provide LinkedIn URLs of 5-15 of your best existing customers (profiles or company pages)"
2. **Product/Service**: "What problem does your product solve? Who benefits most?"

### Optional Questions (ask if not provided)
3. **Deal Size**: "What's your typical deal size or ACV?"
4. **Sales Cycle**: "How long is your typical sales cycle?"
5. **Geographic Focus**: "Any geographic restrictions (US, EU, APAC, etc.)?"
6. **Exclusions**: "Any industries or company types to exclude?"

---

## Phase 2: Data Collection

Use AnySite MCP tools to gather data:

### For LinkedIn Profile URLs (individuals)
```
Tools to use:
- Anysite:get_linkedin_profile - Get full profile with experience, education, skills
- Anysite:get_linkedin_user_posts - Analyze recent activity and interests
- Anysite:get_linkedin_user_experience - Detailed work history
```

### For LinkedIn Company URLs
```
Tools to use:
- Anysite:get_linkedin_company - Company details, size, industry
- Anysite:get_linkedin_company_employees - Key employees and roles
- Anysite:get_linkedin_company_employee_stats - Employee distribution data
- Anysite:get_linkedin_company_posts - Company activity and messaging
```

### Data Points to Extract

**From Profiles:**
- Current title and seniority level
- Company name and industry
- Years of experience (total and current role)
- Skills and endorsements
- Education background
- Location
- Recent post topics and engagement

**From Companies:**
- Industry classification
- Employee count range
- Headquarters location
- Company description/tagline
- Specialties/focus areas
- Recent hiring patterns
- Content themes from posts

---

## Phase 3: Pattern Analysis

After collecting data, analyze for patterns:

### Demographic Patterns
```markdown
## Company Demographics
- **Industries**: [List top 3-5 industries with percentages]
- **Company Size**: [Employee range, e.g., "50-500 employees (70%)"]
- **Stage**: [Startup/Growth/Enterprise distribution]
- **Geography**: [Primary regions]
- **Tech Stack Indicators**: [Common technologies mentioned]

## Decision Maker Demographics  
- **Titles**: [Top 5 titles with frequency]
- **Seniority**: [C-level/VP/Director/Manager distribution]
- **Functions**: [Engineering/Sales/Marketing/Product etc.]
- **Tenure**: [Average years in role and at company]
```

### Behavioral Patterns
```markdown
## Engagement Signals
- **Content Interests**: [Topics they post/engage with]
- **Activity Level**: [Posting frequency]
- **Network Size**: [Connection ranges]
- **Group Memberships**: [Common groups/communities]
```

### Firmographic Patterns
```markdown
## Company Characteristics
- **Growth Indicators**: [Hiring, funding, expansion signals]
- **Technology Adoption**: [Tools/platforms mentioned]
- **Business Model**: [B2B/B2C/Marketplace etc.]
- **Maturity Level**: [Years in business, funding stage]
```

---

## Phase 4: ICP Document Generation

Generate a comprehensive ICP document with this structure:

```markdown
# Ideal Customer Profile: [Company Name]

## Executive Summary
[2-3 sentence overview of ideal customer]

## Company Profile

### Must-Have Criteria (Hard Requirements)
| Criterion | Requirement | Weight |
|-----------|-------------|--------|
| Industry | [Specific industries] | 25% |
| Company Size | [Employee range] | 20% |
| Geography | [Regions] | 15% |
| [Custom] | [Requirement] | X% |

### Nice-to-Have Criteria (Soft Requirements)
| Criterion | Preference | Weight |
|-----------|------------|--------|
| Tech Stack | [Technologies] | 10% |
| Growth Stage | [Funding/stage] | 10% |
| [Custom] | [Preference] | X% |

## Decision Maker Profile

### Primary Buyer Persona
- **Title**: [Most common title]
- **Seniority**: [Level]
- **Function**: [Department]
- **Responsibilities**: [Key duties]
- **Pain Points**: [Problems they face]
- **Success Metrics**: [What they're measured on]

### Secondary Influencers
[List other roles involved in buying decision]

## Scoring Model

### Prospect Scoring (100 points max)

**Company Fit (50 points)**
- Industry exact match: 20 pts
- Industry adjacent: 10 pts
- Company size in range: 15 pts
- Geographic match: 10 pts
- Tech stack match: 5 pts

**Contact Fit (30 points)**
- Title exact match: 15 pts
- Title similar: 8 pts
- Seniority match: 10 pts
- Function match: 5 pts

**Engagement Signals (20 points)**
- Recent relevant activity: 10 pts
- Content engagement: 5 pts
- Network overlap: 5 pts

### Score Interpretation
- **80-100**: Hot prospect - prioritize outreach
- **60-79**: Warm prospect - add to nurture
- **40-59**: Cool prospect - monitor for signals
- **Below 40**: Low priority - deprioritize

## Anti-ICP (Exclusion Criteria)
- [Industry/type to avoid]
- [Company characteristics that don't fit]
- [Red flags to watch for]

## Validated Against
- [X] customers analyzed
- Analysis date: [Date]
- Data source: LinkedIn via AnySite MCP
```

---

## Phase 5: Prospect Discovery

Use the ICP to find lookalike prospects:

### Search Strategies

**By Company Attributes:**
```
Tool: Anysite:search_linkedin_companies
Parameters:
- industry: [From ICP]
- employee_count: [Size range]
- location: [Geography]
- keywords: [Industry terms]
```

**By Decision Maker Profile:**
```
Tool: Anysite:search_linkedin_users
Parameters:
- title: [Target title]
- company_keywords: [Industry/type]
- location: [Geography]
- keywords: [Relevant terms]
```

**By Company Employees:**
```
Tool: Anysite:get_linkedin_company_employees
Parameters:
- companies: [Target company URNs]
- keywords: [Title keywords]
```

### Prospect Enrichment

For each discovered prospect:
1. Fetch full profile/company data
2. Apply scoring model
3. Calculate fit score
4. Identify personalization hooks

---

## Output Formats

### ICP Summary Report
Save as: `icp-report-[company]-[date].md`

### Prospect List
Save as: `prospects-[company]-[date].json`

```json
{
  "icp_version": "1.0",
  "generated_date": "YYYY-MM-DD",
  "prospects": [
    {
      "name": "Company/Person Name",
      "linkedin_url": "URL",
      "score": 85,
      "score_breakdown": {
        "company_fit": 45,
        "contact_fit": 25,
        "engagement": 15
      },
      "match_reasons": ["Industry match", "Title match"],
      "personalization_hooks": ["Recent post about X", "Hiring for Y"]
    }
  ]
}
```

---

## Example Workflow

```
User: "Help me build an ICP based on my best customers"

Claude:
1. Ask for customer LinkedIn URLs
2. Collect data using AnySite MCP tools
3. Analyze patterns across all profiles
4. Generate ICP document with scoring model
5. Optionally: Search for lookalike prospects
6. Output: ICP report + prospect list
```

---

## Best Practices

1. **Minimum Sample Size**: Analyze at least 5 customers for reliable patterns
2. **Mix of Data**: Include both "best" customers and "average" ones for contrast
3. **Regular Updates**: Refresh ICP quarterly as customer base evolves
4. **Validate with Sales**: Cross-check patterns with sales team knowledge
5. **Iterate**: Start broad, narrow down based on conversion data

---

## Integration with AnySite Tools

This skill leverages these AnySite MCP capabilities:

| Tool | Purpose |
|------|---------|
| `get_linkedin_profile` | Full profile extraction |
| `get_linkedin_company` | Company details |
| `get_linkedin_company_employees` | Find key contacts |
| `get_linkedin_company_employee_stats` | Org structure |
| `get_linkedin_user_posts` | Activity analysis |
| `get_linkedin_user_experience` | Career history |
| `search_linkedin_users` | Find lookalikes |
| `search_linkedin_companies` | Discover targets |

---

## Troubleshooting

**Issue**: Not enough data for pattern analysis
**Solution**: Request more customer URLs or include adjacent customers

**Issue**: Patterns too broad/generic
**Solution**: Focus on "best" customers only (highest ACV, fastest close)

**Issue**: No prospects found matching criteria
**Solution**: Relax secondary criteria, expand geography, broaden industries

---

## Version History

- v1.0 (January 2026): Initial release with core ICP building workflow
