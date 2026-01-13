# AnySite MCP Endpoints Reference

Complete endpoint documentation for deep universal search. Reference when you need parameter details or cascade patterns.

## Platform Coverage

| Platform | Tools | Primary Use |
|----------|-------|-------------|
| LinkedIn | 24 | Professional profiles, companies, activity |
| Twitter/X | 5 | Real-time opinions, public discussions |
| Instagram | 8 | Personal brand, visual content |
| Reddit | 3 | Community sentiment, technical discussions |
| Y Combinator | 3 | Startup intelligence, founder research |
| Web | 3 | News, articles, general research |

---

## LinkedIn Endpoints (24 tools)

### Search & Discovery

**search_linkedin_users**
```json
{
  "keywords": "string",        // General search terms
  "first_name": "string",      // Exact first name
  "last_name": "string",       // Exact last name
  "title": "string",           // Job title filter
  "company_keywords": "string", // Company name filter
  "location": "string",        // Location filter
  "school_keywords": "string", // Education filter
  "count": 10                  // Max results (default: 10)
}
```
**Use for:** Finding people by name, role, company

**search_linkedin_companies**
```json
{
  "keywords": "string",         // Company name/keywords
  "location": "string",         // Location filter
  "industry": "string",         // Industry filter
  "employee_count": ["string"], // Size filters: "1-10", "11-50", etc.
  "count": 10                   // Max results
}
```
**Use for:** Finding companies by name, industry, size

**search_linkedin_sales_navigator_users**
```json
{
  "count": 10,
  "keywords": "string",
  "current_titles": ["string"],
  "past_titles": ["string"],
  "current_company_names": ["string"],
  "past_company_names": ["string"],
  "location_names": ["string"],
  "education_names": ["string"],
  "seniority_levels": ["Entry", "Manager", "Director", "VP", "CXO"],
  "company_sizes": ["1-10", "11-50", "51-200", "201-500", "501-1000", "1001+"],
  "years_in_current_company": ["0-1", "2-5", "6-10", "10+"],
  "years_in_current_position": ["0-1", "2-5", "6-10", "10+"]
}
```
**Use for:** Advanced people search with precise filters (Sales Navigator)

### Profile Retrieval

**get_linkedin_profile**
```json
{
  "user": "linkedin-username-or-url",
  "with_experience": true,
  "with_education": true,
  "with_skills": true
}
```
**Returns:** Full profile with experience, education, skills, summary
**Critical:** Extract URN (`urn:li:fsd_profile:ACoAAA...`) for subsequent calls

**get_linkedin_company**
```json
{
  "company": "company-slug-or-url"
}
```
**Returns:** Company overview, size, industry, description, specialties

### Activity Analysis

**get_linkedin_user_posts**
```json
{
  "urn": "urn:li:fsd_profile:ACoAAA...",  // MUST use full URN
  "count": 20
}
```
**Critical:** Always use complete URN format from profile, NOT URL

**get_linkedin_user_comments**
```json
{
  "urn": "urn:li:fsd_profile:ACoAAA...",
  "count": 30
}
```

**get_linkedin_user_reactions**
```json
{
  "urn": "urn:li:fsd_profile:ACoAAA...",
  "count": 50
}
```

**get_linkedin_company_posts**
```json
{
  "urn": "urn:li:company:...",  // Company URN from profile
  "count": 20
}
```

### Employee & Team

**get_linkedin_company_employees**
```json
{
  "companies": ["company-slug"],
  "keywords": "engineer OR developer",
  "first_name": "string",
  "last_name": "string",
  "count": 50
}
```
**Use for:** Team analysis, finding specific roles

### Content Search

**search_linkedin_posts**
```json
{
  "keywords": "topic keywords",
  "count": 20
}
```
**Use for:** Topic research, industry trends

## Twitter/X Endpoints (5 tools)

**search_twitter_users**
```json
{
  "query": "name OR @handle",
  "count": 10
}
```

**get_twitter_user**
```json
{
  "user": "username"  // Without @
}
```
**Returns:** Profile, followers, following, bio, verification status

**get_twitter_user_posts**
```json
{
  "user": "username",
  "count": 50
}
```
**Returns:** Recent tweets with engagement metrics

**search_twitter_posts**
```json
{
  "query": "search terms OR @handle",
  "count": 50
}
```
**Use for:** Mentions, sentiment analysis, topic research

## Instagram Endpoints (8 tools)

**get_instagram_user**
```json
{
  "username": "handle"
}
```
**Returns:** Profile, followers, following, bio, post count

**get_instagram_user_posts**
```json
{
  "user": "username",
  "count": 20
}
```

**search_instagram_posts**
```json
{
  "query": "#hashtag OR keyword",
  "count": 10
}
```

**get_instagram_user_friendships**
```json
{
  "user": "username",
  "type": "followers" | "following",
  "count": 50
}
```

## Reddit Endpoints (3 tools)

**search_reddit_posts**
```json
{
  "query": "search terms",
  "subreddit": "specific_sub",  // Optional
  "count": 30
}
```
**Use for:** Community sentiment, discussions, opinions

