---
name: universal-search
description: Deep multi-platform intelligence search across ALL AnySite MCP sources (LinkedIn, Twitter, Instagram, Reddit, Y Combinator, web). Auto-detects search type (person, company, or topic) and performs CASCADING research - person searches include their company analysis, company searches include leadership profiles, topic searches aggregate facts from all platforms. Use when users ask to "find", "search", "research", "investigate", or need comprehensive intelligence on any subject. Produces detailed reports with cross-validated findings and source links.
---

# Universal Deep Search

Comprehensive intelligence gathering across ALL available data sources with cascading analysis.

## Core Principle: CASCADING SEARCH

Every search expands to related entities:
- **PERSON** → + their company + key colleagues + company news
- **COMPANY** → + founders + C-level team + investors + competitors mentions
- **TOPIC** → + key people mentioned + companies involved + YC startups in space

## Query Classification

### Type 1: PERSON
**Triggers:** Names, roles ("CEO of"), profile URLs, "who is", "find person"

**Context to extract:**
- Full name (required)
- Company (helpful)
- Role/title (helpful)
- Location (helpful)

### Type 2: COMPANY
**Triggers:** Company names, domains (.io, .com), "startup", "company", linkedin.com/company/

**Context to extract:**
- Company name (required)
- Domain (helpful)
- Industry (helpful)
- Location (helpful)

### Type 3: TOPIC
**Triggers:** Abstract concepts, questions, hashtags, "news about", "trends in"

**Context to extract:**
- Keywords (required)
- Time frame (helpful)
- Industry/niche (helpful)

---

## PERSON Search Workflow

### Phase 1: Find & Identify Person

```
1. search_linkedin_users
   - keywords: "[name]"
   - company_keywords: "[company]" if known
   - title: "[role]" if known
   - count: 10

2. If multiple matches → present top 5 for confirmation
3. If YC founder suspected → search_yc_founders(query="[name]")
```

### Phase 2: Deep Profile Analysis

```
1. get_linkedin_profile
   - user: "[username or URL]"
   - with_experience: true
   - with_education: true
   - with_skills: true
   
   CRITICAL: Extract and save:
   - Full URN: urn:li:fsd_profile:ACoAAA...
   - Current company slug/URN
   - Current role & start date

2. get_linkedin_user_posts
   - urn: "[full URN from above]"
   - count: 50
   
3. get_linkedin_user_comments
   - urn: "[full URN]"
   - count: 30

4. get_linkedin_user_reactions
   - urn: "[full URN]"
   - count: 50
```

### Phase 3: Cross-Platform Presence

```
1. search_twitter_users
   - query: "[name] [company]"
   - count: 5
   
2. get_twitter_user (if found)
   - user: "[handle]"

3. get_twitter_user_posts
   - user: "[handle]"
   - count: 100

4. search_reddit_posts
   - query: "[name] OR [username]"
   - count: 20

5. get_instagram_user (if B2C/personal brand)
   - username: "[handle]"

6. duckduckgo_search
   - query: "[name] [company] speaker OR interview OR article OR podcast"
   - count: 10

7. duckduckgo_search
   - query: "[name] site:github.com OR site:medium.com OR site:substack.com"
   - count: 10
```

### Phase 4: CASCADE → Company Analysis

**Always analyze person's current company:**

```
1. get_linkedin_company
   - company: "[company slug from profile]"

2. get_linkedin_company_posts
   - urn: "[company URN]"
   - count: 20

3. parse_webpage
   - url: "[company website]"
   - only_main_content: true

4. parse_webpage
   - url: "[company website]/about"

5. search_yc_companies (check if YC company)
   - query: "[company name]"

6. duckduckgo_search
   - query: "[company] funding news 2024 2025"
   - count: 10
```

### Phase 5: CASCADE → Key Colleagues

```
1. get_linkedin_company_employees
   - companies: ["[company slug]"]
   - keywords: "founder OR CEO OR CTO OR VP"
   - count: 10

2. For top 2-3 executives:
   - get_linkedin_profile (brief)
```

---

## COMPANY Search Workflow

### Phase 1: Find & Identify Company

```
1. search_linkedin_companies
   - keywords: "[company name]"
   - location: "[location]" if known
   - industry: "[industry]" if known
   - count: 10

2. search_yc_companies
   - query: "[company name]"
   - hits_per_page: 20

3. If multiple matches → present options for confirmation
```

### Phase 2: Deep Company Profile

```
1. get_linkedin_company
   - company: "[slug]"
   
   Extract: URN, employee count, industry, description

2. get_linkedin_company_employee_stats
   - urn: "[company URN]"

3. get_linkedin_company_posts
   - urn: "[company URN]"
   - count: 30
```

### Phase 3: Website Intelligence

