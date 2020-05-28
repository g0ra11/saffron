import React, { useState } from "react";
import { Product } from "../models/product";
import { cartItems } from "../models/mockData";
import { Row, Toast, Col, Alert } from "react-bootstrap";

type ProductProps = {
    product: Product;
}

export function ProductCard(props: ProductProps) {
    const [show, setShow] = useState(false);

    const addToCart = (product: Product) => {
        cartItems.push(product)
        setShow(true);
    }

    

    return (
        <>
            <div className="col-md-4 d-flex">
                <div className="card text-center m-2">
                    <img
                        className="card-img-top"
                        src={props.product.img}
                        alt="Card image cap"
                    />
                    <div className="card-body">
                        <h5 className="card-title">{props.product.name}</h5>
                        <p className="card-text">
                            {props.product.description}
                        </p>
                    </div>
                    <div className="card-footer">
                        <div className="col-md-12">
                            <div className="d-flex">
                                <div className="p-2">
                                    <div className="input-group input-group-sm">
                                        <div className="input-group-append">
                                            <button
                                                className="btn btn-outline-secondary"
                                                type="button"
                                                onClick={() => addToCart(props.product)}
                                            >
                                                Add
                          </button>
                                        </div>
                                    </div>
                                </div>
                                <div className="p-2">
                                    <span className="badge badge-danger">{props.product.price} lei</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <Row style={{ position: "fixed", right: "10px", bottom: "10px", zIndex:1}}>
                <Col xs={12}>
                    <Toast onClose={() => setShow(false)} show={show}>
                        <Toast.Header>
                            <strong className="mr-auto">Great!</strong>
                        </Toast.Header>
                        <Toast.Body>
                            <Alert variant="primary"> {props.product.name} added to cart </Alert>
                        </Toast.Body>
                    </Toast>
                </Col>
                {/* // eslint-disable-next-line */}
                {/* <Col xs={6}> */}
                {/* <Button onClick={() => setShow(true)}>Show Toast</Button> */}
                {/* </Col> */}
            </Row>
        </>
    )
}

export default ProductCard;