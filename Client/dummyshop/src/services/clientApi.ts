import { axiosClient } from "./axiosClient";
import { handleError } from "./apiUtils";

export const requestPaymentToken = async (email: string, amount: string) => {
    try {
        return axiosClient.get("request_money_token?email=" + email + "&amount=" + amount + "&user=adaj@yahoo.com");
    }
    catch (handleError) {
        return handleError(handleError);
    }
}

export const redeemPaykey = async (paykey: string) => {
    try {
        return axiosClient.get("redeem_paykey?paykey="+paykey);
    }
    catch (handleError) {
        return handleError(handleError);
    }
}