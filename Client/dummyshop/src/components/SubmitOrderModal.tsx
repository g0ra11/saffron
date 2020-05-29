import { Modal, Button, Form, Row, Col } from "react-bootstrap";
import React, { useState } from "react";
import { Product } from "../models/product";
import { requestPaymentToken, redeemPaykey } from "../services/clientApi";

type SubmitModalProps = {
    amount: number;
    show: boolean;
    onClose: () => void;

}

export const SubmitOrderModal = (props: SubmitModalProps) => {
    const [email, setEmail] = useState("");
  const [token, setToken] = useState("");
    return (
        <Modal show={props.show}
            onHide={props.onClose}
            size="lg"
            aria-labelledby="contained-modal-title-vcenter"
            centered>
            <Modal.Header>
                <Modal.Title id="contained-modal-title-vcenter">
                    Submit Order
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group as={Row} controlId="formHorizontalEmail">
                        <Col sm={10}>
                        <Form.Control
                            type="email"
                            placeholder="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        </Col>
                        <Col sm={2}>
                        <Button type="button"
                        onClick={ () => requestPaymentToken(email, props.amount + '') }>Request Token</Button>
                        </Col>
                    </Form.Group>
                    <Form.Group as={Row} controlId="formHorizontalToken">
                        <Col sm={10}>
                        <Form.Control
                            type="text"
                            placeholder="token"
                            value={token}
                            onChange={(e) => setToken(e.target.value)}
                        />
                        </Col>
                        <Button type="button" onClick={ () => redeemPaykey(token) }>Check Token</Button>
                    </Form.Group>
                </Form>
            </Modal.Body>
        </Modal>
    )
}