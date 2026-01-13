#!/usr/bin/env python3
"""
Universal Competitor Analysis Script
Creates structured template for analyzing any competitor
"""

import json
import sys
from datetime import datetime
from typing import Dict, List, Any

def create_analysis_template(competitor_name: str, website: str) -> Dict[str, Any]:
    """
    Creates a structured template for competitor analysis
    
    Args:
        competitor_name: Name of the competitor
        website: Primary website URL
        
    Returns:
        Dict with analysis structure
    """
    return {
        "metadata": {
            "competitor_name": competitor_name,
            "website": website,
            "analysis_date": datetime.now().isoformat(),
            "status": "draft"
        },
        "company_overview": {
            "description": "",
            "headquarters": "",
            "founded": "",
            "employee_count": "",
            "funding": {
                "total_raised": "",
                "last_round": "",
                "last_round_date": "",
                "investors": []
            }
        },
        "market_position": {
            "positioning_statement": "",
            "value_proposition": "",
            "target_segments": [],
            "ideal_customer_profile": "",
            "key_differentiators": [],
            "messaging_themes": []
        },
        "product": {
            "core_features": [],
            "unique_capabilities": [],
            "limitations": [],
            "technical_capabilities": {
                "api_available": False,
                "api_quality": "",
                "integrations": [],
                "technology_stack": [],
                "deployment_options": []
            },
            "pricing": {
                "model": "",
                "tiers": [],
                "entry_price": "",
                "unit_economics": "",
                "free_tier": False,
                "free_tier_limits": "",
                "notes": ""
            }
        },
        "go_to_market": {
            "sales_motion": "",
            "primary_channels": [],
            "content_strategy": {
                "blog_frequency": "",
                "key_topics": [],
                "content_quality": "",
                "tone_of_voice": ""
            },
            "partnerships": [],
            "community_presence": []
        },
        "online_presence": {
            "website": {
                "design_quality": "",
                "messaging_clarity": "",
                "conversion_focus": ""
            },
            "social_media": {
                "linkedin": {
                    "url": "",
                    "followers": 0,
                    "post_frequency": "",
                    "engagement_quality": "",
                    "content_themes": []
                },
                "twitter": {
                    "company_account": {
                        "handle": "",
                        "followers": 0,
                        "tweet_frequency": "",
                        "response_time": "",
                        "engagement_rate": "",
                        "content_mix": []
                    },
                    "founder_accounts": [],
                    "mention_volume": 0,
                    "sentiment_score": 0.0,
                    "positive_mentions": 0,
                    "negative_mentions": 0,
                    "key_complaints": [],
                    "key_praise_points": []
                }
            },
            "community": {
                "reddit": {
                    "total_mentions": 0,
                    "subreddits_present": [],
                    "sentiment_distribution": {
                        "positive": 0,
                        "neutral": 0,
                        "negative": 0
                    },
                    "top_discussions": [],
                    "common_use_cases": [],
                    "pain_points": [],
                    "competitive_comparisons": []
                },
                "overall_sentiment": "",
                "community_size": "",
                "engagement_quality": ""
            }
        },
        "traction_signals": {
            "customer_evidence": {
                "testimonials_count": 0,
                "case_studies_count": 0,
                "customer_logos": [],
                "review_ratings": {}
            },
            "growth_indicators": {
                "employee_growth": "",
                "job_openings": 0,
                "product_updates_frequency": "",
                "market_momentum": ""
            }
        },
        "strengths_weaknesses": {
            "strengths": [],
            "weaknesses": [],
            "opportunities": [],
            "threats": []
        },
        "competitive_intelligence": {
            "what_they_do_well": [],
            "where_they_struggle": [],
            "pricing_vs_market": "",
            "feature_gaps": [],
            "strategic_vulnerabilities": []
        },
        "strategic_insights": {
            "key_takeaways": [],
            "competitive_threats": [],
            "opportunities_to_exploit": [],
            "watch_areas": []
        },
        "leadership": {
            "founders": [],
            "c_level": [],
            "key_hires": [],
            "founder_profiles": {
                "background": [],
                "previous_companies": [],
                "expertise_areas": [],
                "public_presence": {
                    "linkedin_activity": "",
                    "twitter_followers": 0,
                    "thought_leadership": ""
                }
            }
        },
        "alternative_data": {
            "glassdoor": {
                "overall_rating": 0,
                "ceo_approval": 0,
                "culture_score": 0,
                "recent_sentiment": ""
            },
            "github": {
                "repos_count": 0,
                "total_stars": 0,
                "commit_frequency": "",
                "community_size": ""
            },
            "patents": [],
            "recent_news": []
        }
    }

