import { Product } from "./product";

export const products: Product[] = [
    {id:"1" , name: "Tableta Samsung Galaxy Tab S6", description:"Octa-Core, 10.5inch, 6GB RAM, 128GB, 4G, Brown", price:3237, img:"https://s12emagst.akamaized.net/products/24652/24651141/images/res_26554286b16caacef0d0c050fa0b9c66_450x450_5ci3.jpg"},
    {id:"2" , name: "Apple iPad Pro (2018)", description:"11inch, 256GB, Wi-Fi, Silver", price:4879, img:"https://s12emagst.akamaized.net/products/18296/18295781/images/res_19541ec1cbdd59024c1b97a0f530fe9e_450x450_f5sv.jpg"},
    {id:"3" , name: "Apple iPad (2019)", description:"10.2inch, 32GB, Cellular, Gold", price:2349, img:"https://s12emagst.akamaized.net/products/25334/25333525/images/res_d58bb96b65a1a066fe631713ca4f5f0b_450x450_ub6j.jpg"},
    {id:"4" , name: "Tableta Huawei MatePad Pro", description:"Octa-Core, 10.8inch, 6GB RAM, 128GB, Wi-Fi, Gray", price:2499, img:"https://s12emagst.akamaized.net/products/29758/29757846/images/res_ed2d4033b49bc4cf1d09a8c51d40c5f5_450x450_knjh.jpg"},
]

export const cartItems: {id: string, name: string, price: number}[] = 
[
    {id:"1" , name: "Tableta Samsung Galaxy Tab S6", price:3237},
    {id:"2" , name: "Apple iPad Pro (2018)", price:4879},
]