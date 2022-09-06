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
// import ToDosList from "./components/ToDo";
// import ProjectsList from "./components/Project";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';

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
        const author1 = {id: 1, last_name: 'Александр', first_name: 'Грин', birthday_year: 1880}
        const author2 = {id: 2, last_name: 'Александр', first_name: 'Пушкин', birthday_year: 1799}
        const authors = [author1, author2]
        const book1 = {id: 1, name: 'Алые паруса', author: author1}
        const book2 = {id: 2, name: 'Золотая цепь', author: author1}
        const book3 = {id: 3, name: 'Пиковая дама', author: author2}
        const book4 = {id: 4, name: 'Руслан и Людмила', author: author2}
        const books = [book1, book2, book3, book4]
        this.state = {
            'books' : books,
            'authors': authors,
            'users': [],
            'projects': [],
            'ToDos': [],
        }
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
                        <Route exact path='/books' component={() => <BookList items={this.state.books} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route path="/author/:id">

                        {/*<Route exact path='/users' component={() => <UsersList users={this.state.users}/>}/>*/}
                        {/*<Route exact path='/ToDos' component={() => <ToDosList ToDos={this.state.ToDos}/>}/>*/}
                        {/*<Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects}/>}/>*/}
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
