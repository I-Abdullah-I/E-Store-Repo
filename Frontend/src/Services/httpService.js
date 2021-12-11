//TODOS
//add a logging serivce
//add a notification module for handling all kind of errors {toastify}
//Fix env variables issues
/***********************/

import axios from "axios";
import { authHeader } from "../helpers";
// import logger from "./logService";
// import { toast } from "react-toastify";

axios.defaults.baseURL = process.env.REACT_APP_SERVER_URL;
console.log("Header Sent", authHeader());
axios.defaults.headers.common = authHeader();
//
console.log("base Url", process.env.REACT_APP_SERVER_URL);
axios.interceptors.response.use(null, error => {
  const expectedError =
    error.response &&
    error.response.status >= 400 &&
    error.response.status < 500;

  if (!expectedError) {
    console.log(error);
  }

  return Promise.reject(error);
});

export default {
  request: axios.request,
  get: axios.get,
  delete: axios.delete,
  head: axios.head,
  options: axios.options,
  post: axios.post,
  put: axios.put,
  patch: axios.patch
};
