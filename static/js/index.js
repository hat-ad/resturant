import API from "./API/Api.js";
$(document).on("click", ".btn-group button", function () {
  $(this).addClass("active").siblings().removeClass("active");
});

$(".feat-btn").click(function () {
  $(".brakefast-show").toggleClass("show");
});
$(".feat-btn2").click(function () {
  $(".meal-show").toggleClass("show1");
});
$(".feat-btn3").click(function () {
  $(".snack-show").toggleClass("show2");
});
$(".feat-btn4").click(function () {
  $(".dinner-show").toggleClass("show3");
});

const getUser = () => {
  let userDetails = document.getElementsByClassName("form-control");
  let details = {
    email: userDetails[0].value,
    phone: userDetails[1].value,
    username: userDetails[2].value,
    table_no: userDetails[3].value,
    no_of_customer: userDetails[4].value,
    waiter: userDetails[5].value,
  };
  // console.log(details);
  // post('',details)
};

// ADD to cart
let item = [];
const getItem = (e) => {
  let card = e.target.parentNode;
  // console.log(card.parentNode.getElementsByTagName("img")[0].src);
  let item_name_price = card
    .getElementsByClassName("title")[0]
    .innerText.split("\n");
  let name = item_name_price[0];
  let price = item_name_price[1];
  let item_img = card.parentNode.getElementsByTagName("img")[0].src;
  addCartItem(name, price, item_img);
};

const updateTotal = () => {
  let total = 0.0;
  let cart_list = document.getElementById("cart");
  $("#total").empty();

  for (let i = 1; i < cart_list.childElementCount; i++) {
    let name =
      cart_list.children[i].children[0].children[0].children[1].children[0]
        .innerText;
    let qty = cart_list.children[i].children[1].children[0].value;
    let price = cart_list.children[i].children[2].innerText.split("$")[0];
    let item_price = 0.0;
    qty = parseFloat(qty);
    price = parseFloat(price);
    item_price = item_price + qty * price;
    total = total + item_price;
    addTotalItem(name, qty, item_price);
    item.push({
      itemName: name,
      itemQuantity: qty,
      itemPrice: price,
    });
  }
  document.getElementsByTagName("strong")[0].innerText = "₹" + total;
};

const addCartItem = (name, price, item_img) => {
  $(document).ready(function () {
    $("tbody").append(`<tr class="item-main-list">
      <td class="items">
        <div class="cart-info">
          <img src=${item_img}>
          <div class="p">
            <p>${name}</p>
          </div>
        </div>
      </td>
      <td><input type="number" value="1" min="1" max="99"></td>
      <td class="price">${price}</td>
      <td>
        <button class="btn btn-danger btn-sm pl-2 text-center"><span><i class="fa fa-trash-o pr-2"></i></span></button>
      </td>
    </tr>`);
  });

  $(document).on("click", ".btn-danger", function (e) {
    var r = $(this).closest("tr").remove();
  });
};

const addTotalItem = (name, qty, price) => {
  let list = `<li class="list-group-item d-flex justify-content-between lh-condensed">
  <div>
    <h6 class="my-0">${name}</h6>
    <small class="text-muted">Quantity: ${qty}</small>
  </div>
  <span class="text-muted">₹${price}</span>
</li>`;

  $("#total").prepend(list);
};

const getMenu = async (type) => {
  let menu_type = ["breakfast", "meal", "snacks", "dinner"];
  let menu_list_body = document.getElementsByClassName("menu-list");
  $(menu_list_body).empty();
  for (let j = 0; j < menu_list_body.length; j++) {
    let response = await API.get(type + menu_type[j] + "/?format=json");
    for (let i = 0; i < response.length; i++) {
      addCard(
        menu_list_body[j],
        response[i].image,
        response[i].name,
        response[i].price
      );
    }
  }

  let add = document.getElementsByClassName("btn-success");
  for (let i = 0; i < add.length - 1; i++) {
    add[i].addEventListener("click", (e) => getItem(e));
  }
  add[add.length - 1].addEventListener("click", () => {
    console.log(item);
    // post("billing", item);
  });
};

const addCard = (body, img, title, price) => {
  let card_HTML = `<div class="card1">
  <img src=${img} class="card-img-top">
  <div class="card-body">
    <h5 class="title">${title}<span>${price}$</span></h5>
    <button class="btn btn-success">Add</button>
  </div>
</div>`;

  $(body).append(card_HTML);
};

// Button click Events
getMenu("veg_");
let menu_buttons = document.getElementsByClassName("btn-outline-info");
menu_buttons[0].addEventListener("click", () => getMenu("veg_"));
menu_buttons[1].addEventListener("click", () => getMenu("non_veg_"));

let saveUser = document
  .getElementsByClassName("btn-save")[0]
  .addEventListener("click", getUser);
let cardTotal = document

  .getElementById("cartTotal")
  .addEventListener("click", updateTotal);

API.post("test", { data: "data" });
