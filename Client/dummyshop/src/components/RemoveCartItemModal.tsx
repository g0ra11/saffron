import { Modal, Button, Form } from "react-bootstrap";
import React, { useState } from "react";
import { Product } from "../models/product";

type RemoveCartItemModalProps = {
    show: boolean;
    onClose: () => void;
    onSaveChanges: () => void;
}

export const RemoveCartItemModal = (props: RemoveCartItemModalProps) => {
    return (
        <Modal show={props.show}
            onHide={props.onClose}
            size="sm"
            aria-labelledby="contained-modal-title-vcenter"
            centered>
            <Modal.Header>
                <Modal.Title id="contained-modal-title-vcenter">
                    Remove Item from cart
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                Are you sure you want to remove from cart?
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={props.onClose}>
                    Back
                </Button>
                <Button
                    variant="primary"
                    onClick={() => {props.onSaveChanges(); props.onClose()}}
                >
                    Yes
        </Button>
            </Modal.Footer>
        </Modal>
    )
}