import React from 'react'
import {Link} from "react-router-dom";


const ProjectItem = ({item, deleteProject}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.users}</td>
            <td><button onClick={()=>deleteProject(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const ProjectsList = ({items, deleteProject}) => {
    return (
        <div>
            <table>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>Owner</th>
                    <th></th>
                </tr>
                {items.map((item) => <ProjectItem item={item} deleteProject={deleteProject}/>)}
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectsList