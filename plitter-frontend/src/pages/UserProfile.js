import './UserProfile.css';
import { useParams } from 'react-router-dom';
import Pleet from '../components/Pleet';
import { useState, useEffect } from 'react';
// http://127.0.0.1:5001 backend
// Sathvika & Jessica

const UserProfile = props => {
    const { id } = useParams(); // this is the user id, use this to fetch from backend
    const [pleetsArray, setPleetsArray] = useState([]);
    let action = false;

    const addPleet = async () => {
        const response = await fetch("http://127.0.0.1:5001/pleets", {
            method: 'POST'
            // TODO: add more request args
        });
        action = !action;
        return response.json();
    }
    
    const delPleet = async (pleet_id) => {
        const response = await fetch("http://127.0.0.1:5001/pleets/" + pleet_id, {
            method: 'DELETE'
            // TODO: add more request args
        });
        action = !action;
        return response.json();
    }

    useEffect(() => {
        const getPleets = async (id) => {
            const response = await fetch("http://127.0.0.1:5001/users/" + id + "/pleets");
            const pleets = await response.json();
            const pleetsArray = pleets.pleets;
            setPleetsArray(pleetsArray);
        }
        getPleets(id);
    }, [action]);

    // for (let i = 0; i < pleetsArray.length; i++) {
    //     pleetsArray[i] = <Pleet pleet={pleetsArray[i]}/>
    // }
    const newArray = pleetsArray.map(el => <Pleet pleet={el} />);

    return (
        <div>
            <p>Here is the user_id: {id}</p>
            {newArray}
            <div class="button_container">
                <button onClick={delPleet(id.pleet_id)}>delete</button> {/* FIXME: use arrow function here */}
                <button onClick={addPleet}>add</button>
            </div>
        </div>
    );
}


// query backend (pleets)
// organize information
// start designing ui elements

export default UserProfile;  