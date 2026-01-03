import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const baseUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev`
          : 'http://localhost:8000';
        const apiUrl = `${baseUrl}/api/workouts/`;
        
        console.log('Workouts - Fetching from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Workouts - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Workouts - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Workout Suggestions</h2>
      <div className="row">
        {workouts.length === 0 ? (
          <div className="col-12">
            <p className="text-center">No workout suggestions found</p>
          </div>
        ) : (
          workouts.map((workout, index) => (
            <div key={workout.id || index} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{workout.name || 'Untitled Workout'}</h5>
                  <p className="card-text">{workout.description || 'No description available'}</p>
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                      <strong>Type:</strong> {workout.workout_type || 'N/A'}
                    </li>
                    <li className="list-group-item">
                      <strong>Difficulty:</strong> {workout.difficulty_level || 'N/A'}
                    </li>
                    <li className="list-group-item">
                      <strong>Duration:</strong> {workout.duration || 'N/A'} min
                    </li>
                    {workout.calories_burned && (
                      <li className="list-group-item">
                        <strong>Calories:</strong> {workout.calories_burned}
                      </li>
                    )}
                  </ul>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Workouts;
