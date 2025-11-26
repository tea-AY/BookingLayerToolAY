#!/usr/bin/env python3
"""
Adventure Yogi Retreat Data Updater
Run this script to update your app with the latest retreat data from your website.
"""

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json

def scrape_adventure_yogi_retreats():
    """Scrape retreat dates from the Adventure Yogi calendar page"""
    url = "https://adventureyogi.com/calendar/"
    
    try:
        # Make request with proper headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()
        
        # Find date patterns
        pattern = r'(\d{1,2}(?:st|nd|rd|th)?\s+\w+)\s*-\s*(\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4})'
        matches = re.findall(pattern, text_content)
        
        retreats = []
        for i, (start_str, end_str) in enumerate(matches):
            try:
                # Clean and parse dates
                start_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', start_str.strip())
                end_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', end_str.strip())
                
                # Extract year from end date
                year_match = re.search(r'\d{4}', end_clean)
                year = int(year_match.group()) if year_match else 2025
                
                # Parse dates
                start_date = parse_date(start_clean, year)
                end_date = parse_date(end_clean)
                
                if start_date and end_date:
                    duration = (end_date - start_date).days + 1
                    
                    # Determine retreat type
                    if duration == 3:
                        retreat_type = 'Weekend'
                    elif duration == 4:
                        retreat_type = 'Weekend'
                    elif duration == 5:
                        retreat_type = 'Mid-Week'
                    elif duration >= 7:
                        retreat_type = 'Holiday'
                    else:
                        retreat_type = f'{duration} days'
                    
                    retreat = {
                        'id': f"retreat_{year}_{i+1:02d}",
                        'name': "Adventure Yogi Retreat",
                        'start_date': start_date.strftime('%Y-%m-%d'),
                        'end_date': end_date.strftime('%Y-%m-%d'),
                        'location': "TBD",  # You can update this manually
                        'duration': duration,
                        'retreat_type': retreat_type
                    }
                    retreats.append(retreat)
                    
            except Exception as e:
                print(f"Error parsing dates {start_str} - {end_str}: {e}")
                continue
        
        # Filter to only future retreats
        today = datetime.now().date()
        future_retreats = [r for r in retreats if datetime.strptime(r['start_date'], '%Y-%m-%d').date() >= today]
        
        print(f"Found {len(future_retreats)} upcoming retreats")
        return future_retreats
        
    except Exception as e:
        print(f"Error scraping retreats: {e}")
        return []

def parse_date(date_str, year=None):
    """Parse date string with various formats"""
    try:
        formats = ['%d %b %Y', '%d %B %Y', '%d %b', '%d %B']
        
        for fmt in formats:
            try:
                if '%Y' not in fmt and year:
                    date_obj = datetime.strptime(f"{date_str} {year}", fmt + ' %Y')
                else:
                    date_obj = datetime.strptime(date_str, fmt)
                return date_obj
            except ValueError:
                continue
        return None
    except:
        return None

def generate_js_array(retreats):
    """Generate JavaScript array format for the app"""
    js_retreats = []
    
    for retreat in retreats:
        js_retreat = f'''            {{
                id: "{retreat['id']}",
                name: "{retreat['name']}",
                start_date: "{retreat['start_date']}",
                end_date: "{retreat['end_date']}",
                location: "{retreat['location']}",
                duration: {retreat['duration']},
                retreat_type: "{retreat['retreat_type']}"
            }}'''
        js_retreats.append(js_retreat)
    
    return "[\n" + ",\n".join(js_retreats) + "\n        ]"

def main():
    print("🏃‍♀️ Scraping Adventure Yogi retreat data...")
    
    # Scrape retreat data
    retreats = scrape_adventure_yogi_retreats()
    
    if not retreats:
        print("❌ No retreats found. Check your internet connection or website access.")
        return
    
    # Generate JavaScript format
    js_array = generate_js_array(retreats)
    
    # Save as JSON for backup
    with open('retreat_data.json', 'w') as f:
        json.dump(retreats, f, indent=2)
    
    print(f"✅ Found {len(retreats)} upcoming retreats")
    print("\n📋 To update your app:")
    print("1. Open your HTML file")
    print("2. Find the ADVENTURE_YOGI_RETREATS array")
    print("3. Replace it with the following:")
    print("\nconst ADVENTURE_YOGI_RETREATS = " + js_array + ";")
    print("\n📁 Also saved raw data to retreat_data.json")
    
    # Show sample retreats
    print("\n🗓️  Sample upcoming retreats:")
    for retreat in retreats[:5]:
        print(f"  • {retreat['start_date']} to {retreat['end_date']} ({retreat['retreat_type']})")

if __name__ == "__main__":
    main()
