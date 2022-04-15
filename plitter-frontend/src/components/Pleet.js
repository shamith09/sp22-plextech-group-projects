import './Pleet.css';
// http://127.0.0.1:5001 backend
// Vuk

const Pleet = props => {
    //will probably delete some of these 
    const pleets = props.pleet;
    //const pleet_id = pleets['pleet_id'];
    const user = pleets["user"];
    //const user_id = user['user_id'];
    const display_name = user['display_name'];
    const username = user['username'];
    const text = pleets['text'];
    const datetime = pleets['datetime'];
    const date_int = new Date(datetime);
    let date_string = date_int.toString();
    date_string.slice(0, -14);

    //headline div should display items in horizontal order on top of the pleet rectangle 
    //pleebox should be the actual rectangle containing the pleet text 
    return (
        <div className = "pleetbox">
            <div className = "headline">
                <h1>{display_name}</h1>
                <a className = "boldtext" href = {"http://localhost:5002/users/" + user.user_id}>{username}</a>
                <p className = "boldtext">{date_string}</p>
            </div>
    
            <div> 
                <p>{text}</p>
            </div>
        </div>
    );


}

export default Pleet;