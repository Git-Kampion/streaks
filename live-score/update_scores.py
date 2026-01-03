import json
import sqlite3
from datetime import datetime, timedelta
import random
from pathlib import Path

class ScoreUpdater:
    def __init__(self):
        self.data_dir = Path('data')
        self.data_dir.mkdir(exist_ok=True)
        
        # Sample teams data - replace with your actual teams
        self.teams_file = self.data_dir / 'teams.json'
        self.scores_file = self.data_dir / 'scores.json'
        
        self.init_teams_data()
    
    def init_teams_data(self):
        """Initialize sample teams data"""
        if not self.teams_file.exists():
            teams_data = {
                "teams": [
                    "Manchester United", "Liverpool", "Arsenal", "Chelsea", 
                    "Manchester City", "Tottenham", "Newcastle", "Aston Villa",
                    "Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla",
                    "Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Bayer Leverkusen",
                    "Juventus", "AC Milan", "Inter Milan", "Napoli",
                    "Paris Saint-Germain", "Marseille", "Lyon", "Monaco"
                ],
                "leagues": [
                    "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"
                ]
            }
            self.save_json(self.teams_file, teams_data)
    
    def generate_mock_scores(self):
        """Generate realistic mock scores - replace with your actual data source"""
        teams_data = self.load_json(self.teams_file)
        matches = []
        
        for league in teams_data['leagues']:
            # Generate 4-6 matches per league
            for i in range(random.randint(4, 6)):
                home_team = random.choice(teams_data['teams'])
                away_team = random.choice([t for t in teams_data['teams'] if t != home_team])
                
                # Random status with weights
                status_weights = ['scheduled'] * 3 + ['live'] * 1 + ['finished'] * 2
                status = random.choice(status_weights)
                
                match_date = datetime.now() + timedelta(days=random.randint(-2, 7))
                
                if status == 'scheduled':
                    home_score = away_score = 0
                    minute = None
                elif status == 'live':
                    home_score = random.randint(0, 3)
                    away_score = random.randint(0, 3)
                    minute = random.randint(1, 90)
                else:  # finished
                    home_score = random.randint(0, 5)
                    away_score = random.randint(0, 5)
                    minute = 'FT'
                
                match = {
                    'id': f"{league.replace(' ', '_').lower()}_{i}",
                    'league': league,
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_score': home_score,
                    'away_score': away_score,
                    'status': status,
                    'date': match_date.strftime('%Y-%m-%d'),
                    'time': match_date.strftime('%H:%M'),
                    'minute': minute,
                    'venue': f"Stadium {random.randint(1, 10)}",
                    'last_updated': datetime.now().isoformat()
                }
                
                # Add events for live/finished matches
                if status != 'scheduled':
                    match['events'] = self.generate_match_events(home_team, away_team, home_score, away_score)
                
                matches.append(match)
        
        return {'matches': matches, 'last_updated': datetime.now().isoformat()}
    
    def generate_match_events(self, home_team, away_team, home_score, away_score):
        """Generate mock match events"""
        events = []
        events_count = home_score + away_score + random.randint(0, 3)
        
        for _ in range(events_count):
            event_type = random.choice(['Goal', 'Yellow Card', 'Red Card', 'Substitution'])
            team = random.choice([home_team, away_team])
            player = f"Player {random.randint(1, 23)}"
            minute = random.randint(1, 90)
            
            events.append({
                'type': event_type,
                'team': team,
                'player': player,
                'minute': minute
            })
        
        return sorted(events, key=lambda x: x['minute'])
    
    def load_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_json(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def update_scores(self):
        """Update scores data"""
        print("Updating scores...")
        scores_data = self.generate_mock_scores()
        self.save_json(self.scores_file, scores_data)
        print(f"Scores updated at {datetime.now()}")

if __name__ == "__main__":
    updater = ScoreUpdater()
    updater.update_scores()