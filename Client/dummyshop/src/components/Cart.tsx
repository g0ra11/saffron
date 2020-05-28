import React, { useState, useEffect } from "react";
import { cartItems } from "../models/mockData";

function Cart() {
  let totalPrice=0;
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Product Name</th>
          <th>Product Price</th>
        </tr>
      </thead>
      <tbody>
        {cartItems.map((item) => {
          totalPrice=totalPrice+item.price;
          console.log(totalPrice);
          return (
            <tr key={item.id}>
              <td>
               {item.name}
              </td>
              <td>
               {item.price} lei
              </td>
            </tr>
          );
        })}
        <tr key={cartItems[cartItems.length - 1].id + 1}>
              <td>
               TOTAL
              </td>
              <td>
               {totalPrice} lei
              </td>
            </tr>
      </tbody>
    </table>
  )
}

export default Cart;