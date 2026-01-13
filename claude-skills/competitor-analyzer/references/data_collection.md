# Data Collection Methodology

This reference provides systematic approaches for gathering competitive intelligence using Anysite MCP tools.

## Table of Contents
1. [Web Presence Analysis](#web-presence-analysis)
2. [LinkedIn Intelligence](#linkedin-intelligence)
3. [Social Media Monitoring](#social-media-monitoring)
4. [Community & Sentiment Analysis](#community--sentiment-analysis)
5. [Technical Discovery](#technical-discovery)

---

## Web Presence Analysis

### Primary Website Scraping

**Tool:** `Anysite:parse_webpage`

**Target Pages Priority:**
1. Homepage (`/`) - Core value prop, hero message
2. Pricing (`/pricing`, `/plans`, `/buy`) - Cost structure
3. Product/Features (`/features`, `/product`, `/solutions`) - Capabilities
4. About (`/about`, `/company`, `/team`) - Company background
5. Documentation (`/docs`, `/api`, `/developers`) - Technical depth
6. Blog (`/blog`, `/news`, `/resources`) - Content strategy
7. Careers (`/careers`, `/jobs`, `/team`) - Growth signals
8. Customers (`/customers`, `/case-studies`) - Social proof

**Optimal Parameters:**
```python
Anysite:parse_webpage({
    "url": "https://competitor.com",
    "only_main_content": true,
    "strip_all_tags": true,
    "extract_contacts": true
})
```

**Key Extraction Points:**

*Homepage Analysis:*
- H1/H2 headlines → positioning statement
- Subheadlines → value proposition details
- CTA buttons → conversion focus
- Feature bullets → core capabilities
- Customer logos → social proof
- "Why us" section → differentiators

*Pricing Page Analysis:*
- Plan names and prices
- Features per tier
- Unit costs (per user, per API call, etc.)
- Free tier details
- Enterprise options ("Contact Sales")
- Billing frequency (monthly/annual)
- Money-back guarantees
- Compare features tables

*About Page Analysis:*
- Company mission/vision
- Founding story and date
- Team size indicators
- Location/headquarters
- Company culture signals
- Awards and recognition

### Website Quality Assessment

**Metrics to Note:**
- Design sophistication (modern vs outdated)
- Messaging clarity (clear vs confusing)
- Information architecture (easy to navigate vs complex)
- Mobile responsiveness
- Load speed
- Security (HTTPS, trust badges)

---

## LinkedIn Intelligence

### Company Discovery

**Tools:** 
- `Anysite:search_linkedin_companies` → Find company profile
- `Anysite:get_linkedin_company` → Get detailed info

**Search Strategy:**
```python
# Step 1: Find the company
Anysite:search_linkedin_companies({
    "keywords": "competitor name",
    "count": 5
})

# Step 2: Get detailed profile
Anysite:get_linkedin_company({
    "company": "company-linkedin-slug"
})
```

**Data Points to Extract:**
- Employee count (size indicator)
- Follower count (brand reach)
- Industry tags
- Headquarters location
- Company description
- Website verification
- Founded year (if available)
- Specialties (keywords they emphasize)

### Employee Intelligence

**Tool:** `Anysite:get_linkedin_company_employees`

**Use Cases:**
- Understand team structure (eng:sales ratio)
- Identify key decision-makers
- Track hiring patterns
- Find ex-employees (potential insights source)

**Target Searches:**
```python
# Find leadership
Anysite:get_linkedin_company_employees({
    "companies": ["company-slug"],
    "keywords": "CEO founder",
    "count": 10
})

# Check eng team size
Anysite:get_linkedin_company_employees({
    "companies": ["company-slug"],
    "keywords": "engineer developer",
    "count": 50
})

# Sales team analysis
Anysite:get_linkedin_company_employees({
    "companies": ["company-slug"],
    "keywords": "sales account executive",
    "count": 50
})
```

**Team Composition Signals:**
- High eng count → product-focused
- High sales count → GTM-focused
- Many senior titles → mature org
- Recent hires → growth phase

### Content Strategy Analysis

**Tool:** `Anysite:get_linkedin_company_posts`

```python
Anysite:get_linkedin_company_posts({
    "urn": "company-urn-from-profile",
    "count": 20
})
```

**What to Analyze:**

*Posting Frequency:*
- Daily → very active
- 2-3x per week → active
- Weekly → moderate
- Less → minimal social presence

*Content Themes:*
- Product updates
- Customer wins
- Thought leadership
- Team/culture posts
- Industry news
- Event participation

*Engagement Patterns:*
- Likes per post
- Comments per post
- Share count
- Who's engaging (customers, employees, prospects)

**Engagement Benchmarks:**
- High: >100 likes, >20 comments
- Medium: 20-100 likes, 5-20 comments  
- Low: <20 likes, <5 comments

*Tone Analysis:*
- Professional vs casual
- Technical vs business-focused
- Salesy vs educational
- Founder-led vs corporate

### Employee Posting Activity

**Tool:** `Anysite:get_linkedin_user_posts`

**Why Track:** Employee posts reveal:
- Company culture
- Product launches
- Customer wins
- Hiring signals
- Market positioning

**Target Users:**
- CEO/founders (vision, strategy)
- Head of Product (roadmap hints)
- Marketing leads (positioning)
- Technical leaders (tech stack)

---

## Social Media Deep Research

### Twitter Comprehensive Analysis

**Tool:** `Anysite:get_twitter_user`, `Anysite:get_twitter_user_posts`, `Anysite:search_twitter_posts`

**Multi-Layer Research Approach:**

#### Layer 1: Company Account Analysis

```python
# Profile metrics
Anysite:get_twitter_user({
    "user": "competitor_handle"
})

# Content analysis (100 posts for patterns)
Anysite:get_twitter_user_posts({
    "user": "competitor_handle",
    "count": 100
})
```

**Extract & Analyze:**
- Follower/following ratio (engagement strategy)
- Tweet frequency (activity level)
- Content mix percentages
- Engagement rates (likes/retweets per post)
- Response patterns
- Best performing content types

#### Layer 2: Leadership Twitter Presence

```python
Anysite:get_twitter_user_posts({
    "user": "founder_handle",
    "count": 100
})
```

**Founder archetypes:**
- **The Builder:** Technical, product-focused
- **The Evangelist:** Industry thought leader
- **The Engager:** Community-focused
- **The Silent:** Minimal presence

#### Layer 3: Brand Mentions & Sentiment (200+ mentions)

**Positive signals:**
```python
Anysite:search_twitter_posts({
    "query": "competitor_name (love OR great OR amazing OR solved OR recommend)",
    "count": 100
})
```

**Negative signals:**
```python
Anysite:search_twitter_posts({
    "query": "competitor_name (problem OR bug OR expensive OR switching)",
    "count": 100
})
```

**Competitive mentions:**
```python
Anysite:search_twitter_posts({
    "query": "competitor_name vs OR alternative",
    "count": 100
})
```

**Sentiment score formula:**
```
sentiment_score = (positive - negative) / total
Range: -1.0 to +1.0
```

### Reddit Deep Community Intelligence

**Tool:** `Anysite:search_reddit_posts`, `Anysite:get_reddit_post`, `Anysite:get_reddit_post_comments`

#### Layer 1: Multi-Subreddit Mapping

**Targeted subreddit search:**
```python
relevant_subs = ["SaaS", "startups", "webdev", "programming", "nocode", "automation"]

for sub in relevant_subs:
    Anysite:search_reddit_posts({
        "query": "competitor_name",
        "subreddit": sub,
        "count": 50
    })
```

**What presence reveals:**
- r/SaaS → B2B positioning
- r/webdev → Developer focus  
- r/startups → Early-stage appeal
- Multiple subs → Broad market

#### Layer 2: Competitive Intelligence

**Direct comparisons:**
```python
Anysite:search_reddit_posts({
    "query": "competitor_name vs alternative1",
    "count": 100
})

Anysite:search_reddit_posts({
    "query": "alternative to competitor_name",
    "count": 100
})
```

#### Layer 3: Deep Thread Analysis

**For high-value threads (20+ comments, 50+ upvotes):**

```python
# Get full discussion
Anysite:get_reddit_post({
    "post_url": "reddit.com/r/sub/comments/..."
})

Anysite:get_reddit_post_comments({
    "post_url": "reddit.com/r/sub/comments/..."
})
```

**Analyze comments for:**
- Technical depth discussions
- Real user experiences
- Pain points and workarounds
- Feature comparisons
- Pricing sensitivity
- Decision factors

#### Layer 4: Sentiment Classification

**Positive indicators:**
- "I love [tool]"
- "Best [category]"
- "Highly recommend"
- User-created tutorials

**Negative indicators:**
- "Waste of money"
- "Switched away"
- "Constant issues"
- Looking for alternatives

**Churn signals:**
- "Cancelling subscription"
- "Not worth the price"
- "Moving to [competitor]"

#### Layer 5: Community Health Metrics

```python
# Calculate metrics
total_mentions = count_all_mentions()
unique_subreddits = count_unique_subs()
positive_ratio = positive / total
community_help = user_to_user_help_count()

# Interpretation
awareness_score = total_mentions * unique_subreddits
health_score = positive_ratio * community_help
```

### Cross-Platform Intelligence Synthesis

**Twitter vs Reddit:**

| Aspect | Twitter | Reddit |
|--------|---------|--------|
| Authenticity | Mixed | High (anonymous) |
| Depth | Surface | Deep technical |
| Speed | Real-time | Considered |
| Use | Brand pulse | True insights |

**Pattern detection:**

1. **Marketing vs Reality:** Twitter positive + Reddit negative = Product gaps
2. **Organic Growth:** Both positive + users helping = PMF
3. **Support Issues:** Twitter quick + Reddit complaints = Theater
4. **True Love:** Both advocates + tutorials = Strong community

**Combined sentiment (Reddit weighted 70%):**
```python
combined = twitter * 0.3 + reddit * 0.7
trust_score = combined * consistency
```

---

## Community & Sentiment Analysis
Anysite:search_twitter_posts({
    "query": "competitor_name vs OR alternative",
    "count": 100
})
```

**Sentiment score formula:**
```
sentiment_score = (positive - negative) / total
Range: -1.0 to +1.0
```

### Reddit Deep Community Intelligence

### Twitter/X Analysis

**Tools:**
- `Anysite:get_twitter_user` → Profile stats
- `Anysite:get_twitter_user_posts` → Recent activity
- `Anysite:search_twitter_posts` → Mentions & sentiment

**Profile Analysis:**
```python
Anysite:get_twitter_user({
    "user": "competitor_handle"
})
```

**Extract:**
- Follower count (reach)
- Following count (engagement style)
- Tweet count (activity history)
- Join date (presence longevity)
- Bio (positioning in 160 chars)
- Website verification

**Activity Analysis:**
```python
Anysite:get_twitter_user_posts({
    "user": "competitor_handle",
    "count": 50
})
```

**Analyze:**
- Tweet frequency (daily, weekly, sporadic)
- Content mix (product, thought leadership, customer engagement)
- Engagement per tweet (likes, retweets, replies)
- Response time to mentions
- Tone of voice
- Use of threads (deep content)

**Mention Tracking:**
```python
Anysite:search_twitter_posts({
    "query": "competitor_name OR @handle",
    "count": 100
})
```

**Sentiment Indicators:**
- Positive: "love", "great", "amazing", "helped", "solved"
- Negative: "disappointed", "broken", "slow", "expensive", "switching"
- Questions: "how to", "help", "support", "issue"

### Instagram Presence (if applicable)

**Tools:**
- `Anysite:get_instagram_user`
- `Anysite:get_instagram_user_posts`

**Use For:**
- B2C companies
- Brand-focused businesses
- Visual product demos
- Culture/team content

---

## Community & Sentiment Analysis

### Reddit Intelligence

**Tool:** `Anysite:search_reddit_posts`

**Target Subreddits by Industry:**
- Tech/SaaS: r/SaaS, r/startups, r/Entrepreneur
- Development: r/webdev, r/programming, r/devops
- No-code: r/nocode, r/automation
- Data: r/datascience, r/analytics
- Marketing: r/marketing, r/digital_marketing

**Search Strategies:**

*Direct Mentions:*
```python
Anysite:search_reddit_posts({
    "query": "competitor_name",
    "count": 50
})
```

*Competitive Comparisons:*
```python
Anysite:search_reddit_posts({
    "query": "competitor_name vs alternative",
    "count": 50
})
```

*Problem Space:*
```python
Anysite:search_reddit_posts({
    "query": "problem_they_solve",
    "subreddit": "relevant_subreddit",
    "count": 50
})
```

**What to Extract:**
- Mention volume (brand awareness)
- Sentiment distribution
- Common complaints
- Praise points
- Alternative products mentioned
- Price sensitivity discussions
- Feature requests
- Use case descriptions

**Sentiment Analysis:**
- Count positive vs negative mentions
- Identify recurring complaints
- Note abandoned customers
- Track feature satisfaction

---

## Technical Discovery

### API & Documentation Analysis

**Tool:** `Anysite:parse_webpage` on docs

**Target URLs:**
- `/docs`
- `/api-reference`
- `/developers`
- `/api/v1/docs`
- `/documentation`

**Assessment Criteria:**

*Documentation Quality:*
- Completeness (all endpoints documented)
- Code examples (Python, JS, cURL)
- Interactive API explorer
- Changelog/versioning
- Rate limits clearly stated
- Authentication explained
- Error handling documented

*API Maturity Indicators:*
- RESTful design
- GraphQL option
- Webhook support
- SDKs available (Python, JS, Ruby, etc.)
- OpenAPI/Swagger spec
- Sandbox environment
- Status page

### Integration Ecosystem

**Discovery Methods:**

*Direct Check:*
```python
Anysite:parse_webpage({
    "url": "https://competitor.com/integrations",
    "only_main_content": true
})
```

*Sitemap Discovery:*
```python
Anysite:get_sitemap({
    "url": "https://competitor.com/sitemap.xml",
    "count": 100
})
```

**Integration Categories:**

*No-Code/Automation:*
- Zapier → SMB/no-code focus
- Make.com → European market
- n8n → Open-source community
- Integromat → Power users

*CRM/Sales:*
- Salesforce → Enterprise
- HubSpot → SMB
- Pipedrive → Small business

*Collaboration:*
- Slack → Team-first
- Microsoft Teams → Enterprise
- Discord → Community-focused

*Data/Analytics:*
- Google Sheets → Accessible
- Airtable → Modern teams
- Snowflake → Data-heavy enterprise

**Market Signal:**
Number and type of integrations indicate target market and maturity.

---

## Timing & Frequency

### Initial Deep Dive
- Complete all sections: 3-4 hours
- Focus on highest-priority competitor

### Quarterly Updates
- Re-scrape pricing page
- Check LinkedIn for growth
- Review recent posts
- Update funding data

### Monthly Monitoring
- Social media activity
- Blog content
- Product changelog
- Job postings

### Weekly Alerts (if critical)
- Pricing changes
- Major announcements
- Funding news
- Customer wins

---

## Alternative Data Sources

### The Data Explosion Problem

**Modern competitive intelligence requires:**
- Patents (innovation signals)
- ESG filings (sustainability, governance)
- Glassdoor reviews (internal culture)
- GitHub commits (development velocity)
- Real-time signals vs quarterly reports

**The 80/20 Problem:**
> "Analysts spend 80% of their time collecting data, and only 20% analyzing it."

This skill automates the collection phase.

### Employee Reviews (Glassdoor)

**Tool:** `Anysite:parse_webpage`

**URL patterns:**
```
https://www.glassdoor.com/Reviews/[company-name]-Reviews-E[id].htm
https://www.glassdoor.com/Overview/Working-at-[company-name]
```

**Key Metrics to Extract:**

*Overall Ratings:*
- Company rating (1-5 stars)
- CEO approval rating (%)
- Recommend to friend (%)
- Business outlook (positive/neutral/negative)

*Category Scores (1-5):*
- Culture & Values
- Work/Life Balance
- Senior Management
- Compensation & Benefits
- Career Opportunities

*Qualitative Signals:*
- Pros (common themes in positive reviews)
- Cons (common complaints)
- Recent review sentiment (last 3 months)
- Review volume trend (growing/stable/declining)

**Analysis Framework:**

```
High satisfaction (>4.0) + High CEO approval (>85%):
→ Strong culture, effective leadership

Low satisfaction (<3.5) + Negative trend:
→ Internal problems, potential talent exodus

High compensation + Low culture:
→ Mercenary employees, retention risk

Recent negative reviews spike:
→ Recent changes, reorg, layoffs?
```

### GitHub Activity

**Tool:** `Anysite:parse_webpage` on GitHub

**For Open Source or Public Repos:**

```
https://github.com/[org-name]
https://github.com/[org-name]/[main-repo]
```

**Metrics to Track:**

*Repository Level:*
- Star count (developer interest)
- Fork count (actual usage/contribution)
- Watchers (active followers)
- Contributors (community size)
- Commit frequency (last month/quarter)
- Issue count (open vs closed)
- Pull request activity
- Release cadence

*Organization Level:*
- Total public repos
- Total stars across all repos
- Team size (public members)
- Contribution guidelines (community maturity)
- Sponsorship program (monetization)

**Velocity Indicators:**

```
Daily commits → Very active development
Weekly commits → Active
Monthly commits → Moderate
Sporadic → Side project or legacy

Issue response time:
<24h → Excellent support
<72h → Good
<1 week → Acceptable
>1 week → Poor
```

**Community Health:**

- **Strong:** Active contributors, PRs from outside org, issues get closed
- **Medium:** Some external contributions, responsive maintainers
- **Weak:** Only internal commits, stale issues, no external engagement

### Patent Analysis

**Tool:** `Anysite:parse_webpage`

**Sources:**
```
Google Patents: patents.google.com
USPTO: patft.uspto.gov
Company website: /patents or /innovation pages
```

**What to Look For:**

*Patent Portfolio Size:*
- Total patents granted
- Pending applications
- Recent filings (last 12 months)

*Technology Areas:*
- Core technology patents
- Defensive patents
- Strategic patent clusters

*Patent Quality Indicators:*
- Citations by other patents (impact)
- Forward citations (influence)
- Inventor names (key technical talent)

**Strategic Signals:**

```
Recent patent spike → R&D investment surge
Broad portfolio → Platform company
Niche patents → Specialized focus
Defensive patents → Protecting moat
Licensing patents → Monetization strategy
```

### ESG & Sustainability Data

**Tool:** `Anysite:parse_webpage`

**Sources:**
```
Company sustainability reports
ESG rating providers (if public)
CDP (Carbon Disclosure Project)
Company /sustainability or /esg pages
```

**Extract:**
- Sustainability commitments
- Carbon neutrality goals
- Diversity metrics
- Board composition
- Governance structure
- ESG scores (if available)

**Why It Matters:**
- Enterprise buyers increasingly require ESG compliance
- Strong ESG → Attractive to talent and investors
- Public ESG commitments → Accountability signals

### Job Postings Intelligence

**Tool:** `Anysite:search_linkedin_jobs`

```python
Anysite:search_linkedin_jobs({
    "keywords": "company-name",
    "count": 50
})
```

**Growth Signals:**

*Hiring Volume:*
- 0-10 openings → Small/stable
- 10-50 openings → Growing
- 50-100 openings → Rapid expansion
- 100+ openings → Hyper-growth

*Role Analysis:*
- Many eng roles → Building product
- Many sales roles → Scaling GTM
- Leadership roles → Expanding management
- Specialized roles → New initiatives

*Location Patterns:*
- Remote → Talent anywhere
- Hub cities → Office-centric
- New locations → Geographic expansion

**Timing Signals:**
- Recent posting spike → Growth phase
- Long-open positions → Hiring challenges
- Frequent re-postings → High turnover or bad fit

### News & Media Mentions

**Tool:** `Anysite:search_reddit_posts`, `Anysite:search_twitter_posts`

**What to Track:**

*Funding News:*
- Recent raises
- Investor announcements
- Valuation reports

*Product Launches:*
- New features
- Major updates
- Platform announcements

*Partnerships:*
- Strategic partnerships
- Integration announcements
- Channel partnerships

*Customer Wins:*
- Enterprise logos
- Case study announcements
- Customer testimonials

*Negative News:*
- Layoffs
- Executive departures
- Product issues
- Customer complaints going viral

### Real-Time Signals vs Quarterly Reports

**Traditional (Quarterly):**
- Financial reports
- Earnings calls
- Investor updates

**Real-Time (This Skill):**
- Daily GitHub commits
- Weekly job postings
- Real-time social sentiment
- Glassdoor reviews (weekly)
- LinkedIn activity (daily)
- Blog/changelog updates
- Reddit/Twitter mentions

**Speed Advantage:**
Markets move faster than quarterly cycles. Real-time signals provide:
- Early growth indicators
- Problem detection before official news
- Strategic shift signals
- Competitive move warnings

---

## Data Quality Guidelines

**Always Note:**
- Data freshness (when collected)
- Confidence level (verified vs estimated)
- Source (direct from site, third-party, inferred)
- Missing data (what couldn't be found)

**Verification:**
- Cross-reference across multiple sources
- Check official announcements
- Verify numbers (don't trust marketing claims blindly)
- Note assumptions clearly
