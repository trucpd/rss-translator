document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('data/translated_feeds.json');
        if (!response.ok) {
            throw new Error('Failed to fetch feed data');
        }
        
        const data = await response.json();
        displayEntries(data.entries);
        updateLastUpdated(data.last_updated);
        populateSourceFilter(data.entries);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('loading').textContent = 'Error loading feeds. Please try again later.';
    }
});

function displayEntries(entries) {
    const container = document.getElementById('entries-container');
    container.innerHTML = '';
    
    if (entries.length === 0) {
        container.innerHTML = '<p>No entries available.</p>';
        return;
    }
    
    entries.forEach(entry => {
        const entryElement = document.createElement('div');
        entryElement.className = 'entry';
        entryElement.dataset.source = entry.feed_name;
        
        const title = entry.translated ? entry.translated_title : entry.title;
        const summary = entry.translated ? entry.translated_summary : entry.summary;
        
        entryElement.innerHTML = `
            <div class="entry-source">${entry.feed_name}</div>
            <h2 class="entry-title">${title}</h2>
            <div class="entry-date">${formatDate(entry.published)}</div>
            <div class="entry-summary">${summary}</div>
            <a href="${entry.link}" target="_blank" class="read-more">Read More</a>
        `;
        
        container.appendChild(entryElement);
    });
}

function updateLastUpdated(dateString) {
    const element = document.getElementById('update-time');
    const date = new Date(dateString);
    element.textContent = date.toLocaleString();
}

function formatDate(dateString) {
    if (!dateString) return 'Unknown date';
    
    try {
        const date = new Date(dateString);
        return date.toLocaleString();
    } catch (e) {
        return dateString;
    }
}

function populateSourceFilter(entries) {
    const sources = [...new Set(entries.map(entry => entry.feed_name))];
    const sourceFilter = document.getElementById('source-filter');
    
    sources.forEach(source => {
        const option = document.createElement('option');
        option.value = source;
        option.textContent = source;
        sourceFilter.appendChild(option);
    });
    
    sourceFilter.addEventListener('change', () => {
        const selectedSource = sourceFilter.value;
        filterEntriesBySource(selectedSource);
    });
}

function filterEntriesBySource(source) {
    const entries = document.querySelectorAll('.entry');
    
    entries.forEach(entry => {
        if (source === 'all' || entry.dataset.source === source) {
            entry.style.display = 'block';
        } else {
            entry.style.display = 'none';
        }
    });
}