```
1. parse_webpage (homepage)
   - url: "https://[domain]"
   - only_main_content: true
   - extract_contacts: true

2. parse_webpage (about)
   - url: "https://[domain]/about"

3. parse_webpage (pricing)
   - url: "https://[domain]/pricing"

4. parse_webpage (team/leadership)
   - url: "https://[domain]/team" OR "/about#team"

5. get_sitemap
   - url: "https://[domain]/sitemap.xml"
   - count: 50
```

### Phase 4: Social & Community Presence

```
1. search_twitter_users
   - query: "[company name]"
   - count: 5

2. get_twitter_user
   - user: "[company handle]"

3. get_twitter_user_posts
   - user: "[handle]"
   - count: 50

4. search_twitter_posts
   - query: "[company] OR @[handle]"
   - count: 100

5. search_reddit_posts
   - query: "[company name]"
   - count: 50

6. search_reddit_posts
   - query: "[company name]"
   - subreddit: "[relevant sub]" (e.g., "startups", "SaaS", industry-specific)
   - count: 30

7. search_instagram_posts (if B2C)
   - query: "#[company] OR [company name]"
   - count: 20
```

### Phase 5: CASCADE → Leadership Team Analysis

**Always analyze founders and C-level:**

```
1. get_linkedin_company_employees
   - companies: ["[slug]"]
   - keywords: "founder"
   - count: 10

2. get_linkedin_company_employees
   - companies: ["[slug]"]
   - keywords: "CEO OR CTO OR CPO OR CFO OR COO"
   - count: 10

3. For each founder/C-level (top 5):
   a. get_linkedin_profile
      - with_experience: true
      - with_education: true
      - with_skills: true
   
   b. get_linkedin_user_posts
      - count: 20
   
   c. search_twitter_users → get_twitter_user_posts
      - count: 30

4. search_yc_founders
   - query: "[founder names]"
```

### Phase 6: News & External Intelligence

```
1. duckduckgo_search
   - query: "[company] funding news"
   - count: 10

2. duckduckgo_search
   - query: "[company] launch product announcement"
   - count: 10

3. duckduckgo_search
   - query: "[company] review OR competitor OR alternative"
   - count: 10

4. parse_webpage (top news articles)
   - Parse 3-5 most relevant results

5. If tech company:
   duckduckgo_search
   - query: "[company] site:github.com"
   - count: 5
```

### Phase 7: Y Combinator Check

```
1. search_yc_companies
   - query: "[company name]"

2. If found:
   get_yc_company
   - company: "[slug]"
   
   Extract: batch, status, funding, team size, founders

3. search_yc_founders
   - query: "[company name]"
```

---

## TOPIC Search Workflow

### Phase 1: Web Overview

```
1. duckduckgo_search
   - query: "[topic keywords]"
   - count: 15

2. duckduckgo_search
   - query: "[topic] trends 2024 2025"
   - count: 10

3. duckduckgo_search
   - query: "[topic] news recent"
   - count: 10

4. parse_webpage
   - Parse top 5 most authoritative results
```

### Phase 2: Professional Discussion (LinkedIn)

```
1. search_linkedin_posts
   - keywords: "[topic]"
   - count: 30

2. search_linkedin_companies
   - keywords: "[topic] OR [related terms]"
   - count: 20

3. search_linkedin_users
   - keywords: "[topic] expert OR thought leader"
   - count: 10
```

### Phase 3: Real-time Sentiment (Twitter)

```
1. search_twitter_posts
   - query: "[topic]"
   - count: 100

2. search_twitter_posts
   - query: "[topic] #[hashtag]"
   - count: 50

3. search_twitter_users
   - query: "[topic] expert"
   - count: 10
```

### Phase 4: Community Insights (Reddit)

```
1. search_reddit_posts
   - query: "[topic]"
   - count: 50

2. search_reddit_posts
   - query: "[topic]"
   - subreddit: "[most relevant sub]"
   - count: 30

3. get_reddit_post_comments (on popular posts)
   - Parse top 3 most discussed threads
```

### Phase 5: Visual Content (Instagram)

```
1. search_instagram_posts
   - query: "#[topic_hashtag]"
   - count: 20
```

### Phase 6: Startup Landscape (Y Combinator)

```
1. search_yc_companies
   - query: "[topic]"
   - industries: ["[related industry]"]
   - hits_per_page: 50

2. For top 5 relevant YC companies:
   get_yc_company
   - company: "[slug]"

3. search_yc_founders
   - query: "[topic]"
   - industries: ["[related industry]"]
```

### Phase 7: CASCADE → Key Entities

**Identify and analyze key people/companies mentioned:**

```
1. From all collected data, extract:
   - Most mentioned people → run PERSON mini-analysis
   - Most mentioned companies → run COMPANY mini-analysis

2. Mini-analysis (for each top entity):
   - LinkedIn profile/company
   - Recent posts
   - Twitter presence
```