**get_reddit_post**
```json
{
  "post_url": "https://reddit.com/r/..."
}
```

**get_reddit_post_comments**
```json
{
  "post_url": "https://reddit.com/r/..."
}
```

## Web Endpoints (3 tools)

**duckduckgo_search**
```json
{
  "query": "search terms",
  "count": 10
}
```
**Use for:** General web search, news, articles

**parse_webpage**
```json
{
  "url": "https://example.com",
  "only_main_content": true,
  "strip_all_tags": true,
  "extract_contacts": false,
  "social_links_only": false
}
```
**Use for:** Extracting content from specific pages

**get_sitemap**
```json
{
  "url": "https://example.com/sitemap.xml",
  "count": 50
}
```
**Use for:** Discovering all pages on a website

## Y Combinator Endpoints (3 tools)

**search_yc_companies** - Find startups in YC database
```json
{
  "query": "search terms",           // Company name, product, technology
  "batches": ["W24", "S23", "W23"],  // YC batch filters
  "industries": ["B2B", "AI", "Fintech", "Healthcare", "Developer Tools"],
  "regions": ["United States", "Europe", "Asia"],
  "team_size_min": 2,
  "team_size_max": 50,
  "is_hiring": true,                 // Currently hiring
  "top_company": true,               // YC top companies only
  "nonprofit": false,
  "hits_per_page": 100,              // Max results
  "page": 0                          // Pagination
}
```
**Use for:** Finding YC startups by industry, batch, size, hiring status

**Available industries:**
- B2B, B2C, Consumer, Developer Tools, Education
- Fintech, Healthcare, AI/ML, SaaS, Marketplace
- Hardware, Biotech, Climate, Gaming, Crypto

**Available batches:** W24, S23, W23, S22, W22... (format: Season + Year)

**search_yc_founders** - Find YC founders
```json
{
  "query": "name or keyword",
  "batches": ["W24", "S23"],
  "industries": ["AI", "B2B"],
  "titles": ["CEO", "CTO", "Founder", "Co-Founder"],
  "top_company": true,
  "hits_per_page": 100,
  "page": 0
}
```
**Use for:** Finding founders by name, expertise, or company characteristics

**get_yc_company** - Full YC company details
```json
{
  "company": "company-slug"  // From search results
}
```
**Returns:**
- Company name, description, one-liner
- Batch (e.g., "W24")
- Status (Active, Acquired, Dead)
- Team size
- Founders (names, LinkedIn URLs, Twitter handles)
- Website, social links
- Industries, tags
- Funding info (if available)

---

## Cascade Patterns

### PERSON → COMPANY Cascade
```
1. get_linkedin_profile → extract company slug
2. get_linkedin_company(company=slug)
3. get_linkedin_company_posts(urn=company_urn, count=20)
4. search_yc_companies(query=company_name)
5. parse_webpage(url=company_website)
6. duckduckgo_search(query="company funding news")
```

### COMPANY → LEADERSHIP Cascade
```
1. get_linkedin_company → extract company slug
2. get_linkedin_company_employees(companies=[slug], keywords="founder CEO CTO", count=10)
3. For each leader:
   - get_linkedin_profile(user=username)
   - get_linkedin_user_posts(urn=user_urn, count=20)
   - search_twitter_users(query=name) → get_twitter_user_posts
4. search_yc_founders(query=company_name)
```

### TOPIC → ENTITIES Cascade
```
1. Collect all mentions from search results
2. Extract top mentioned people → PERSON mini-search
3. Extract top mentioned companies → COMPANY mini-search
4. search_yc_companies(industries=[related_industry])
5. search_yc_founders(industries=[related_industry])
```

### Full Entity Graph
```
PERSON
  ├── LinkedIn Profile
  ├── LinkedIn Activity (posts, comments, reactions)
  ├── Twitter Profile + Posts
  ├── Reddit Activity
  ├── Web Presence (articles, talks)
  └── CASCADE: Current Company
        ├── LinkedIn Company
        ├── Company Posts
        ├── Website Analysis
        ├── YC Status Check
        └── Key Colleagues (top 3)

COMPANY
  ├── LinkedIn Company
  ├── Company Posts
  ├── Employee Stats
  ├── Website (home, about, pricing, team)
  ├── Twitter + Posts
  ├── Reddit Discussions
  ├── News (funding, products)
  ├── YC Profile (if applicable)
  └── CASCADE: Leadership Team
        ├── Founders (full profiles)
        ├── C-Level (full profiles)
        └── Their Activity

TOPIC
  ├── Web Search (news, articles)
  ├── LinkedIn Posts
  ├── Twitter Discussions
  ├── Reddit Threads
  ├── Instagram Content
  ├── YC Startups in Space
  └── CASCADE: Key Entities
        ├── Top People Mentioned
        └── Top Companies Mentioned
```

---

## Common Patterns

