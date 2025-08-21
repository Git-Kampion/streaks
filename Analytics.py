import json
from datetime import datetime, timedelta
from collections import defaultdict

def parse_date(date_str):
    """Parse date from different formats in the JSON"""
    try:
        if '.' in date_str and len(date_str.split('.')[0]) <= 2:
            day, month = date_str.split('.')[:2]
            return datetime(2025, int(month), int(day)).date()
        elif '-' in date_str:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, IndexError):
        return None

# Load fixtures data
with open('fixturesAnlytics.json', 'r') as f:
    fixtures = json.load(f)

# Define date range (August 4-10, 2025)
start_date = datetime(2025, 8, 4).date()
end_date = datetime(2025, 8, 10).date()

# Process fixtures
daily_fixtures = defaultdict(list)
total_fixtures = 0

for fixture in fixtures:
    date = parse_date(fixture['date'])
    if date and start_date <= date <= end_date:
        daily_fixtures[date].append(fixture)
        total_fixtures += 1

# Sort dates chronologically
sorted_dates = sorted(daily_fixtures.keys())

# Display header
print(f"\nFixtures for Week of August 4-10, 2025 (Monday to Sunday)")
print("=" * 70)
print(f"{'Date':<15}{'Day':<12}{'Matches':<45}{'Count':<5}")
print("-" * 70)

# Display fixtures by day with counts
for date in sorted_dates:
    day_name = date.strftime('%A')
    fixtures_list = daily_fixtures[date]
    count = len(fixtures_list)
    
    # Display first fixture with date and count
    first_fixture = fixtures_list[0]
    print(f"{date.strftime('%Y-%m-%d'):<15}{day_name:<12}"
          f"{first_fixture['home']} vs {first_fixture['away']:<30}"
          f"{count:>3}")
    
    # Display remaining fixtures for the same day
    for fixture in fixtures_list[1:]:
        print(f"{' ' * 27}{fixture['home']} vs {fixture['away']}")

# Display totals
print("=" * 70)
print(f"{'DAILY TOTALS:':<27}", end="")
for date in sorted_dates:
    print(f"{date.strftime('%a')}: {len(daily_fixtures[date]):<3}", end=" ")
print(f"\n{'WEEKLY TOTAL:':<27}{total_fixtures:>3} fixtures")
print("=" * 70)