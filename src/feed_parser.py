import feedparser
import json
import time

class FeedParser:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
    def parse_feeds(self):
        """Parse all feeds defined in the config file"""
        all_entries = []
        
        for feed in self.config['feeds']:
            try:
                parsed_feed = feedparser.parse(feed['url'])
                
                for entry in parsed_feed.entries[:10]:  # Limit to 10 entries per feed
                    entry_data = {
                        'feed_name': feed['name'],
                        'source_language': feed['language'],
                        'title': entry.title,
                        'link': entry.link,
                        'published': entry.get('published', ''),
                        'summary': entry.get('summary', ''),
                        'timestamp': time.time()
                    }
                    all_entries.append(entry_data)
                    
            except Exception as e:
                print(f"Error parsing feed {feed['name']}: {e}")
        
        return all_entries
