import './UserProfile.css';
import { useParams } from 'react-router-dom';

const UserProfile = props => {
    let { id } = useParams(); // this is the user id, use this to fetch from backend

    return (
        <p>Here is the user_id: {id}</p>
    )
}

export default UserProfile;