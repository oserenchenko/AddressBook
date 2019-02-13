import React, { Component } from 'react';
import './App.css';
import API from "./utils/API";
import Form from "./components/form";

class App extends Component {
  state = {
    addresses: {}
  }

  componentDidMount() {
    this.fetchAddresses();
  };

  fetchAddresses = () => {
    API.getAddresses() 
    .then(res => console.log(res))
    .catch(err => console.log(err))
  };

  render() {
    return (
      <div className="container">
        <h1 className="title text-center">Address Book</h1>
        <Form></Form>
      </div>
    );
  }
}

export default App;
