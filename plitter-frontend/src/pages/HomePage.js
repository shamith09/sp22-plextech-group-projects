import './HomePage.css';
import Pleet from '../components/Pleet';
import { useState, useEffect } from 'react';

// http://127.0.0.1:5001 backend
// Nandish & Vishal


const HomePage = props => {
  const [array, setArray] = useState([]);
  useEffect ( () => {
    const getPleets = async () => {
      const response = await fetch('http://127.0.0.1:5001/pleets');
      const json1 = await response.json();
      setArray(json1.pleets);
    }
    getPleets();
  },[]);

  return (
    <div>
      <h1>This is the Home Page!</h1>
      {array.map(el => <Pleet key={el.pleet_id} pleet={el}/>)}
    </div> 
  );
}

export default HomePage;

// query pleets to get top 10 
// display + stylize