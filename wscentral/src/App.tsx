import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface GameState {
      id: number;
      title: string;
      title_kana: string;
      title_english: string;
      description: string; 
      release_date: string;
      release_price: number;
      loose_price: number;
      boxed_price: number;
    }

const App = () => {
   const [games, setGames] = useState<GameState[]>([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/games/')
      .then(response => {
        setGames(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the tasks!", error);
      });
  }, []);
  return (
    <div className="App">
      <h1>Task List</h1>
      <ul>
        {games.map(game => (
          <li key={game.id}>
            <h3>{game.title}</h3>
            <p>{game.description}</p>
            <p>Price: {game.release_price }</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
