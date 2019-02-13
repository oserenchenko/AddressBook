import React, { Component } from 'react';
import './App.css';
import API from "./utils/API";
import Form from "./components/form";

class App extends Component {
  state = {
    addresses: []
  }

  componentDidMount() {
    this.fetchAddresses();
  };

  fetchAddresses = () => {
    API.getAddresses() 
    .then(res => this.setState({
      addresses: res.data
    }))
    .catch(err => console.log(err))
  };

  deleteAddress = (event) => {
    console.log(event.target.id)
    API.deleteAddress(event.target.id)
    .then(res => console.log("deleted address"))
    .catch(err => console.log(err))
  };

  render() {
    console.log(this.state.addresses)
    return (
      <div className="container">
        <h1 className="title text-center">Address Book</h1>
        <table className="table table-bordered mt-3">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Address</th>
              <th scope="col">City</th>
              <th scope="col">State</th>
              <th scope="col">Zip Code</th>
              <th scope="col">Delete</th>
            </tr>
          </thead>
          <tbody>
            {this.state.addresses.map(address =>
                <tr id={address.id}>
                  <td>{address.name}</td>
                  <td>{address.address}</td>
                  <td>{address.city}</td>
                  <td>{address.state}</td>
                  <td>{address.zipcode}</td>
                  <td><button type="button" className="btn btn-sm btn-danger" onClick={this.deleteAddress}id={address.id}>X</button></td>
              </tr>
              )}
          </tbody>
        </table>

        <Form></Form>
      </div>
    );
  }
}

export default App;