def format_markdown_report(data: Dict[str, Any]) -> str:
    """
    Converts analysis data into formatted markdown report
    """
    md = f"""# Competitive Intelligence Report: {data['metadata']['competitor_name']}

**Analysis Date:** {data['metadata']['analysis_date'][:10]}  
**Website:** {data['metadata']['website']}  
**Status:** {data['metadata']['status']}

---

## Executive Summary

### Positioning
{data['market_position'].get('positioning_statement', '_To be completed_')}

### Value Proposition
{data['market_position'].get('value_proposition', '_To be completed_')}

### Key Differentiators
"""
    
    if data['market_position'].get('key_differentiators'):
        for diff in data['market_position']['key_differentiators']:
            md += f"- {diff}\n"
    else:
        md += "_To be completed_\n"
    
    md += f"""

---

## Company Overview

**Description:** {data['company_overview'].get('description', '_To be completed_')}

**Key Facts:**
- Headquarters: {data['company_overview'].get('headquarters', '_Unknown_')}
- Founded: {data['company_overview'].get('founded', '_Unknown_')}
- Employees: {data['company_overview'].get('employee_count', '_Unknown_')}

### Funding
- Total Raised: {data['company_overview']['funding'].get('total_raised', '_Unknown_')}
- Last Round: {data['company_overview']['funding'].get('last_round', '_Unknown_')}
- Date: {data['company_overview']['funding'].get('last_round_date', '_Unknown_')}
"""
    
    if data['company_overview']['funding'].get('investors'):
        md += f"- Investors: {', '.join(data['company_overview']['funding']['investors'])}\n"
    
    md += """

---

## Product Analysis

### Core Features
"""
    
    if data['product'].get('core_features'):
        for feature in data['product']['core_features']:
            md += f"- {feature}\n"
    else:
        md += "_To be completed_\n"
    
    md += "\n### Unique Capabilities\n"
    
    if data['product'].get('unique_capabilities'):
        for cap in data['product']['unique_capabilities']:
            md += f"- {cap}\n"
    else:
        md += "_To be completed_\n"
    
    md += f"""

### Technical Stack
- API Available: {data['product']['technical_capabilities'].get('api_available', 'Unknown')}
- API Quality: {data['product']['technical_capabilities'].get('api_quality', '_To be assessed_')}
"""
    
    if data['product']['technical_capabilities'].get('integrations'):
        md += f"- Integrations: {', '.join(data['product']['technical_capabilities']['integrations'])}\n"
    
    md += f"""

### Pricing Structure
- **Model:** {data['product']['pricing'].get('model', '_To be determined_')}
- **Entry Price:** {data['product']['pricing'].get('entry_price', '_To be determined_')}
- **Free Tier:** {data['product']['pricing'].get('free_tier', False)}
"""
    
    if data['product']['pricing'].get('free_tier_limits'):
        md += f"- **Free Tier Limits:** {data['product']['pricing']['free_tier_limits']}\n"
    
    if data['product']['pricing'].get('unit_economics'):
        md += f"- **Unit Economics:** {data['product']['pricing']['unit_economics']}\n"
    
    if data['product']['pricing'].get('tiers'):
        md += "\n**Pricing Tiers:**\n"
        for tier in data['product']['pricing']['tiers']:
            md += f"- {tier}\n"
    
    md += """

---

## Go-to-Market Analysis

### Sales Motion
"""
    md += data['go_to_market'].get('sales_motion', '_To be determined_') + "\n\n"
    
    md += "### Primary Channels\n"
    if data['go_to_market'].get('primary_channels'):
        for channel in data['go_to_market']['primary_channels']:
            md += f"- {channel}\n"
    else:
        md += "_To be determined_\n"
    
    md += f"""

### Content Strategy
- Blog Frequency: {data['go_to_market']['content_strategy'].get('blog_frequency', '_Unknown_')}
- Content Quality: {data['go_to_market']['content_strategy'].get('content_quality', '_To be assessed_')}
- Tone of Voice: {data['go_to_market']['content_strategy'].get('tone_of_voice', '_To be assessed_')}
"""
    
    if data['go_to_market']['content_strategy'].get('key_topics'):
        md += f"\n**Key Topics:** {', '.join(data['go_to_market']['content_strategy']['key_topics'])}\n"
    
    md += """

---

## Online Presence

### Social Media Performance

**LinkedIn:**
- Followers: {linkedin['followers']:,}
- Post Frequency: {linkedin.get('post_frequency', '_Unknown_')}
- Engagement: {linkedin.get('engagement_quality', '_To be assessed_')}
"""
    
    if linkedin.get('content_themes'):
        md += f"- Content Themes: {', '.join(linkedin['content_themes'])}\n"
    
    twitter = data['online_presence']['social_media'].get('twitter', {})
    company_account = twitter.get('company_account', {})
    
    if company_account.get('followers'):
        md += f"""

**Twitter - Company Account:**
- Handle: @{company_account.get('handle', '_Unknown_')}
- Followers: {company_account['followers']:,}
- Tweet Frequency: {company_account.get('tweet_frequency', '_Unknown_')}
- Response Time: {company_account.get('response_time', '_Unknown_')}
- Engagement Rate: {company_account.get('engagement_rate', '_Unknown_')}
"""
    
    if twitter.get('mention_volume'):
        md += f"""

**Twitter - Brand Mentions:**
- Total Mentions: {twitter['mention_volume']:,}
- Sentiment Score: {twitter.get('sentiment_score', 0):.2f} (-1 to +1)
- Positive Mentions: {twitter.get('positive_mentions', 0)}
- Negative Mentions: {twitter.get('negative_mentions', 0)}
"""
    
    if twitter.get('key_praise_points'):
        md += "\n**What Users Praise:**\n"
        for praise in twitter['key_praise_points'][:5]:
            md += f"- {praise}\n"
    
    if twitter.get('key_complaints'):
        md += "\n**Common Complaints:**\n"
        for complaint in twitter['key_complaints'][:5]:
            md += f"- {complaint}\n"
    
    if twitter.get('founder_accounts'):
        md += f"\n**Founder Twitter Presence:** {', '.join(twitter['founder_accounts'])}\n"
    
    reddit = data['online_presence']['community'].get('reddit', {})
    
    md += f"""

### Reddit Community Analysis

**Presence:**
- Total Mentions: {reddit.get('total_mentions', 0)}
- Subreddits: {', '.join(reddit.get('subreddits_present', [])[:5]) if reddit.get('subreddits_present') else '_None found_'}

**Sentiment Distribution:**
"""
    
    sentiment_dist = reddit.get('sentiment_distribution', {})
    if sentiment_dist.get('positive') or sentiment_dist.get('negative'):
        md += f"- Positive: {sentiment_dist.get('positive', 0)} mentions\n"
        md += f"- Neutral: {sentiment_dist.get('neutral', 0)} mentions\n"
        md += f"- Negative: {sentiment_dist.get('negative', 0)} mentions\n"
    else:
        md += "_To be analyzed_\n"
    
    if reddit.get('common_use_cases'):
        md += "\n**Common Use Cases (from Reddit):**\n"
        for use_case in reddit['common_use_cases'][:5]:
            md += f"- {use_case}\n"
    
    if reddit.get('pain_points'):
        md += "\n**Pain Points (from Reddit):**\n"
        for pain in reddit['pain_points'][:5]:
            md += f"- {pain}\n"
    
    if reddit.get('competitive_comparisons'):
        md += "\n**Competitive Comparisons:**\n"
        for comp in reddit['competitive_comparisons'][:5]:
            md += f"- {comp}\n"
    
    md += f"""

**Overall Community:**
- Sentiment: {data['online_presence']['community'].get('overall_sentiment', '_To be assessed_')}
- Engagement Quality: {data['online_presence']['community'].get('engagement_quality', '_To be assessed_')}
- Community Size: {data['online_presence']['community'].get('community_size', '_Unknown_')}

---

## Traction Signals

### Customer Evidence
- Testimonials: {data['traction_signals']['customer_evidence'].get('testimonials_count', 0)}
- Case Studies: {data['traction_signals']['customer_evidence'].get('case_studies_count', 0)}
"""
    
    if data['traction_signals']['customer_evidence'].get('customer_logos'):
        md += f"- Notable Customers: {', '.join(data['traction_signals']['customer_evidence']['customer_logos'][:5])}\n"
    
    md += f"""

### Growth Indicators
- Employee Growth: {data['traction_signals']['growth_indicators'].get('employee_growth', '_Unknown_')}
- Job Openings: {data['traction_signals']['growth_indicators'].get('job_openings', 0)}
- Product Update Frequency: {data['traction_signals']['growth_indicators'].get('product_updates_frequency', '_Unknown_')}
- Market Momentum: {data['traction_signals']['growth_indicators'].get('market_momentum', '_To be assessed_')}

---

## SWOT Analysis

### Strengths
"""
    
    if data['strengths_weaknesses'].get('strengths'):
        for strength in data['strengths_weaknesses']['strengths']:
            md += f"- {strength}\n"
    else:
        md += "_To be completed_\n"
    
    md += "\n### Weaknesses\n"
    
    if data['strengths_weaknesses'].get('weaknesses'):
        for weakness in data['strengths_weaknesses']['weaknesses']:
            md += f"- {weakness}\n"
    else:
        md += "_To be completed_\n"
    
    md += "\n### Opportunities\n"
    
    if data['strengths_weaknesses'].get('opportunities'):
        for opp in data['strengths_weaknesses']['opportunities']:
            md += f"- {opp}\n"
    else:
        md += "_To be completed_\n"
    
    md += "\n### Threats\n"
    
    if data['strengths_weaknesses'].get('threats'):
        for threat in data['strengths_weaknesses']['threats']:
            md += f"- {threat}\n"
    else:
        md += "_To be completed_\n"
    
    md += """

---

## Competitive Intelligence

### What They Do Well
"""
    
    if data['competitive_intelligence'].get('what_they_do_well'):
        for item in data['competitive_intelligence']['what_they_do_well']:
            md += f"- {item}\n"
    else:
        md += "_To be completed_\n"
    
    md += "\n### Where They Struggle\n"
    
    if data['competitive_intelligence'].get('where_they_struggle'):
        for item in data['competitive_intelligence']['where_they_struggle']:
            md += f"- {item}\n"
    else:
        md += "_To be completed_\n"
    
    md += f"""

### Pricing Position
{data['competitive_intelligence'].get('pricing_vs_market', '_To be determined_')}

---

## Strategic Insights

### Key Takeaways
"""
    
    if data['strategic_insights'].get('key_takeaways'):
        for takeaway in data['strategic_insights']['key_takeaways']:
            md += f"- {takeaway}\n"
    else:
        md += "_Analysis pending_\n"
    
    md += "\n### Competitive Threats\n"
    
    if data['strategic_insights'].get('competitive_threats'):
        for threat in data['strategic_insights']['competitive_threats']:
            md += f"- {threat}\n"
    else:
        md += "_Analysis pending_\n"
    
    md += "\n### Opportunities to Exploit\n"
    
    if data['strategic_insights'].get('opportunities_to_exploit'):
        for opp in data['strategic_insights']['opportunities_to_exploit']:
            md += f"- {opp}\n"
    else:
        md += "_Analysis pending_\n"
    
    md += "\n### Areas to Watch\n"
    
    if data['strategic_insights'].get('watch_areas'):
        for area in data['strategic_insights']['watch_areas']:
            md += f"- {area}\n"
    else:
        md += "_Analysis pending_\n"
    
    md += """

---

## Leadership Intelligence

### Founders & C-Level
"""
    
    if data['leadership'].get('founders'):
        md += "\n**Founders:**\n"
        for founder in data['leadership']['founders']:
            md += f"- {founder}\n"
    
    if data['leadership'].get('c_level'):
        md += "\n**C-Level Team:**\n"
        for exec in data['leadership']['c_level']:
            md += f"- {exec}\n"
    
    founder_profiles = data['leadership'].get('founder_profiles', {})
    
    if founder_profiles.get('background'):
        md += "\n### Founder Background\n"
        for bg in founder_profiles['background']:
            md += f"- {bg}\n"
    
    if founder_profiles.get('previous_companies'):
        md += "\n**Previous Companies:**\n"
        for company in founder_profiles['previous_companies']:
            md += f"- {company}\n"
    
    if founder_profiles.get('expertise_areas'):
        md += f"\n**Expertise:** {', '.join(founder_profiles['expertise_areas'])}\n"
    
    public_presence = founder_profiles.get('public_presence', {})
    if public_presence.get('linkedin_activity') or public_presence.get('twitter_followers'):
        md += "\n### Public Presence\n"
        if public_presence.get('linkedin_activity'):
            md += f"- LinkedIn Activity: {public_presence['linkedin_activity']}\n"
        if public_presence.get('twitter_followers'):
            md += f"- Twitter Followers: {public_presence['twitter_followers']:,}\n"
        if public_presence.get('thought_leadership'):
            md += f"- Thought Leadership: {public_presence['thought_leadership']}\n"
    
    md += """

---

## Alternative Data Sources

### Employee Sentiment (Glassdoor)
"""
    
    glassdoor = data['alternative_data'].get('glassdoor', {})
    if glassdoor.get('overall_rating'):
        md += f"- Overall Rating: {glassdoor['overall_rating']}/5\n"
        md += f"- CEO Approval: {glassdoor['ceo_approval']}%\n"
        md += f"- Culture Score: {glassdoor['culture_score']}/5\n"
        md += f"- Recent Sentiment: {glassdoor.get('recent_sentiment', '_Unknown_')}\n"
    else:
        md += "_Data not available_\n"
    
    md += "\n### GitHub Presence\n"
    
    github = data['alternative_data'].get('github', {})
    if github.get('repos_count'):
        md += f"- Public Repositories: {github['repos_count']}\n"
        md += f"- Total Stars: {github['total_stars']:,}\n"
        md += f"- Commit Frequency: {github.get('commit_frequency', '_Unknown_')}\n"
        md += f"- Community Size: {github.get('community_size', '_Unknown_')}\n"
    else:
        md += "_No significant GitHub presence_\n"
    
    if data['alternative_data'].get('patents'):
        md += "\n### Patents\n"
        for patent in data['alternative_data']['patents']:
            md += f"- {patent}\n"
    
    return md

def save_analysis(data: Dict[str, Any], output_path: str = None):
    """
    Saves analysis to both JSON and Markdown formats
    """
    competitor_slug = data['metadata']['competitor_name'].lower().replace(' ', '-').replace('.', '')
    timestamp = datetime.now().strftime('%Y%m%d')
    
    if not output_path:
        output_path = f"/mnt/user-data/outputs/competitor_analysis_{competitor_slug}_{timestamp}"
    
    # Save JSON
    json_path = f"{output_path}.json"
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Save Markdown
    md_path = f"{output_path}.md"
    md_content = format_markdown_report(data)
    with open(md_path, 'w') as f:
        f.write(md_content)
    
    return json_path, md_path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python analyze_competitor.py <competitor_name> <website>")
        print("Example: python analyze_competitor.py 'Acme Corp' 'https://acme.com'")
        sys.exit(1)
    
    competitor = sys.argv[1]
    website = sys.argv[2]
    
    template = create_analysis_template(competitor, website)
    print(json.dumps(template, indent=2))
