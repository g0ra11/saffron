import React, { useState } from "react"
import { Form, Col, Row } from "react-bootstrap"
import { requestPaymentToken, redeemPaykey } from "../services/clientApi";
import Button from '@material-ui/core/Button';

type PaymentProps = {
    children: never[];
}
export const TokenForm = (props: PaymentProps) => {
    const [token, setToken] = useState("");
    return (
        <Form>
                    <Form.Group as={Row} controlId="formHorizontalEmail">
                            <Col sm={10}>
                                <Form.Control
                                    type="text"
                                    placeholder="token"
                                    value={token}
                                    onChange={(e) => setToken(e.target.value)}
                                />
                            </Col>
                            <Col sm={2}>
                                <Button type="button"
                                    onClick={()=>redeemPaykey(token)}>Check Token</Button>
                            </Col>
                        </Form.Group>
                </Form>
    )
}