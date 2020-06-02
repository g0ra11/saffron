import React, { useState, useEffect } from "react";
// eslint-disable-next-line
import { Row, Col, Toast, Button, Alert } from "react-bootstrap";
import { axiosClient } from "./../services/axiosClient";

export const ErrorReporter = () => {
  const [showTokenSent, setTokenSent] = useState(false);
  const [showTokenInvalid, setTokenInvalid] = useState(false);
  const [showTokenValid, setTokenValid] = useState(false);
  const [show, setShow] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const interceptor = axiosClient.interceptors.response.use(
      function (response) {
        console.log(response)
        if(response.data.mesage == "paykey generated ok"){
          setTokenSent(true);
          setTimeout(()=>setTokenSent(false), 3000);
        }
        else if(response.data.error == "Invalid token"){
          setTokenInvalid(true);
          setTimeout(()=>setTokenInvalid(false), 3000);
        }
        return response;
      },
      function (error) {
        const message = error.message
          ? error.message
          : "Something went wrong, please try again.";
        setErrorMessage(message);
        setShow(true);
        return Promise.reject(error);
      }
    );

    return () => {
      axiosClient.interceptors.response.eject(interceptor);
    };
  }, []);

  return (
  <>
    <Row style={{ position: "absolute", right: "20px", bottom: "20px" }}>
      <Col xs={12}>
        <Toast onClose={() => setShow(false)} show={show}>
          <Toast.Header>
            <strong className="mr-auto">Error</strong>
          </Toast.Header>
          <Toast.Body>
            <Alert variant="danger"> {errorMessage} </Alert>
          </Toast.Body>
        </Toast>
      </Col>
    </Row>
    <Row style={{ position: "absolute", right: "20px", bottom: "20px", zIndex:999999 }}>
    <Col xs={12}>
      <Toast onClose={() => setTokenSent(false)} show={showTokenSent}>
        <Toast.Header>
          <strong className="mr-auto">One step closer..</strong>
        </Toast.Header>
        <Toast.Body>
          <Alert variant="success">Token sent! Check Saffron Banking app.</Alert>
        </Toast.Body>
      </Toast>
    </Col>
  </Row>
  <Row style={{ position: "absolute", right: "20px", bottom: "20px", zIndex:999999 }}>
    <Col xs={12}>
      <Toast onClose={() => setTokenInvalid(false)} show={showTokenInvalid}>
        <Toast.Header>
          <strong className="mr-auto">Oops..</strong>
        </Toast.Header>
        <Toast.Body>
          <Alert variant="danger">Invalid Token. Try again!</Alert>
        </Toast.Body>
      </Toast>
    </Col>
  </Row>
  <Row style={{ position: "absolute", right: "20px", bottom: "20px", zIndex:999999 }}>
    <Col xs={12}>
      <Toast onClose={() => setTokenValid(false)} show={showTokenValid}>
        <Toast.Header>
          <strong className="mr-auto">Great!</strong>
        </Toast.Header>
        <Toast.Body>
          <Alert variant="success">That's all here. Your payment will be processed soon.</Alert>
        </Toast.Body>
      </Toast>
    </Col>
  </Row>
  </>
  );
};
