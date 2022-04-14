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

    //headline div should display items in horizontal order on top of the pleet rectangle 
    //pleebox should be the actual rectangle containing the pleet text 
    return (
        <div>
            {/*style = "display:flex; flex-direction: row; justify-content: flex-start;" */}
            <div className = "headline">
                <h1> `{display_name}` </h1>
                <img src = "C:\Users\vukpe\Downloads\screenshot-480-_custom-da951372e8aeb5e94c1577fc58ee06c8c4d93698.png" alt="Profile pic"/>
                <p> `{username}` . </p>
                <p> `{datetime}`</p>
            </div>
            {/*style = "width: 200px; height: 200px; border: 1px solid #000;"*/}
            <div className = "pleetbox"> {/* FIXME: move style to Pleet.css */}
                <p>`{text}`</p>
            </div>
        </div>
    );


}

export default Pleet;