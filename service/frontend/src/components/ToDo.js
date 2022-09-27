import React from 'react'
import {Link} from "react-router-dom";


const ToDoItem = ({item, deleteToDo}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.title}</td>
            <td>{item.project}</td>
            <td><button onClick={()=>deleteToDo(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const ToDosList = ({items, deleteToDo}) => {
    return (
        <div>
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>PROJECT</th>
                <th></th>
            </tr>
            {items.map((item) => <ToDoItem item={item} deleteToDo={deleteToDo}/>)}
        </table>
        <Link to='/todos/create'>Create</Link>
        </div>
    )
}

export default ToDosList