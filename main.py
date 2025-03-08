import os
import json
from src.feed_parser import FeedParser
from src.translator import Translator
from src.html_generator import HtmlGenerator

def main():
    # Create necessary directories
    os.makedirs('data', exist_ok=True)
    
    # Paths
    config_path = 'data/config.json'
    output_path = 'data/translated_feeds.json'
    
    # Check if config file exists
    if not os.path.exists(config_path):
        print(f"Config file not found at {config_path}")
        return
    
    print("Parsing RSS feeds...")
    feed_parser = FeedParser(config_path)
    entries = feed_parser.parse_feeds()
    print(f"Parsed {len(entries)} entries from feeds")
    
    print("Translating entries...")
    translator = Translator(config_path)
    translated_entries = translator.translate_entries(entries)
    print(f"Translated {len(translated_entries)} entries")
    
    print("Generating output...")
    html_generator = HtmlGenerator()
    html_generator.generate_json(translated_entries, output_path)
    print(f"Output generated at {output_path}")
    
    print("RSS translation complete!")

if __name__ == "__main__":
    main()
