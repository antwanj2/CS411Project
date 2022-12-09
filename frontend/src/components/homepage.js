import React, {Component} from "react";
import {render} from "react-dom";

export default class Homepage extends Component {
    constructor(props){    
        super(props);
    }
    render(){
        return <h1> <body>WORKKKK</body> </h1>;
        
    }
}

const appDiv = document.getElementById("homepage");
render(<Homepage />, appDiv)