---

## Validation & Cross-Referencing

### For PERSON
- Name matches across platforms
- Company/role consistency
- Profile photo verification (same person)
- Timeline consistency (career progression)

### For COMPANY
- Domain matches LinkedIn company
- Employee count consistency
- Founding date alignment
- Industry classification match

### For TOPIC
- Source authority ranking
- Recency weighting
- Cross-source fact verification
- Sentiment consistency

### Confidence Scoring
- **HIGH**: 4+ validation points, consistent across 3+ platforms
- **MEDIUM**: 2-3 validation points, minor inconsistencies
- **LOW**: 1 validation point or significant conflicts

---

## Output Format

```markdown
# Deep Search Report: [Subject]

**Type:** PERSON / COMPANY / TOPIC
**Query:** [Original query]
**Confidence:** HIGH / MEDIUM / LOW
**Platforms Searched:** [list all]
**Total API Calls:** [number]
**Analysis Date:** [date]

---

## Executive Summary

[3-5 key findings in bullet points]

---

## Primary Subject Analysis

### [Subject Name]

[Detailed findings organized by data type]

**Profile:**
[Core facts]

**Activity Analysis:**
[Posts, engagement patterns]

**Cross-Platform Presence:**
[Twitter, Reddit, Instagram, Web findings]

---

## Cascaded Analysis

### [Related Entity 1: Company/Person]
[Key findings from cascade]

### [Related Entity 2: Leadership/Colleagues]
[Key findings from cascade]

---

## Topic/Industry Context

[For PERSON/COMPANY: industry context]
[For TOPIC: full analysis here]

### YC Landscape
[Relevant YC companies and founders]

### Recent News & Trends
[From web search]

---

## Cross-Platform Synthesis

**Consistent Facts:**
- [Facts verified across multiple sources]

**Platform-Specific Insights:**
- LinkedIn: [professional persona]
- Twitter: [public opinions]
- Reddit: [community engagement]
- Instagram: [personal brand]

**Inconsistencies/Flags:**
- [Any conflicts to note]

---

## Sources

| # | Platform | URL | Type | Freshness |
|---|----------|-----|------|-----------|
| 1 | LinkedIn | [link] | Profile | Current |
| 2 | Twitter | [link] | Posts | Last 30d |
| 3 | Reddit | [link] | Discussion | Last 7d |
| 4 | YC | [link] | Company | Current |
| 5 | Web | [link] | Article | [date] |

---

## Metadata

- Platforms: LinkedIn, Twitter, Reddit, Instagram, YC, Web
- Data Points Collected: ~[number]
- Validation Status: PASSED / PARTIAL / NEEDS_REVIEW
- Cascade Depth: [how many related entities analyzed]
```

---

## Quick Reference: All Endpoints Used

### LinkedIn (24 tools)
- `search_linkedin_users` - find people
- `search_linkedin_companies` - find companies
- `search_linkedin_sales_navigator_users` - advanced people search
- `get_linkedin_profile` - person details
- `get_linkedin_company` - company details
- `get_linkedin_company_employees` - team members
- `get_linkedin_company_posts` - company content
- `get_linkedin_company_employee_stats` - growth data
- `get_linkedin_user_posts` - person's posts
- `get_linkedin_user_comments` - person's comments
- `get_linkedin_user_reactions` - person's reactions
- `search_linkedin_posts` - topic search

### Twitter (5 tools)
- `search_twitter_users` - find accounts
- `get_twitter_user` - profile details
- `get_twitter_user_posts` - tweets
- `search_twitter_posts` - topic/mention search

### Instagram (8 tools)
- `get_instagram_user` - profile
- `get_instagram_user_posts` - posts
- `search_instagram_posts` - hashtag/topic search
- `get_instagram_user_friendships` - followers/following

### Reddit (3 tools)
- `search_reddit_posts` - find discussions
- `get_reddit_post` - post details
- `get_reddit_post_comments` - comments

### Y Combinator (3 tools)
- `search_yc_companies` - find startups
- `get_yc_company` - company details
- `search_yc_founders` - find founders

### Web (3 tools)
- `duckduckgo_search` - web search
- `parse_webpage` - extract content
- `get_sitemap` - discover pages

---

## Error Handling

**No results:** Try alternative spellings, broader terms, different platforms
**Rate limits:** Continue with available data, note gaps
**Private profiles:** Note as limitation, use public data
**Multiple matches:** Present options, ask for confirmation

## Search Depth Options

User can request:
- **Quick scan** (10 min): Primary endpoints only, no cascade
- **Standard** (20-30 min): Full workflow, 1-level cascade (DEFAULT)
- **Deep dive** (45-60 min): Extended counts, 2-level cascade, all platforms
