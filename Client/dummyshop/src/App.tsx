import "bootstrap/dist/css/bootstrap.min.css";
import React from 'react';
import './App.css';
import { Route, Switch } from "react-router-dom";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import { ErrorReporter } from "./components/ErrorReporter";
import NotFoundPage from "./components/NotFoundPage";
import Cart from "./components/Cart";
import ProductsList from "./components/ProductsList";

function App() {
  return (
    <div className="container-fluid">
      <Header />
      <Navbar />
      <Switch>
        <Route path="/" exact component={ProductsList}/>
        <Route path="/cart" component={Cart} />
        <Route component={NotFoundPage} />
      </Switch>
      <ErrorReporter></ErrorReporter>
    </div>
  );
}

export default App;
