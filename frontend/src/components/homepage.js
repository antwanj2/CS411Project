import React, {Component} from "react";
import {render} from "react-dom";

export default class Homepage extends Component {
    constructor(props){    
        super(props);
    }
    render(){
        return 
        <h1> 
            Hi! 
            Welcome to Play the Weather, an app that can generate a playlist based on the weather at your location. 
            Simply log in with your Spotify account, let us know where you are, and we will take care of the rest! 
        </h1>
        
    };
}

const appDiv = document.getElementById("homepage");
render(<Homepage />, appDiv)