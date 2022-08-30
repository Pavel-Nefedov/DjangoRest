import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.firstname}</td>
            <td>{user.lastname}</td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>Username</th>
            <th>First name</th>
            <th>Last Name</th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UsersList