# RSS Translator

A Python application that fetches RSS feeds from multiple sources, translates the content, and displays the translated articles on a web page.

## Features

- Fetches RSS feeds from multiple sources defined in configuration
- Translates feed content using either Google Translate API or OpenAI API
- Displays translated articles on a responsive web interface
- Automatically updates feeds daily via GitHub Actions
- Deployed on GitHub Pages for easy access

## Project Structure

```
/
├── .github/workflows/     # GitHub Actions workflows
├── src/                   # Python source code
├── static/                # Static web assets (CSS, JS)
├── data/                  # Data storage
├── index.html             # Main web page
├── main.py                # Main application script
└── requirements.txt       # Python dependencies
```

## Setup Instructions

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/rss-translator.git
   cd rss-translator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure RSS feeds and translation settings:
   - Edit `data/config.json` to add your RSS feeds and select translation service
   - If using OpenAI, add your API key to the config file

4. Run the application:
   ```
   python main.py
   ```

5. Open `index.html` in your browser to view the translated feeds

### GitHub Pages Deployment

1. Push the repository to GitHub
2. Enable GitHub Pages in repository settings
   - Set the source to the main branch
3. GitHub Actions will automatically update the feeds daily

## Configuration

Edit the `data/config.json` file to customize:

- RSS feed sources (URL, name, language)
- Translation service (Google or OpenAI)
- Target language for translation
- Fields to translate (title, summary, etc.)

## License

MIT License