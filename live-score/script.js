class LiveScores {
    constructor() {
        this.scoresData = null;
        this.updateInterval = 45 * 60 * 1000; // 45 minutes
        this.init();
    }

    init() {
        this.loadScores();
        this.setupEventListeners();
        this.startAutoRefresh();
    }

    async loadScores() {
        try {
            this.showLoading();
            const response = await fetch('data/scores.json');
            this.scoresData = await response.json();
            this.displayScores();
            this.updateLastUpdateTime();
            this.hideLoading();
        } catch (error) {
            console.error('Error loading scores:', error);
            this.showError('Failed to load scores');
        }
    }

    displayScores() {
        const container = document.getElementById('matchesContainer');
        const searchTerm = document.getElementById('searchInput').value.toLowerCase();
        const statusFilter = document.getElementById('statusFilter').value;

        const filteredMatches = this.scoresData.matches.filter(match => {
            const matchesSearch = match.home_team.toLowerCase().includes(searchTerm) ||
                match.away_team.toLowerCase().includes(searchTerm) ||
                match.league.toLowerCase().includes(searchTerm);
            const matchesStatus = statusFilter === 'all' || match.status === statusFilter;
            return matchesSearch && matchesStatus;
        });

        if (filteredMatches.length === 0) {
            container.innerHTML = '<div class="no-matches">No matches found</div>';
            return;
        }

        container.innerHTML = filteredMatches.map(match => this.createMatchCard(match)).join('');
    }

    createMatchCard(match) {
        const isLive = match.status === 'live';
        const isFinished = match.status === 'finished';
        const isScheduled = match.status === 'scheduled';

        return `
            <div class="match-card ${match.status}" onclick="this.classList.toggle('expanded')">
                <div class="match-header">
                    <span class="league">${match.league}</span>
                    <span class="match-status status-${match.status}">
                        ${isLive ? '?? LIVE' : isFinished ? '? FINISHED' : '? ' + match.time}
                    </span>
                </div>
                <div class="match-content">
                    <div class="team team-home">
                        <div class="team-logo">${this.getTeamInitials(match.home_team)}</div>
                        <div class="team-name">${match.home_team}</div>
                    </div>
                    <div class="score-area">
                        ${isScheduled ?
                '<div class="vs">VS</div>' :
                `<div class="score">${match.home_score} - ${match.away_score}</div>`
            }
                        ${isLive ? '<div class="match-time">' + match.minute + "'</div>" : ''}
                    </div>
                    <div class="team team-away">
                        <div class="team-logo">${this.getTeamInitials(match.away_team)}</div>
                        <div class="team-name">${match.away_team}</div>
                    </div>
                </div>
                ${this.createMatchDetails(match)}
            </div>
        `;
    }

    createMatchDetails(match) {
        if (match.status === 'scheduled') {
            return `
                <div class="match-details">
                    <div><strong>Date:</strong> ${match.date}</div>
                    <div><strong>Time:</strong> ${match.time}</div>
                    <div><strong>Venue:</strong> ${match.venue}</div>
                </div>
            `;
        }

        return `
            <div class="match-details">
                ${match.status === 'finished' ?
                `<div><strong>Final Score</strong></div>` :
                `<div><strong>Live:</strong> ${match.minute}' minute</div>`
            }
                ${match.events ? `
                    <div class="match-events">
                        ${match.events.map(event =>
                `<div>${event.minute}' ${event.type}: ${event.player}</div>`
            ).join('')}
                    </div>
                ` : ''}
            </div>
        `;
    }

    getTeamInitials(teamName) {
        return teamName.split(' ').map(word => word[0]).join('').toUpperCase().substring(0, 3);
    }

    setupEventListeners() {
        document.getElementById('searchInput').addEventListener('input', () => this.displayScores());
        document.getElementById('statusFilter').addEventListener('change', () => this.displayScores());
        document.getElementById('refreshBtn').addEventListener('click', () => this.loadScores());
    }

    startAutoRefresh() {
        setInterval(() => {
            this.loadScores();
        }, this.updateInterval);
    }

    updateLastUpdateTime() {
        const lastUpdateElement = document.getElementById('lastUpdate');
        lastUpdateElement.textContent = new Date().toLocaleString();
    }

    showLoading() {
        document.getElementById('loading').style.display = 'block';
    }

    hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }

    showError(message) {
        const container = document.getElementById('matchesContainer');
        container.innerHTML = `<div class="error">${message}</div>`;
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    new LiveScores();
});