const baseURL = "http://127.0.0.1:8000/";
// todo, random

function getCookie(name) {
  let cookieArr = document.cookie.split(";");

  for (let i = 0; i < cookieArr.length; i++) {
    let cookiePair = cookieArr[i].split("=");

    if (name == cookiePair[0].trim()) {
      return decodeURIComponent(cookiePair[1]);
    }
  }

  // Return null if not found
  return null;
}

const get = (url) => {
  $.ajax({
    type: "GET",
    url: baseURL + url,
    contentType: "application/json",
    error: function () {
      console.log("ERR: Failed to load data from the server");
    },
    success: function (response) {
      console.log(response);
    },
  });
};

const post = (url, data) => {
  console.log(data);
  $.ajax({
    type: "POST",
    url: baseURL + url,
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    data: JSON.stringify(data),
    error: function () {
      console.log("ERR: Failed to load data from the server");
    },
    success: function (response) {
      console.log(data);
    },
  });
};

export { get, post };
