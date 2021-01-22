import React, { Component} from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";


export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return <div>
            <HomePage />
        </div>;   // rendering HomePage component from HomePage.js
    }
}

// access the index.html's app container to render
const appDiv = document.getElementById("app");
render(<App />, appDiv);