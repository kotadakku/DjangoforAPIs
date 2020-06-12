import React, { Component } from 'react';
import axios from 'axios';
import React, {Component} from 'react'

//const list = [
//    {
//        "id": 1,
//        "title": "Hello Wold",
//        "body": "Hello Every Body"
//    },
//    {
//        "id": 2,
//        "title": "Second",
//        "body": "Hello Acs"
//    }
//]
class App extends Component {
    state = {
        todos: []
    };
// new
    componentDidMount(){
        this.getTodos();
    }
// new
    getTodos() {
    axios
        .get('http://127.0.0.1:8000/api/')
        .then(res => {
        this.setState({ todos: res.data });
    })
    .catch(err => {
        console.log(err);
    });
}

    render(){
        return(
            <div>
                {this.state.todos.map(item => (
                    <div key={item.id}>
                        <h1>{item.title}</h1>
                        <p>{item.body}</p>
                </div>
                ))}
            </div>
            );
    }
}
export default App;