### Full PERSON Analysis (with cascade)
```
# Phase 1: Find person
search_linkedin_users(keywords="Name Company")
# If YC founder suspected:
search_yc_founders(query="Name")

# Phase 2: Deep profile
get_linkedin_profile(user=username, with_experience=true, with_education=true, with_skills=true)
# SAVE: urn:li:fsd_profile:ACoAAA... for all subsequent calls

# Phase 3: Activity
get_linkedin_user_posts(urn=full_urn, count=50)
get_linkedin_user_comments(urn=full_urn, count=30)
get_linkedin_user_reactions(urn=full_urn, count=50)

# Phase 4: Cross-platform
search_twitter_users(query="Name Company")
get_twitter_user(user=handle)
get_twitter_user_posts(user=handle, count=100)
search_reddit_posts(query="Name OR username", count=20)
duckduckgo_search(query="Name Company speaker interview article", count=10)
duckduckgo_search(query="Name site:github.com OR site:medium.com", count=10)

# Phase 5: CASCADE → Company
get_linkedin_company(company=company_slug_from_profile)
get_linkedin_company_posts(urn=company_urn, count=20)
parse_webpage(url=company_website)
parse_webpage(url=company_website+"/about")
search_yc_companies(query=company_name)
duckduckgo_search(query="Company funding news 2024", count=10)

# Phase 6: CASCADE → Colleagues
get_linkedin_company_employees(companies=[slug], keywords="founder CEO CTO VP", count=10)
# Brief profile on top 2-3
```

### Full COMPANY Analysis (with cascade)
```
# Phase 1: Find company
search_linkedin_companies(keywords="Company Name")
search_yc_companies(query="Company Name")

# Phase 2: Company profile
get_linkedin_company(company=slug)
get_linkedin_company_employee_stats(urn=company_urn)
get_linkedin_company_posts(urn=company_urn, count=30)

# Phase 3: Website
parse_webpage(url="https://domain.com")
parse_webpage(url="https://domain.com/about")
parse_webpage(url="https://domain.com/pricing")
parse_webpage(url="https://domain.com/team")
get_sitemap(url="https://domain.com/sitemap.xml", count=50)

# Phase 4: Social presence
search_twitter_users(query="Company Name")
get_twitter_user(user=handle)
get_twitter_user_posts(user=handle, count=50)
search_twitter_posts(query="Company OR @handle", count=100)
search_reddit_posts(query="Company Name", count=50)
search_instagram_posts(query="#Company", count=20)  # if B2C

# Phase 5: News & external
duckduckgo_search(query="Company funding news", count=10)
duckduckgo_search(query="Company launch product announcement", count=10)
duckduckgo_search(query="Company review alternative competitor", count=10)
# Parse top 3-5 articles

# Phase 6: YC check
search_yc_companies(query="Company")
get_yc_company(company=yc_slug)  # if found
search_yc_founders(query="Company")

# Phase 7: CASCADE → Leadership
get_linkedin_company_employees(companies=[slug], keywords="founder", count=10)
get_linkedin_company_employees(companies=[slug], keywords="CEO CTO CPO CFO", count=10)
# For top 5 leaders:
get_linkedin_profile(user=username, with_experience=true)
get_linkedin_user_posts(urn=user_urn, count=20)
search_twitter_users(query="Leader Name")
get_twitter_user_posts(user=leader_handle, count=30)
```

### Full TOPIC Analysis (with cascade)
```
# Phase 1: Web overview
duckduckgo_search(query="topic keywords", count=15)
duckduckgo_search(query="topic trends 2024 2025", count=10)
duckduckgo_search(query="topic news recent", count=10)
# Parse top 5 authoritative sources

# Phase 2: Professional (LinkedIn)
search_linkedin_posts(keywords="topic", count=30)
search_linkedin_companies(keywords="topic related", count=20)
search_linkedin_users(keywords="topic expert", count=10)

# Phase 3: Real-time (Twitter)
search_twitter_posts(query="topic", count=100)
search_twitter_posts(query="topic #hashtag", count=50)
search_twitter_users(query="topic expert", count=10)

# Phase 4: Community (Reddit)
search_reddit_posts(query="topic", count=50)
search_reddit_posts(query="topic", subreddit="relevant_sub", count=30)
# Get comments on top 3 threads

# Phase 5: Visual (Instagram)
search_instagram_posts(query="#topic_hashtag", count=20)

# Phase 6: Startups (YC)
search_yc_companies(query="topic", industries=["relevant"], hits_per_page=50)
# Get details on top 5 YC companies
search_yc_founders(query="topic", industries=["relevant"])

# Phase 7: CASCADE → Key entities
# Extract most mentioned people → PERSON mini-search
# Extract most mentioned companies → COMPANY mini-search
```

## Error Handling

**Common issues:**

1. **"Profile not found"** → Try URL variations, search by name
2. **"Invalid URN"** → Use full `urn:li:fsd_profile:ACoAAA...` format
3. **"Rate limited"** → Wait and retry, or continue with partial data
4. **"No results"** → Broaden search terms, try alternative spellings
5. **"Access denied"** → Some profiles are private, note in report

**URN formats:**
- User: `urn:li:fsd_profile:ACoAAA...`
- Company: `urn:li:company:12345`
- Post: `urn:li:activity:12345...`
