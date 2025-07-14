#!/usr/bin/env python3
"""
Design Inspiration API Integration Module
Fetches design inspiration from Pinterest, Dribbble, Behance, and RSS feeds
"""

import asyncio
import aiohttp
import feedparser
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import datetime
import logging
from urllib.parse import urljoin, urlparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class DesignInspiration:
    """Represents a design inspiration item"""
    title: str
    description: str
    image_url: str
    source_url: str
    author: str
    platform: str
    tags: List[str]
    created_date: str
    engagement_metrics: Dict[str, Any]

class DesignInspirationAPI:
    """Main class for fetching design inspiration from multiple sources"""
    
    def __init__(self, api_keys: Dict[str, str] = None):
        """Initialize with API keys"""
        self.api_keys = api_keys or {}
        self.session = None
        
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def fetch_pinterest_inspiration(self, query: str, limit: int = 20) -> List[DesignInspiration]:
        """
        Fetch design inspiration from Pinterest
        Note: Pinterest API requires approval - using RSS as backup
        """
        try:
            # Pinterest RSS feed approach for public content
            rss_url = f"https://www.pinterest.com/search/pins/?q={query}&rs=typed&term_meta[]={query}%7Ctyped"
            
            # For now, use RSS feeds as Pinterest API is restricted
            return await self._fetch_pinterest_rss(query, limit)
            
        except Exception as e:
            logger.error(f"Pinterest API error: {e}")
            return []
    
    async def fetch_dribbble_inspiration(self, query: str, limit: int = 20) -> List[DesignInspiration]:
        """Fetch design inspiration from Dribbble API"""
        if 'dribbble' not in self.api_keys:
            logger.warning("Dribbble API key not provided")
            return []
        
        try:
            url = "https://api.dribbble.com/v2/shots"
            headers = {
                'Authorization': f'Bearer {self.api_keys["dribbble"]}',
                'Accept': 'application/json'
            }
            
            params = {
                'per_page': limit,
                'sort': 'popular'
            }
            
            if query:
                params['q'] = query
            
            async with self.session.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return [self._parse_dribbble_item(item) for item in data]
                else:
                    logger.error(f"Dribbble API error: {response.status}")
                    return []
                    
        except Exception as e:
            logger.error(f"Dribbble API error: {e}")
            return []
    
    async def fetch_behance_inspiration(self, query: str, limit: int = 20) -> List[DesignInspiration]:
        """Fetch design inspiration from Behance API"""
        if 'behance' not in self.api_keys:
            logger.warning("Behance API key not provided")
            return []
        
        try:
            url = "https://api.behance.net/v2/projects"
            params = {
                'api_key': self.api_keys['behance'],
                'q': query,
                'per_page': limit,
                'sort': 'appreciations'
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    projects = data.get('projects', [])
                    return [self._parse_behance_item(item) for item in projects]
                else:
                    logger.error(f"Behance API error: {response.status}")
                    return []
                    
        except Exception as e:
            logger.error(f"Behance API error: {e}")
            return []
    
    async def fetch_design_rss_feeds(self, sources: List[str] = None) -> List[DesignInspiration]:
        """Fetch design inspiration from RSS feeds"""
        if not sources:
            sources = [
                "https://www.awwwards.com/rss/",
                "https://feeds.feedburner.com/css-tricks",
                "https://feeds.feedburner.com/smashingmagazine",
                "https://dribbble.com/shots/popular.rss",
                "https://www.behance.net/feeds/projects"
            ]
        
        all_items = []
        
        for source in sources:
            try:
                items = await self._fetch_rss_feed(source)
                all_items.extend(items)
            except Exception as e:
                logger.error(f"RSS feed error for {source}: {e}")
                continue
        
        return all_items
    
    async def fetch_all_inspiration(self, query: str, limit_per_source: int = 10) -> Dict[str, List[DesignInspiration]]:
        """Fetch inspiration from all available sources"""
        results = {}
        
        # Fetch from all sources concurrently
        tasks = []
        
        if 'pinterest' in self.api_keys or True:  # Pinterest RSS always available
            tasks.append(('pinterest', self.fetch_pinterest_inspiration(query, limit_per_source)))
        
        if 'dribbble' in self.api_keys:
            tasks.append(('dribbble', self.fetch_dribbble_inspiration(query, limit_per_source)))
        
        if 'behance' in self.api_keys:
            tasks.append(('behance', self.fetch_behance_inspiration(query, limit_per_source)))
        
        # Always fetch RSS feeds
        tasks.append(('rss', self.fetch_design_rss_feeds()))
        
        # Execute all tasks concurrently
        completed_tasks = await asyncio.gather(*[task[1] for task in tasks], return_exceptions=True)
        
        # Process results
        for i, (source_name, _) in enumerate(tasks):
            result = completed_tasks[i]
            if isinstance(result, Exception):
                logger.error(f"Error fetching from {source_name}: {result}")
                results[source_name] = []
            else:
                results[source_name] = result
        
        return results
    
    # Helper methods for parsing different API responses
    
    def _parse_dribbble_item(self, item: Dict) -> DesignInspiration:
        """Parse Dribbble API response item"""
        return DesignInspiration(
            title=item.get('title', ''),
            description=item.get('description', ''),
            image_url=item.get('images', {}).get('normal', ''),
            source_url=item.get('html_url', ''),
            author=item.get('user', {}).get('name', ''),
            platform='dribbble',
            tags=item.get('tags', []),
            created_date=item.get('created_at', ''),
            engagement_metrics={
                'likes': item.get('likes_count', 0),
                'views': item.get('views_count', 0),
                'comments': item.get('comments_count', 0)
            }
        )
    
    def _parse_behance_item(self, item: Dict) -> DesignInspiration:
        """Parse Behance API response item"""
        return DesignInspiration(
            title=item.get('name', ''),
            description=item.get('description', ''),
            image_url=item.get('covers', {}).get('404', ''),
            source_url=item.get('url', ''),
            author=item.get('owners', [{}])[0].get('display_name', ''),
            platform='behance',
            tags=item.get('tags', []),
            created_date=item.get('created_on', ''),
            engagement_metrics={
                'appreciations': item.get('stats', {}).get('appreciations', 0),
                'views': item.get('stats', {}).get('views', 0),
                'comments': item.get('stats', {}).get('comments', 0)
            }
        )
    
    async def _fetch_pinterest_rss(self, query: str, limit: int) -> List[DesignInspiration]:
        """Fetch Pinterest content via RSS (fallback method)"""
        try:
            # Pinterest RSS feeds are limited, this is a basic implementation
            # You might want to implement web scraping for better results
            return []
        except Exception as e:
            logger.error(f"Pinterest RSS error: {e}")
            return []
    
    async def _fetch_rss_feed(self, url: str) -> List[DesignInspiration]:
        """Fetch and parse RSS feed"""
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    feed = feedparser.parse(content)
                    
                    items = []
                    for entry in feed.entries[:20]:  # Limit to 20 items
                        item = self._parse_rss_item(entry, url)
                        if item:
                            items.append(item)
                    
                    return items
                else:
                    logger.error(f"RSS feed error: {response.status} for {url}")
                    return []
                    
        except Exception as e:
            logger.error(f"RSS feed error: {e}")
            return []
    
    def _parse_rss_item(self, entry: Any, source_url: str) -> Optional[DesignInspiration]:
        """Parse RSS feed entry"""
        try:
            # Determine platform from URL
            domain = urlparse(source_url).netloc
            platform = 'rss'
            if 'dribbble' in domain:
                platform = 'dribbble'
            elif 'behance' in domain:
                platform = 'behance'
            elif 'awwwards' in domain:
                platform = 'awwwards'
            elif 'css-tricks' in domain:
                platform = 'css-tricks'
            elif 'smashingmagazine' in domain:
                platform = 'smashingmagazine'
            
            # Extract image URL from content
            image_url = ''
            if hasattr(entry, 'media_content') and entry.media_content:
                image_url = entry.media_content[0].get('url', '')
            elif hasattr(entry, 'links'):
                for link in entry.links:
                    if link.get('type', '').startswith('image/'):
                        image_url = link.get('href', '')
                        break
            
            return DesignInspiration(
                title=entry.get('title', ''),
                description=entry.get('summary', ''),
                image_url=image_url,
                source_url=entry.get('link', ''),
                author=entry.get('author', ''),
                platform=platform,
                tags=entry.get('tags', []),
                created_date=entry.get('published', ''),
                engagement_metrics={}
            )
            
        except Exception as e:
            logger.error(f"RSS item parsing error: {e}")
            return None

class DesignInspirationManager:
    """High-level manager for design inspiration integration"""
    
    def __init__(self, api_keys: Dict[str, str] = None):
        self.api_keys = api_keys or {}
        self.cache = {}
        self.cache_expiry = 3600  # 1 hour
    
    async def get_inspiration_for_project(self, project_keywords: List[str], 
                                        project_type: str = "web") -> Dict[str, Any]:
        """Get curated design inspiration for a specific project"""
        
        # Combine keywords for search
        search_query = " ".join(project_keywords + [project_type])
        
        async with DesignInspirationAPI(self.api_keys) as api:
            results = await api.fetch_all_inspiration(search_query, limit_per_source=15)
        
        # Process and categorize results
        processed_results = {
            'query': search_query,
            'total_items': sum(len(items) for items in results.values()),
            'by_platform': results,
            'curated_recommendations': self._curate_recommendations(results, project_type),
            'trending_tags': self._extract_trending_tags(results),
            'generated_at': datetime.datetime.now().isoformat()
        }
        
        return processed_results
    
    def _curate_recommendations(self, results: Dict[str, List[DesignInspiration]], 
                               project_type: str) -> List[DesignInspiration]:
        """Curate top recommendations based on project type"""
        all_items = []
        for platform_items in results.values():
            all_items.extend(platform_items)
        
        # Sort by engagement metrics
        sorted_items = sorted(all_items, 
                            key=lambda x: sum(x.engagement_metrics.values()), 
                            reverse=True)
        
        # Return top 10 curated items
        return sorted_items[:10]
    
    def _extract_trending_tags(self, results: Dict[str, List[DesignInspiration]]) -> List[str]:
        """Extract trending tags from all results"""
        tag_counts = {}
        
        for platform_items in results.values():
            for item in platform_items:
                for tag in item.tags:
                    tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        # Return top 10 trending tags
        return sorted(tag_counts.keys(), key=lambda x: tag_counts[x], reverse=True)[:10]
    
    async def generate_inspiration_report(self, project_name: str, 
                                        keywords: List[str]) -> str:
        """Generate a comprehensive inspiration report"""
        
        inspiration_data = await self.get_inspiration_for_project(keywords)
        
        report = f"""
# Design Inspiration Report: {project_name}

**Generated:** {inspiration_data['generated_at']}
**Search Query:** {inspiration_data['query']}
**Total Items Found:** {inspiration_data['total_items']}

## Trending Tags
{', '.join(inspiration_data['trending_tags'])}

## Top Recommendations

"""
        
        for i, item in enumerate(inspiration_data['curated_recommendations'], 1):
            report += f"""
### {i}. {item.title}
**Platform:** {item.platform}
**Author:** {item.author}
**Link:** {item.source_url}
**Description:** {item.description}
**Engagement:** {item.engagement_metrics}

"""
        
        report += f"""
## Results by Platform

"""
        
        for platform, items in inspiration_data['by_platform'].items():
            report += f"""
### {platform.title()} ({len(items)} items)
"""
            for item in items[:5]:  # Show top 5 per platform
                report += f"- [{item.title}]({item.source_url}) by {item.author}\n"
        
        report += """

---
*Generated by Fusion v11 Design Inspiration API*
"""
        
        return report

# Example usage and integration functions
async def main():
    """Example usage of the Design Inspiration API"""
    
    # Example API keys (replace with your actual keys)
    api_keys = {
        'dribbble': 'your_dribbble_token',
        'behance': 'your_behance_api_key',
        'pinterest': 'your_pinterest_access_token'
    }
    
    # Create manager
    manager = DesignInspirationManager(api_keys)
    
    # Get inspiration for a project
    project_keywords = ['mobile app', 'fintech', 'dashboard']
    inspiration = await manager.get_inspiration_for_project(project_keywords, 'mobile')
    
    # Generate report
    report = await manager.generate_inspiration_report('Fintech Mobile App', project_keywords)
    
    # Save report
    with open('design_inspiration_report.md', 'w') as f:
        f.write(report)
    
    print("Design inspiration report generated!")
    print(f"Found {inspiration['total_items']} items across {len(inspiration['by_platform'])} platforms")

if __name__ == "__main__":
    asyncio.run(main()) 