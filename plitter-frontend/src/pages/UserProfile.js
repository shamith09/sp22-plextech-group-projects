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

    const [pleetValue, setPleetsValue] = useState("");
    const addPleet = async () => {
        const data = {
            username: pleetsArray[0].user.username,
            text: pleetValue
        }
        const response = await fetch("http://127.0.0.1:5001/pleets", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
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
            const response = await fetch("http://127.0.0.1:2500/users/" + id + "/pleets");
            const pleets = await response.json();
            const pleetsArray = pleets.pleets;
            setPleetsArray(pleetsArray);
        }
        getPleets(id);
    }, [action]);

    // for (let i = 0; i < pleetsArray.length; i++) {
    //     pleetsArray[i] = <Pleet pleet={pleetsArray[i]}/>
    // }
    const newArray = pleetsArray.map(el => {
        return (
            <div className="pleetsclass">
                <Pleet pleet={el} />
                <div class="delete_button">
                    <button onClick={() => delPleet(el.pleet_id)}>DELETE</button>
                </div>
            </div>
        );
    });

    const handleSubmit = () => {
        addPleet();
    }

    const handleChange = (value) => {
        setPleetsValue(value.target.value);
    }

    return (
        <div>
            <p>Here is the user_id: {id}</p>
            {newArray}
            <p>Add a new pleet</p>
            <form onSubmit={() => handleSubmit()}>
                <input type="text" name="newPleet" value={pleetValue} onChange={(value) => handleChange(value)}>
                </input>
                <button onClick={() => handleSubmit()}>SUBMIT</button>
            </form>
            {/* <div class="add_button">
                <button onClick={() => handleSubmit()}>SUBMIT</button>
            </div> */}
        </div>
    );
}

// query backend (pleets)
// organize information
// start designing ui elements

export default UserProfile;  