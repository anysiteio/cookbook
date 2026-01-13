#!/usr/bin/env python3
"""
Helper utilities for person analysis workflow.
Provides date calculations for filtering LinkedIn data by timeframes.
"""

from datetime import datetime, timedelta
import sys


def get_date_filter(days_ago: int) -> str:
    """
    Calculate ISO timestamp for X days ago.
    Used for posted_after and commented_after filters.
    
    Args:
        days_ago: Number of days to go back
        
    Returns:
        ISO 8601 formatted timestamp string
        
    Examples:
        >>> get_date_filter(90)  # 90 days ago
        '2024-08-14T00:00:00Z'
    """
    target_date = datetime.now() - timedelta(days=days_ago)
    return target_date.strftime('%Y-%m-%dT%H:%M:%SZ')


def calculate_posting_frequency(post_count: int, days: int) -> dict:
    """
    Calculate posting frequency metrics.
    
    Args:
        post_count: Number of posts in the period
        days: Number of days in the period
        
    Returns:
        Dictionary with frequency metrics
    """
    posts_per_week = (post_count / days) * 7
    posts_per_month = (post_count / days) * 30
    
    return {
        'posts_per_week': round(posts_per_week, 1),
        'posts_per_month': round(posts_per_month, 1),
        'activity_level': classify_activity(posts_per_week)
    }


def classify_activity(posts_per_week: float) -> str:
    """Classify user activity level based on posting frequency."""
    if posts_per_week >= 5:
        return "Very High"
    elif posts_per_week >= 2:
        return "High"
    elif posts_per_week >= 1:
        return "Medium"
    elif posts_per_week >= 0.25:
        return "Low"
    else:
        return "Very Low"


def calculate_engagement_rate(total_reactions: int, post_count: int) -> dict:
    """
    Calculate engagement metrics.
    
    Args:
        total_reactions: Sum of all reactions across posts
        post_count: Number of posts
        
    Returns:
        Dictionary with engagement metrics
    """
    if post_count == 0:
        return {'avg_reactions': 0, 'engagement_level': 'No Activity'}
    
    avg_reactions = total_reactions / post_count
    
    return {
        'avg_reactions': round(avg_reactions, 1),
        'engagement_level': classify_engagement(avg_reactions)
    }


def classify_engagement(avg_reactions: float) -> str:
    """Classify engagement level based on average reactions per post."""
    if avg_reactions >= 100:
        return "Very High"
    elif avg_reactions >= 50:
        return "High"
    elif avg_reactions >= 20:
        return "Medium"
    elif avg_reactions >= 10:
        return "Low"
    else:
        return "Very Low"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analysis_helpers.py <days_ago>")
        print("Example: python analysis_helpers.py 90")
        sys.exit(1)
    
    days_ago = int(sys.argv[1])
    date_filter = get_date_filter(days_ago)
    print(f"Date filter for {days_ago} days ago: {date_filter}")
    print("\nStandard timeframes:")
    print(f"  90 days (active users): {get_date_filter(90)}")
    print(f"  180 days (less active): {get_date_filter(180)}")
    print(f"  30 days (recent only): {get_date_filter(30)}")
