import json
from googletrans import Translator as GoogleTranslator
import openai

class Translator:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
            
        self.service = self.config['translation']['service']
        self.target_language = self.config['translation']['target_language']
        
        if self.service == "openai" and self.config['translation']['openai_api_key']:
            openai.api_key = self.config['translation']['openai_api_key']
            
        self.google_translator = GoogleTranslator()
            
    def translate_entry(self, entry):
        """Translate specified fields of an entry"""
        translated_entry = entry.copy()
        
        # Skip translation if the source language is the same as the target language
        if entry['source_language'] == self.target_language:
            translated_entry['translated'] = False
            return translated_entry
        
        for field in self.config['translation']['fields_to_translate']:
            if field in entry and entry[field]:
                try:
                    if self.service == "google":
                        translated_text = self.google_translator.translate(
                            entry[field], 
                            src=entry['source_language'], 
                            dest=self.target_language
                        ).text
                    elif self.service == "openai":
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": f"Translate the following text from {entry['source_language']} to {self.target_language}:"},
                                {"role": "user", "content": entry[field]}
                            ]
                        )
                        translated_text = response.choices[0].message.content.strip()
                    
                    translated_entry[f"translated_{field}"] = translated_text
                except Exception as e:
                    print(f"Translation error for {field}: {e}")
                    translated_entry[f"translated_{field}"] = entry[field]
        
        translated_entry['translated'] = True
        return translated_entry
    
    def translate_entries(self, entries):
        """Translate all entries"""
        translated_entries = []
        
        for entry in entries:
            translated_entry = self.translate_entry(entry)
            translated_entries.append(translated_entry)
            
        return translated_entries
