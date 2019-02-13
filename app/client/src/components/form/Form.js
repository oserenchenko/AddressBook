import React, { Component } from 'react';
import API from "../../utils/API";

class Form extends Component {
  state = {
    name: "",
    address: "",
    city: "",
    state: "",
    zipcode: ""
  }

  addAddress = () => {
    API.postAddress({
      name: this.state.name,
      address: this.state.address,
      city: this.state.city,
      state: this.state.state,
      zipcode: this.state.zipcode
    }) 
    .then(res => this.props.fetchAddresses())
    .catch(err => console.log(err))
  };

  handleInputChange = event => {
    const {
        name,
        value
    } = event.target;
    this.setState({
        [name]: value
    });
  };

  onSubmitClick = (e) => {
    e.preventDefault();
    this.addAddress();
  };

  render() {
    return(
      <form>
        <div className="form-group">
          <label>Name</label>
          <textarea className="form-control" name="name" rows="1" onChange={this.handleInputChange}></textarea>
        </div>
        <div className="form-group">
          <label>Address</label>
          <textarea className="form-control" name="address" rows="1" onChange={this.handleInputChange}></textarea>
        </div>
        <div className="form-group">
          <label>City</label>
          <textarea className="form-control" name="city" rows="1" onChange={this.handleInputChange}></textarea>
        </div>
        <div className="form-group">
          <label>State</label>
          <textarea className="form-control" name="state" rows="1" onChange={this.handleInputChange}></textarea>
        </div>
        <div className="form-group">
          <label>Zipcode</label>
          <textarea className="form-control" name="zipcode" rows="1" onChange={this.handleInputChange}></textarea>
        </div>
        <button type="submit" className="btn btn-primary" onClick={this.onSubmitClick}>Submit</button>
      </form>
    )}
}

export default Form;