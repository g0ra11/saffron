import React from "react";
import { NavLink } from "react-router-dom";

function Navbar() {
    const activeStyle = { color: "black" };
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <NavLink className="navbar-brand" activeStyle={activeStyle} exact to="/"
            ><img
                    src="https://cdn1.iconfinder.com/data/icons/shopping-and-ecommerce-2/64/E-commerce_and_Shopping-98-512.png"
                    width="40"
                    height="40"
                    className="d-inline-block align-top"
                /></NavLink>
            <div className="collapse navbar-collapse" id="navbarText">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item">
                        <NavLink className="nav-link" activeStyle={activeStyle} exact to="/"> Products </NavLink>
                    </li>

                </ul>
                <ul className="nav navbar-nav navbar-right">
                    <li className="nav-item">
                        <NavLink className="nav-link" activeStyle={activeStyle} to="/cart">Cart</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" activeStyle={activeStyle} to="/login">Login</NavLink>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Navbar;