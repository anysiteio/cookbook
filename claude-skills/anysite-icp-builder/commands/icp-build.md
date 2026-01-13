# /icp-build - Build Ideal Customer Profile from LinkedIn Data

Build a data-driven Ideal Customer Profile by analyzing your best customers' LinkedIn profiles.

## Arguments

- `$CUSTOMER_URLS` (optional): Comma-separated LinkedIn URLs of existing customers
- `$OUTPUT_FORMAT` (optional): Output format - "report" (default), "json", or "both"

## Instructions

### Phase 1: Gather Input

If customer URLs not provided, ask:
1. "Please share LinkedIn URLs of 5-15 of your best customers (people or companies)"
2. "What problem does your product solve?"
3. "What's your typical deal size?"
4. "Any geographic focus areas?"

### Phase 2: Collect LinkedIn Data

For each provided URL, use AnySite MCP tools:

**For Profile URLs (linkedin.com/in/...):**
```
Use: Anysite:get_linkedin_profile
Extract: title, company, skills, experience, location
```

**For Company URLs (linkedin.com/company/...):**
```
Use: Anysite:get_linkedin_company
Extract: industry, employee_count, location, description
Also use: Anysite:get_linkedin_company_employees (first 10)
```

### Phase 3: Analyze Patterns

After collecting all data, identify:

1. **Company patterns:**
   - Most common industries (top 3)
   - Employee count range (min/median/max)
   - Geographic distribution
   - Common tech/tool mentions

2. **Contact patterns:**
   - Most common titles
   - Seniority levels (C-level, VP, Director, Manager)
   - Functions (Engineering, Sales, Marketing, Product)
   - Common skills

### Phase 4: Generate ICP

Create comprehensive ICP document including:

1. **Executive Summary** (2-3 sentences)
2. **Company Criteria** (must-have vs nice-to-have)
3. **Decision Maker Profile** (primary buyer persona)
4. **Scoring Model** (100-point scale)
5. **Search Queries** (for prospect discovery)

### Phase 5: Optional - Find Prospects

If user wants prospects, use:
```
Anysite:search_linkedin_companies - Find matching companies
Anysite:search_linkedin_users - Find decision makers
```

Score each prospect against the ICP and output prioritized list.

## Output

Save results to:
- `/home/claude/icp-report-[company]-[date].md` - Full report
- `/home/claude/icp-config-[company]-[date].json` - Machine-readable config
- `/home/claude/prospects-[company]-[date].json` - Scored prospect list (if requested)

## Example Usage

```
User: /icp-build
Claude: I'll help you build an ICP. Please share LinkedIn URLs of 5-15 of your best customers...

User: /icp-build https://linkedin.com/in/customer1, https://linkedin.com/company/customer2
Claude: Great, analyzing 2 customers... [proceeds with analysis]
```

## Best Practices

1. Include 5+ customers for reliable patterns
2. Focus on "best" customers (highest ACV, fastest close)
3. Mix of company and profile URLs gives richer data
4. Run quarterly to keep ICP fresh
