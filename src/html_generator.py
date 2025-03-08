import json
from datetime import datetime

class HtmlGenerator:
    def __init__(self, template_path='index.html'):
        self.template_path = template_path
        
    def generate_json(self, translated_entries, output_path):
        """Generate JSON file with translated entries"""
        output_data = {
            'last_updated': datetime.now().isoformat(),
            'entries': translated_entries
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
