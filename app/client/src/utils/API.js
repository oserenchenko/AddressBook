import axios from "axios";

export default {
  // Gets all addresses
  getAddresses: function() {
    return axios.get("/addresses/all");
  },

  postAddress: function(addressData) {
    return axios.post("/addresses/add", addressData);
  },

  deleteAddress: function(id) {
    return axios.delete("/addresses/delete/" + id);
  }
}