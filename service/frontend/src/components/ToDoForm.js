import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {title: '', project: props.project[0]?.id}
    }

    handleChange(event) {
        this.setState(
            {
            [event.target.title]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.title, this.state.project)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="title">title</label>
                    <input type="text" className="form-control" name="title"
                           value={this.state.title}
                           onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="project">project</label>
                    <input type="number" className="form-control" name="project"
                           value={this.state.project}
                           onChange={(event)=>this.handleChange(event)} />
                </div>
                <input type="submit" className="btn-primary" value="Save" />
            </form>
        );
    }
}

export default ToDoForm
