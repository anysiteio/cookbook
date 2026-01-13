#!/usr/bin/env python3
"""
AnySite ICP Analyzer
Analyzes LinkedIn data to extract ICP patterns and score prospects.

Usage:
    python icp_analyzer.py analyze --input customers.json --output icp_report.json
    python icp_analyzer.py score --icp icp_config.json --prospect prospect.json
"""

import json
import argparse
from collections import Counter, defaultdict
from datetime import datetime
from typing import List, Dict, Any, Optional
import re


class ICPAnalyzer:
    """Analyze customer data to build Ideal Customer Profile."""
    
    # Industry keyword mappings
    INDUSTRY_KEYWORDS = {
        'saas': ['software', 'saas', 'cloud', 'platform', 'api'],
        'fintech': ['finance', 'fintech', 'banking', 'payments', 'financial'],
        'healthtech': ['health', 'healthcare', 'medical', 'biotech', 'pharma'],
        'ecommerce': ['ecommerce', 'e-commerce', 'retail', 'marketplace'],
        'ai_ml': ['artificial intelligence', 'machine learning', 'ai', 'ml', 'data science'],
        'cybersecurity': ['security', 'cybersecurity', 'infosec', 'cyber'],
        'martech': ['marketing', 'martech', 'advertising', 'adtech'],
        'hr_tech': ['hr', 'human resources', 'recruiting', 'talent'],
    }
    
    # Seniority level mappings
    SENIORITY_LEVELS = {
        'c_level': ['ceo', 'cto', 'cfo', 'coo', 'cmo', 'cpo', 'chief'],
        'vp': ['vp', 'vice president', 'svp', 'evp'],
        'director': ['director', 'head of', 'lead'],
        'manager': ['manager', 'team lead', 'supervisor'],
        'individual': ['engineer', 'analyst', 'specialist', 'consultant']
    }
    
    # Company size buckets
    SIZE_BUCKETS = {
        'startup': (1, 50),
        'small': (51, 200),
        'medium': (201, 1000),
        'large': (1001, 5000),
        'enterprise': (5001, float('inf'))
    }
    
    def __init__(self):
        self.customers = []
        self.patterns = {}
    
    def load_customers(self, data: List[Dict]) -> None:
        """Load customer data from list of dictionaries."""
        self.customers = data
    
    def extract_seniority(self, title: str) -> str:
        """Extract seniority level from job title."""
        title_lower = title.lower()
        for level, keywords in self.SENIORITY_LEVELS.items():
            if any(kw in title_lower for kw in keywords):
                return level
        return 'individual'
    
    def extract_function(self, title: str) -> str:
        """Extract job function from title."""
        title_lower = title.lower()
        functions = {
            'engineering': ['engineer', 'developer', 'architect', 'technical'],
            'sales': ['sales', 'account', 'business development', 'bd'],
            'marketing': ['marketing', 'growth', 'brand', 'content'],
            'product': ['product', 'pm', 'ux', 'design'],
            'operations': ['operations', 'ops', 'admin', 'support'],
            'finance': ['finance', 'accounting', 'controller'],
            'hr': ['hr', 'people', 'talent', 'recruiting'],
            'executive': ['ceo', 'founder', 'president', 'general manager']
        }
        for func, keywords in functions.items():
            if any(kw in title_lower for kw in keywords):
                return func
        return 'other'
    
    def categorize_company_size(self, employee_count: int) -> str:
        """Categorize company by employee count."""
        for bucket, (min_size, max_size) in self.SIZE_BUCKETS.items():
            if min_size <= employee_count <= max_size:
                return bucket
        return 'unknown'
    
    def extract_industries(self, text: str) -> List[str]:
        """Extract industry keywords from text."""
        text_lower = text.lower()
        matched = []
        for industry, keywords in self.INDUSTRY_KEYWORDS.items():
            if any(kw in text_lower for kw in keywords):
                matched.append(industry)
        return matched if matched else ['other']
    
    def analyze_patterns(self) -> Dict[str, Any]:
        """Analyze all customers to find common patterns."""
        
        patterns = {
            'company': {
                'industries': Counter(),
                'sizes': Counter(),
                'locations': Counter(),
                'employee_ranges': [],
            },
            'contact': {
                'titles': Counter(),
                'seniority': Counter(),
                'functions': Counter(),
                'tenure_years': [],
            },
            'behavioral': {
                'post_topics': Counter(),
                'skills': Counter(),
                'activity_level': Counter(),
            },
            'sample_size': len(self.customers),
            'analysis_date': datetime.now().isoformat(),
        }
        
        for customer in self.customers:
            # Company patterns
            if 'company' in customer:
                company = customer['company']
                
                # Industry
                industry = company.get('industry', '')
                if industry:
                    patterns['company']['industries'][industry] += 1
                
                # Size
                emp_count = company.get('employee_count', 0)
                if emp_count:
                    patterns['company']['employee_ranges'].append(emp_count)
                    size_bucket = self.categorize_company_size(emp_count)
                    patterns['company']['sizes'][size_bucket] += 1
                
                # Location
                location = company.get('location', company.get('headquarters', ''))
                if location:
                    # Extract country/region
                    parts = location.split(',')
                    region = parts[-1].strip() if parts else location
                    patterns['company']['locations'][region] += 1
            
            # Contact patterns
            if 'profile' in customer:
                profile = customer['profile']
                
                # Title
                title = profile.get('headline', profile.get('title', ''))
                if title:
                    patterns['contact']['titles'][title] += 1
                    patterns['contact']['seniority'][self.extract_seniority(title)] += 1
                    patterns['contact']['functions'][self.extract_function(title)] += 1
                
                # Skills
                skills = profile.get('skills', [])
                for skill in skills[:10]:  # Top 10 skills
                    skill_name = skill.get('name', skill) if isinstance(skill, dict) else skill
                    patterns['behavioral']['skills'][skill_name] += 1
            
            # Activity patterns
            if 'posts' in customer:
                posts = customer.get('posts', [])
                patterns['behavioral']['activity_level'][len(posts) > 5 and 'active' or 'passive'] += 1
        
        # Calculate aggregates
        if patterns['company']['employee_ranges']:
            emp_ranges = patterns['company']['employee_ranges']
            patterns['company']['employee_stats'] = {
                'min': min(emp_ranges),
                'max': max(emp_ranges),
                'avg': sum(emp_ranges) // len(emp_ranges),
                'median': sorted(emp_ranges)[len(emp_ranges) // 2]
            }
        
        self.patterns = patterns
        return patterns
    
    def generate_icp_config(self) -> Dict[str, Any]:
        """Generate ICP configuration from analyzed patterns."""
        
        if not self.patterns:
            self.analyze_patterns()
        
        patterns = self.patterns
        
        # Get top values
        top_industries = [ind for ind, _ in patterns['company']['industries'].most_common(3)]
        top_sizes = [size for size, _ in patterns['company']['sizes'].most_common(2)]
        top_locations = [loc for loc, _ in patterns['company']['locations'].most_common(3)]
        top_titles = [title for title, _ in patterns['contact']['titles'].most_common(5)]
        top_seniority = [sen for sen, _ in patterns['contact']['seniority'].most_common(2)]
        top_functions = [func for func, _ in patterns['contact']['functions'].most_common(3)]
        top_skills = [skill for skill, _ in patterns['behavioral']['skills'].most_common(10)]
        
        icp_config = {
            'version': '1.0',
            'generated_date': datetime.now().isoformat(),
            'sample_size': patterns['sample_size'],
            
            'company_criteria': {
                'must_have': {
                    'industries': top_industries,
                    'size_buckets': top_sizes,
                },
                'nice_to_have': {
                    'locations': top_locations,
                }
            },
            
            'contact_criteria': {
                'must_have': {
                    'seniority_levels': top_seniority,
                    'functions': top_functions,
                },
                'nice_to_have': {
                    'example_titles': top_titles,
                    'skills': top_skills,
                }
            },
            
            'scoring': {
                'company_fit': {
                    'industry_exact': 20,
                    'industry_adjacent': 10,
                    'size_match': 15,
                    'location_match': 10,
                    'max_points': 50
                },
                'contact_fit': {
                    'title_exact': 15,
                    'title_similar': 8,
                    'seniority_match': 10,
                    'function_match': 5,
                    'max_points': 30
                },
                'engagement': {
                    'recent_activity': 10,
                    'skill_overlap': 5,
                    'content_match': 5,
                    'max_points': 20
                }
            },
            
            'employee_range': patterns['company'].get('employee_stats', {}),
            
            'patterns_raw': {
                'industries': dict(patterns['company']['industries']),
                'sizes': dict(patterns['company']['sizes']),
                'seniority': dict(patterns['contact']['seniority']),
                'functions': dict(patterns['contact']['functions']),
            }
        }
        
        return icp_config


class ProspectScorer:
    """Score prospects against ICP criteria."""
    
    def __init__(self, icp_config: Dict[str, Any]):
        self.icp = icp_config
        self.scoring = icp_config.get('scoring', {})
    
    def score_company(self, company: Dict) -> Dict[str, Any]:
        """Score company against ICP criteria."""
        score = 0
        reasons = []
        
        company_criteria = self.icp.get('company_criteria', {})
        scoring = self.scoring.get('company_fit', {})
        
        # Industry match
        company_industry = company.get('industry', '').lower()
        must_have_industries = [i.lower() for i in company_criteria.get('must_have', {}).get('industries', [])]
        
        if any(ind in company_industry for ind in must_have_industries):
            score += scoring.get('industry_exact', 20)
            reasons.append('Industry exact match')
        elif company_industry:
            score += scoring.get('industry_adjacent', 10)
            reasons.append('Industry adjacent')
        
        # Size match
        emp_count = company.get('employee_count', 0)
        if emp_count:
            emp_range = self.icp.get('employee_range', {})
            min_emp = emp_range.get('min', 0)
            max_emp = emp_range.get('max', float('inf'))
            
            if min_emp <= emp_count <= max_emp * 1.5:
                score += scoring.get('size_match', 15)
                reasons.append('Company size in range')
        
        # Location match
        location = company.get('location', company.get('headquarters', '')).lower()
        nice_to_have_locations = [l.lower() for l in company_criteria.get('nice_to_have', {}).get('locations', [])]
        
        if any(loc in location for loc in nice_to_have_locations):
            score += scoring.get('location_match', 10)
            reasons.append('Geographic match')
        
        return {
            'score': score,
            'max_score': scoring.get('max_points', 50),
            'reasons': reasons
        }
    
    def score_contact(self, profile: Dict) -> Dict[str, Any]:
        """Score contact against ICP criteria."""
        score = 0
        reasons = []
        
        contact_criteria = self.icp.get('contact_criteria', {})
        scoring = self.scoring.get('contact_fit', {})
        
        title = profile.get('headline', profile.get('title', '')).lower()
        
        # Seniority match
        must_have_seniority = contact_criteria.get('must_have', {}).get('seniority_levels', [])
        for seniority in must_have_seniority:
            if seniority in title or any(kw in title for kw in ICPAnalyzer.SENIORITY_LEVELS.get(seniority, [])):
                score += scoring.get('seniority_match', 10)
                reasons.append(f'Seniority match: {seniority}')
                break
        
        # Function match
        must_have_functions = contact_criteria.get('must_have', {}).get('functions', [])
        for function in must_have_functions:
            if function in title:
                score += scoring.get('function_match', 5)
                reasons.append(f'Function match: {function}')
                break
        
        # Title similarity
        example_titles = contact_criteria.get('nice_to_have', {}).get('example_titles', [])
        for example in example_titles:
            if self._title_similarity(title, example.lower()) > 0.5:
                score += scoring.get('title_similar', 8)
                reasons.append('Similar title to ICP')
                break
        
        return {
            'score': score,
            'max_score': scoring.get('max_points', 30),
            'reasons': reasons
        }
    
    def score_engagement(self, data: Dict) -> Dict[str, Any]:
        """Score engagement signals."""
        score = 0
        reasons = []
        
        scoring = self.scoring.get('engagement', {})
        
        # Recent activity
        posts = data.get('posts', [])
        if len(posts) >= 3:
            score += scoring.get('recent_activity', 10)
            reasons.append('Active on LinkedIn')
        
        # Skill overlap
        profile_skills = set(s.lower() if isinstance(s, str) else s.get('name', '').lower() 
                           for s in data.get('profile', {}).get('skills', []))
        icp_skills = set(s.lower() for s in 
                        self.icp.get('contact_criteria', {}).get('nice_to_have', {}).get('skills', []))
        
        overlap = len(profile_skills & icp_skills)
        if overlap >= 3:
            score += scoring.get('skill_overlap', 5)
            reasons.append(f'Skill overlap: {overlap} skills')
        
        return {
            'score': score,
            'max_score': scoring.get('max_points', 20),
            'reasons': reasons
        }
    
    def score_prospect(self, prospect: Dict) -> Dict[str, Any]:
        """Calculate total prospect score."""
        
        company_score = self.score_company(prospect.get('company', {}))
        contact_score = self.score_contact(prospect.get('profile', {}))
        engagement_score = self.score_engagement(prospect)
        
        total_score = company_score['score'] + contact_score['score'] + engagement_score['score']
        max_score = company_score['max_score'] + contact_score['max_score'] + engagement_score['max_score']
        
        all_reasons = company_score['reasons'] + contact_score['reasons'] + engagement_score['reasons']
        
        # Determine tier
        if total_score >= 80:
            tier = 'hot'
        elif total_score >= 60:
            tier = 'warm'
        elif total_score >= 40:
            tier = 'cool'
        else:
            tier = 'low'
        
        return {
            'total_score': total_score,
            'max_score': max_score,
            'percentage': round(total_score / max_score * 100, 1),
            'tier': tier,
            'breakdown': {
                'company_fit': company_score,
                'contact_fit': contact_score,
                'engagement': engagement_score
            },
            'match_reasons': all_reasons,
            'scored_at': datetime.now().isoformat()
        }
    
    def _title_similarity(self, title1: str, title2: str) -> float:
        """Calculate simple title similarity."""
        words1 = set(title1.split())
        words2 = set(title2.split())
        if not words1 or not words2:
            return 0
        intersection = len(words1 & words2)
        union = len(words1 | words2)
        return intersection / union if union > 0 else 0


def main():
    parser = argparse.ArgumentParser(description='AnySite ICP Analyzer')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze customer data to build ICP')
    analyze_parser.add_argument('--input', '-i', required=True, help='Input JSON file with customer data')
    analyze_parser.add_argument('--output', '-o', required=True, help='Output JSON file for ICP config')
    
    # Score command
    score_parser = subparsers.add_parser('score', help='Score a prospect against ICP')
    score_parser.add_argument('--icp', required=True, help='ICP config JSON file')
    score_parser.add_argument('--prospect', required=True, help='Prospect data JSON file')
    score_parser.add_argument('--output', '-o', help='Output file for score results')
    
    args = parser.parse_args()
    
    if args.command == 'analyze':
        # Load customer data
        with open(args.input, 'r') as f:
            customers = json.load(f)
        
        # Analyze
        analyzer = ICPAnalyzer()
        analyzer.load_customers(customers)
        analyzer.analyze_patterns()
        icp_config = analyzer.generate_icp_config()
        
        # Save
        with open(args.output, 'w') as f:
            json.dump(icp_config, f, indent=2)
        
        print(f"ICP config saved to {args.output}")
        print(f"Analyzed {icp_config['sample_size']} customers")
        print(f"Top industries: {icp_config['company_criteria']['must_have']['industries']}")
        print(f"Top seniority: {icp_config['contact_criteria']['must_have']['seniority_levels']}")
    
    elif args.command == 'score':
        # Load ICP config
        with open(args.icp, 'r') as f:
            icp_config = json.load(f)
        
        # Load prospect
        with open(args.prospect, 'r') as f:
            prospect = json.load(f)
        
        # Score
        scorer = ProspectScorer(icp_config)
        result = scorer.score_prospect(prospect)
        
        # Output
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Score saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))
        
        print(f"\nTotal Score: {result['total_score']}/{result['max_score']} ({result['percentage']}%)")
        print(f"Tier: {result['tier'].upper()}")
        print(f"Match Reasons: {', '.join(result['match_reasons'])}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
