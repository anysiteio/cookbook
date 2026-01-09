# Investor Scoring Reference

Universal scoring criteria - adapt weights based on company's `investor_criteria.json`.

## Scoring Weights

| Factor | Weight | Max Points |
|--------|--------|------------|
| Stage Fit | 25% | 25 |
| Thesis Match | 25% | 25 |
| Portfolio Relevance | 30% | 30 |
| Activity Level | 10% | 10 |
| Network Value | 10% | 10 |

**Gate Check:** Must be actual investor (Partner, GP, Angel, EIR, Venture). Corporate roles = Score 0.

## Stage Fit (25 points)

Match investor's stage focus with company's raising stage.

| Company Stage | Ideal Investor Focus | Points |
|---------------|---------------------|--------|
| Pre-Seed | Pre-seed/Seed primary | 25 |
| Pre-Seed | Early-stage generalist | 20 |
| Pre-Seed | Multi-stage with early deals | 15 |
| Seed | Seed primary focus | 25 |
| Seed | Pre-seed to Series A | 20 |
| Series A | Series A focus | 25 |
| Series A | Seed to Series B | 20 |

**Check size alignment:**
- Angels: $25K-$250K
- Micro VCs: $100K-$500K
- Seed VCs: $500K-$2M
- Series A: $2M-$10M

**Mismatch penalties:**
- Fund too large (Series B+ for pre-seed): -15 points
- Fund too small (angel for Series A): -10 points

## Thesis Match (25 points)

Compare investor thesis keywords with company's `thesis_keywords`.

| Match Level | Points |
|-------------|--------|
| 3+ keywords match | 25 |
| 2 keywords match | 20 |
| 1 strong keyword match | 15 |
| Adjacent/related thesis | 10 |
| Partial overlap | 5 |
| No overlap | 0 |

**Common thesis categories:**
- B2B SaaS
- AI/ML
- Developer Tools
- Data Infrastructure
- Fintech
- Healthcare
- Consumer
- Crypto/Web3
- Climate/Cleantech
- E-commerce
- Marketplace

**Thesis conflicts (Score = 0):**
- Crypto-only investor for SaaS company
- Healthcare-only for DevTools company
- Consumer-only for B2B company

## Portfolio Relevance (30 points)

Check if investor has funded similar companies.

| Portfolio Signal | Points |
|------------------|--------|
| Direct similar company (same category) | 30 |
| Adjacent category (related market) | 20 |
| Same business model (PLG, enterprise, etc.) | 15 |
| Same customer type (SMB, enterprise, etc.) | 10 |
| General tech portfolio | 5 |

**How to find portfolio:**
1. LinkedIn profile "Investments" section
2. Fund website portfolio page
3. `WebSearch("[Fund name] portfolio companies")`
4. Crunchbase investor profile

## Activity Level (10 points)

Recent investment activity signals active deployment.

| Activity | Points |
|----------|--------|
| 3+ investments in last 12 months | 10 |
| 1-2 investments in last 12 months | 7 |
| Active 12-18 months ago | 5 |
| Last investment 18+ months ago | 2 |
| No recent activity visible | 0 |

**Signs of active investor:**
- Recent LinkedIn posts about investments
- Announced deals in last 6 months
- Speaking at startup events
- Active on Twitter/X about startups

## Network Value (10 points)

Investor's ability to help beyond capital.

| Network Signal | Points |
|----------------|--------|
| Top accelerator partner (YC, Techstars) | 10 |
| 100+ investments track record | 8 |
| Active angel network member | 6 |
| Industry expert/operator | 5 |
| Some network visibility | 3 |
| Individual angel, limited network | 1 |

## Score Adjustments

| Condition | Adjustment |
|-----------|------------|
| Portfolio conflict (competitor investment) | -20 |
| Stage mismatch (fund too large/small) | -10 to -15 |
| Geographic restriction (excludes team) | -10 |
| Thesis conflict | -15 |
| Wrong person at LinkedIn URL | = 0 |
| Not actually an investor (corporate role) | = 0 |

## Competitor Detection

Before analysis, define company's competitors in `investor_criteria.json`.

**Conflict check process:**
1. Get fund/investor portfolio
2. Search each competitor name
3. If found: -20 points + add to `risk_factors`

**Conflict doesn't always disqualify:**
- Still valuable for feedback/advice
- May provide intros to other investors
- Lower probability of investment, not zero

## Score Interpretation

| Score | Category | Action |
|-------|----------|--------|
| 85-100 | Strong Fit | Priority outreach, personalized message |
| 70-84 | Good Fit | Standard outreach with personalization |
| 50-69 | Moderate | Consider for warm intros only |
| 30-49 | Weak Fit | Skip unless strategic reason |
| 0-29 | Not Fit | Do not reach out |

## Scoring Examples

### High Score (90)
- Role: Partner @ Seed Fund (Gate: PASS)
- Stage: Seed focus, company raising seed (25/25)
- Thesis: All keywords match (25/25)
- Portfolio: 2 similar companies (25/30)
- Activity: 5 deals this year (10/10)
- Network: YC scout (8/10)
- **Total: 93 → capped at 90**

### Medium Score (72)
- Role: Angel Investor (Gate: PASS)
- Stage: Does pre-seed and seed (20/25)
- Thesis: 1 keyword match (15/25)
- Portfolio: Adjacent companies (20/30)
- Activity: Active last year (7/10)
- Network: Some visibility (4/10)
- **Total: 66 + small adjustments = 72**

### Disqualified (0)
- CSV says: "Angel Investor at Tech Company"
- LinkedIn actual role: VP Engineering at BigCorp
- No investment activity visible
- **Score: 0** - failed gate check

### Conflict Flagged (68)
- Original score: 88
- Found: Invested in direct competitor
- Adjustment: -20 for conflict
- **Final: 68** + risk flag
- Action: Reach out for feedback, lower expectation
