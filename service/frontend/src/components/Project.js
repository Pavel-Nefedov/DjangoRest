import React from 'react'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>id</th>
            <th>Название</th>
            <th>Владелец</th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectsList