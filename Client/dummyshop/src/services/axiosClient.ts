import axios from "axios";

export const axiosClient = axios.create(
    {
        baseURL: "https://soffranbanking.azurewebsites.net/?fbclid=IwAR0WBKS-nn8qZBHKR4xPyZca7hWWFTL3LDuZ_AEDpITZJojSzEcrbwxOBos"
    }
);