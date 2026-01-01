import axios from "axios";

export const api = axios.create({
  baseURL: "http://3.110.119.7:8000",
});
