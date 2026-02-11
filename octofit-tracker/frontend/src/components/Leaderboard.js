import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const apiUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev/api/leaderboards/`
          : 'http://localhost:8000/api/leaderboards/';
        
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard data:', leaderboardData);
        
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="loading-state"><p>⏳ Loading leaderboard...</p></div>;
  if (error) return <div className="error-state"><p>❌ Error: {error}</p></div>;

  const getRankBadgeClass = (index) => {
    if (index === 0) return 'rank-badge gold';
    if (index === 1) return 'rank-badge silver';
    if (index === 2) return 'rank-badge bronze';
    return 'rank-badge default';
  };

  const getRankEmoji = (index) => {
    if (index === 0) return '🥇';
    if (index === 1) return '🥈';
    if (index === 2) return '🥉';
    return index + 1;
  };

  return (
    <div className="content-wrapper">
      <h2 className="page-header">🏅 Leaderboard</h2>
      <p className="text-muted mb-4">Top performers ranked by total points</p>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Total Activities</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry, index) => (
              <tr key={entry.id || entry._id}>
                <td>
                  <div className={getRankBadgeClass(index)}>
                    {getRankEmoji(index)}
                  </div>
                </td>
                <td><strong>{entry.user_name}</strong></td>
                <td><span className="badge bg-success">{entry.team_name}</span></td>
                <td><span className="badge bg-primary fs-6">{entry.total_points}</span></td>
                <td><span className="badge bg-info">{entry.total_activities}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
