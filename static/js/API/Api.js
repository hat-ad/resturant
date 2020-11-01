import API from "./service.js";

export const baseUrl = "127.0.0.1:8000/";

const Api = new API({
  baseUrl: baseUrl,
});

export default Api;
