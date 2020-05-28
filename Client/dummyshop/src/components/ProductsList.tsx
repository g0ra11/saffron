import React from "react";
import ProductCard from "./ProductCard";
import { Product } from "../models/product";
import { products } from "../models/mockData";

export function ProductsList() {
    return (
        <>
            <div className="container mt-4 mb-4">
                <div className="row">
                   {
                       products.map((product)=>
                       {
                           return (
                               <ProductCard key={product.id} product={product}/>
                           );
                       }
                       )
                   } 
                </div>
            </div>
        </>
    );
}

export default ProductsList;