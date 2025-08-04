import json
from datetime import datetime, timedelta

def analyze_fixtures(fixtures_data):
    today = datetime.now().date()
    
    # Initialize counters
    results = {
        "total_fixtures": 0,
        "fixtures_in_august_2025": 0,
        "fixtures_left_from_today": 0,
        "today": today.strftime("%Y-%m-%d"),
        "weekly_counts": {
            "Week 1 (Jul 28 - Aug 3)": 0,
            "Week 2 (Aug 4 - Aug 10)": 0,
            "Week 3 (Aug 11 - Aug 17)": 0,
            "Week 4 (Aug 18 - Aug 24)": 0,
            "Week 5 (Aug 25 - Aug 31)": 0
        },
        "upcoming_fixtures": []
    }

    for fixture in fixtures_data:
        # Parse date
        date_str = fixture["date"]
        if "-" in date_str:
            fixture_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            fixture_date = datetime.strptime(date_str, "%Y/%m/%d").date()
        
        results["total_fixtures"] += 1
        
        # August 2025 analysis
        if fixture_date.month == 8 and fixture_date.year == 2025:
            results["fixtures_in_august_2025"] += 1
            
            # Weekly count
            day = fixture_date.day
            if day <= 3:
                week = "Week 1 (Jul 28 - Aug 3)"
            elif day <= 10:
                week = "Week 2 (Aug 4 - Aug 10)"
            elif day <= 17:
                week = "Week 3 (Aug 11 - Aug 17)"
            elif day <= 24:
                week = "Week 4 (Aug 18 - Aug 24)"
            else:
                week = "Week 5 (Aug 25 - Aug 31)"
            
            results["weekly_counts"][week] += 1
            
            # Upcoming fixtures
            if fixture_date >= today:
                results["fixtures_left_from_today"] += 1
                results["upcoming_fixtures"].append({
                    "date": date_str,
                    "home": fixture["home"],
                    "away": fixture["away"],
                    "round": fixture["round"]
                })

    return results

# Load the JSON data
with open("fixtures.json", "r", encoding="utf-8") as file:
    fixtures_data = json.load(file)

# Get analysis results
analysis = analyze_fixtures(fixtures_data)

# Print summary
print(f"Total fixtures: {analysis['total_fixtures']}")
print(f"Fixtures in August 2025: {analysis['fixtures_in_august_2025']}")
print(f"Fixtures left from today ({analysis['today']}) onwards: {analysis['fixtures_left_from_today']}\n")

# Print weekly breakdown
print("Weekly Breakdown for August 2025:")
for week, count in analysis["weekly_counts"].items():
    print(f"{week}: {count} fixtures")

# Print upcoming fixtures if any
'''
if analysis["upcoming_fixtures"]:
    print("\nUpcoming Fixtures:")
    for fixture in analysis["upcoming_fixtures"]:
        print(f"{fixture['date']} | {fixture['home']} vs {fixture['away']} (Round {fixture['round']})")
else:
    print("\nNo upcoming fixtures in August 2025.")
    '''