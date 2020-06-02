import React, { useState } from "react"
import { Form, Col, Row } from "react-bootstrap"
import { requestPaymentToken } from "../services/clientApi";
import Button from '@material-ui/core/Button';
import { render } from "@testing-library/react";

type PaymentProps = {
    children: never[];
    amount: number;
}

export const PaymentForm = (props: PaymentProps) => {
    const [email, setEmail] = useState("");
    return (
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
                                    onClick={()=>requestPaymentToken(email, props.amount + '')}>Request Token</Button>
                            </Col>
                        </Form.Group>
                </Form>
    )
}