import axios from "axios";

export default {
  // Gets all addresses
  getAddresses: function() {
    return axios.get("/addresses/all");
  },
}