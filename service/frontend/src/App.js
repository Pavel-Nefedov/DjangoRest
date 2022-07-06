import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import {HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

import AuthorList from "./components/Author";
import BookList from './components/Book.js'
import UsersList from "./components/User";
import FooterList from "./components/Footer";
import MenuList from "./components/Menu";
import AuthorBookList from "./components/AuthorBook";
import ToDosList from "./components/ToDo";
import ProjectsList from "./components/Project";

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

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/menus/')
            .then(response => {
                const menus = response.data
                    this.setState(
               {
                        'menus': menus
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                    this.setState(
               {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                    this.setState(
               {
                        'users': users
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/footers/')
            .then(response => {
                const footers = response.data
                    this.setState(
               {
                        'footers': footers
                    }
                )
            }).catch(error => console.log(error));


    }

    render() {
        return (
            <div>
                <HashRouter>
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
                        </ul>
                    </nav>
                    <Switch>

                        <Route exact path='/' component={() => <AuthorList items={this.state.authors} />} />
                        <Route exact path='/books' component={() => <BookList items={this.state.books} />} />

                        <Route exact path='/users' component={() => <UsersList users={this.state.users}/>}/>
                        <Route exact path='/ToDos' component={() => <ToDosList ToDos={this.state.ToDos}/>}/>
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects}/>}/>


                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </HashRouter>
            </div>

            // <div>
            //     Меню
            //     <MenuList menus={this.state.menus} />
            //     <br/>
            //     Список авторов
            //     <AuthorList authors={this.state.authors} />
            //     <br/>
            //     Список пользователей
            //     <UsersList users={this.state.users} />
            //     <br/>
            //     Подвавл
            //     <FooterList footers={this.state.footers} />
            // </div>
        )
    }
}


export default App;
