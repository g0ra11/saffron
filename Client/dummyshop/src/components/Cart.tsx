import React, { useState, useEffect } from "react";
import { cartItems } from "../models/mockData";
import { Button } from "react-bootstrap";
import { RemoveCartItemModal } from "./RemoveCartItemModal";
import { Product } from "../models/product";
import { Link } from "react-router-dom";
import { requestPaymentToken, redeemPaykey } from "../services/clientApi";
import { SubmitOrderModal } from "./SubmitOrderModal";

function Cart() {
  let totalPrice = 0;
  let selectedProduct: Product;

  const [submitModalShow, setSubmitModalShow] = useState(false);
  const [removeModalShow, setRemoveModalShow] = useState(false);

  const removeFromCart = () => {
    let index = cartItems.indexOf(selectedProduct);
    cartItems.splice(index, 1);
    setSubmitModalShow(false);
  };

  return (
    <>
      {(cartItems.length > 0) && <table className="table">
        <thead>
          <tr>
            <th>Product Name</th>
            <th> Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {cartItems.map((item) => {
            totalPrice = totalPrice + item.price;
            return (
              <tr key={item.id}>
                <td>
                  {item.name}
                </td>
                <td>
                  {item.price} lei
              </td>
                <td>
                  <Button variant="danger" onClick={() => { setRemoveModalShow(true); selectedProduct = item; }}>Delete</Button>
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
            <td>
              <Button variant="success" onClick={() => setSubmitModalShow(true)}>Submit</Button>
            </td>
          </tr>

        </tbody>
      </table>}
      {
        (cartItems.length == 0) &&
        <div>
          <h2>Your cart is empty.</h2>
          <p>
            <Link to="/">Let's buy something!</Link>
          </p>
        </div>
      }
      <RemoveCartItemModal
        show={removeModalShow}
        onClose={() => setRemoveModalShow(false)}
        onSaveChanges={removeFromCart}
      ></RemoveCartItemModal>
      <SubmitOrderModal
        amount={totalPrice}
        show={submitModalShow}
        onClose={() => setSubmitModalShow(false)}
      ></SubmitOrderModal>
    </>
  )
}

export default Cart;