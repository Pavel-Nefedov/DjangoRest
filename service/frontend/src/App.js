import React from 'react';
import axios from "axios";
import './App.css';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

import AuthorList from "./components/Author";
import BookList from './components/Book.js'
import AuthorBookList from "./components/AuthorBook";
// import UsersList from "./components/User";
// import FooterList from "./components/Footer";
// import MenuList from "./components/Menu";
import ToDosList from "./components/ToDo";
import ProjectsList from "./components/Project";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';
import ProjectForm from "./components/ProjectForm";
import BookForm from "./components/BookForm";
import user from "./components/User";
import ToDoForm from "./components/ToDoForm";

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена :(</h1>
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)
        // const user1 = {id: 1, username: 'Александр Грин'}
        // const user2 = {id: 2, username: 'Александр Пушкин'}
        // const project1 = {id: 1, name: 'Алые паруса', author: user1}
        // const project2 = {id: 2, name: 'Золотая цепь', author: user1}
        // const project3 = {id: 3, name: 'Пиковая дама', author: user2}
        // const project4 = {id: 4, name: 'Руслан и Людмила', author: user2}
        // const projects = [project1, project2, project3, project4]
        this.state = {
            'books' : [],
            'authors': [],
            'users': [],
            'projects': [],
            'ToDos': [],
        }
    }


    createToDo(title, project) {
        const headers = this.get_headers()
        const data = {title: title, project: project}
        axios.post(`http://127.0.0.1:8000/api/TODO/`, data, {headers})
            .then(response => {
            let new_todos = response.data
            const project = this.state.project.filter((item) => item.id === new_todos.project)[0]
            new_todos.project = project
            this.setState({project: [...this.state.project, new_todos]})
            }).catch(error => console.log(error))
    }


    deleteToDo(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/TODO/${id}`, {headers})
        .then(response => {
                this.setState({project: this.state.project.filter((item)=>item.id !== id)})
        }).catch(error => console.log(error))
    }


    createProject(name, users) {
        const headers = this.get_headers()
        const data = {name: name, users: users}
        axios.post(`http://127.0.0.1:8000/api/projects/`, data, {headers})
            .then(response => {
            let new_project = response.data
            const user = this.state.users.filter((item) => item.id === new_project.user)[0]
            new_project.user = user
            this.setState({projects: [...this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }


    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers})
        .then(response => {
                this.setState({users: this.state.users.filter((item)=>item.id !== id)})
        }).catch(error => console.log(error))
    }



    createBook(name, author) {
        const headers = this.get_headers()
        const data = {name: name, author: author}
        axios.post(`http://127.0.0.1:8000/api/books/`, data, {headers})
            .then(response => {
            let new_book = response.data
            const author = this.state.authors.filter((item) => item.id === new_book.author)[0]
            new_book.author = author
            this.setState({books: [...this.state.books, new_book]})
            }).catch(error => console.log(error))
    }


    deleteBook(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/books/${id}`, {headers})
        .then(response => {
                this.setState({books: this.state.books.filter((item)=>item.id !== id)})
        }).catch(error => console.log(error))
    }


    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout(){
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
    if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                this.setState({authors: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                this.setState({books: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({books: []})
        })

        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                this.setState({projects: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/TODO/', {headers})
            .then(response => {
                this.setState({ToDos: response.data})
            }).catch(error => console.log(error))

    }



    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/ToDos'>ToDos</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                            </li>

                        </ul>
                    </nav>
                    <Switch>

                        <Route exact path='/' component={() => <AuthorList items={this.state.authors} />} />
                        <Route exact path='/projects/create' component={() => <ProjectForm users={this.state.users} createProject={(name, users) => this.createProject(name, users)} />} />
                        <Route exact path='/todos/create' component={() => <ToDoForm project={this.state.project} createToDo={(title, project) => this.createToDo(title, project)} />} />
                        <Route exact path='/books/create' component={() => <BookForm authors={this.state.authors} createBook={(name, author) => this.createBook(name, author)} />} />

                        <Route exact path='/books' component={() => <BookList items={this.state.books} deleteBook={(id)=>this.deleteBook(id)} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects}/>}/>
                        <Route exact path='/ToDos' component={() => <ToDosList ToDos={this.state.ToDos}/>}/>

                        <Route path="/author/:id">

                        {/*<Route exact path='/users' component={() => <UsersList users={this.state.users}/>}/>*/}


                        <AuthorBookList items={this.state.books} />
                        </Route>
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>

        )
    }
}


export default App;
