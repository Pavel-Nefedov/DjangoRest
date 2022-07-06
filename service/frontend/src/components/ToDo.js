import React from 'react'


const ToDoItem = ({ToDo}) => {
    return (
        <tr>
            <td>{ToDo.id}</td>
            <td>{ToDo.title}</td>
            <td>{ToDo.project}</td>
        </tr>
    )
}

const ToDosList = ({ToDos}) => {
    return (
        <table>
            <th>ID</th>
            <th>Название</th>
            <th>Проект</th>
            {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo}/>)}
        </table>
    )
}

export default ToDosList