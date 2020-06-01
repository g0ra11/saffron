import { Modal } from "react-bootstrap";
import React, { useState } from "react";
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepLabel from '@material-ui/core/StepLabel';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { PaymentForm } from "./EmailForm";
import { TokenForm } from "./TokenForm";

type SubmitModalProps = {
    amount: number;
    show: boolean;
    onClose: () => void;
}

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            width: '100%',
        },
        backButton: {
            marginRight: theme.spacing(1),
        },
        instructions: {
            marginTop: theme.spacing(1),
            marginBottom: theme.spacing(1),
        },
    }),
);

function getSteps() {
    return ['E-mail', 'Saffron payment token', 'Finish'];
}

function getStepContent(stepIndex: number, amount: number) {

    switch (stepIndex) {
        case 0:
            return (
                <PaymentForm
                    amount={amount}>
                </PaymentForm>
            )
        case 1:
            return (
                <TokenForm>
                </TokenForm>
            )
        case 2:
            return 'Finish';
        default:
            return 'Unknown stepIndex';
    }
}

type StepperProps = {
    children: never[];
    amount: number
}

function HorizontalLabelPositionBelowStepper(props: StepperProps) {
    console.log(props.amount);
    const classes = useStyles();
    const [activeStep, setActiveStep] = React.useState(0);
    const steps = getSteps();

    const handleNext = () => {
        setActiveStep((prevActiveStep) => prevActiveStep + 1);
    };

    const handleBack = () => {
        setActiveStep((prevActiveStep) => prevActiveStep - 1);
    };

    const handleReset = () => {
        setActiveStep(0);
    };

    return (
        <div className={classes.root}>
            <Stepper activeStep={activeStep} alternativeLabel>
                {steps.map((label) => (
                    <Step key={label}>
                        <StepLabel>{label}</StepLabel>
                    </Step>
                ))}
            </Stepper>
            <div>
                {activeStep === steps.length ? (
                    <div>
                        <Typography className={classes.instructions}>All steps completed</Typography>
                        <Button onClick={handleReset}>Reset</Button>
                    </div>
                ) : (
                        <div>
                            <Typography className={classes.instructions}>{getStepContent(activeStep, props.amount)}</Typography>
                            <div>
                                <Button
                                    disabled={activeStep === 0}
                                    onClick={handleBack}
                                    className={classes.backButton}
                                >
                                    Back
                                </Button>
                                <Button variant="contained" color="primary" onClick={handleNext}>
                                    {activeStep === steps.length - 1 ? 'Finish' : 'Next'}
                                </Button>
                            </div>
                        </div>
                    )}
            </div>
        </div>
    );
}

export const SubmitOrderModal = (props: SubmitModalProps) => {
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
                <HorizontalLabelPositionBelowStepper
                    amount={props.amount}
                >
                </HorizontalLabelPositionBelowStepper>
            </Modal.Body>
        </Modal>
    )
}