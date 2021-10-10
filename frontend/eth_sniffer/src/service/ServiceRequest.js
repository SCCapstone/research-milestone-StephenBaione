export class ServiceRequest {
    baseUrl = 'http://127.0.0.1:8000'

    constructor() {}

    loginUser = function(username, password) {
        var endpoint = '/auth/login';

        fetch(this.baseUrl + endpoint, {
            method: 'POST',
            body: JSON.stringify({'username': username, 'password': password})
        })
        .then(resp => {
            console.log(resp);
        });
    }

    signupUser = function(username, email, password) {
        var endpoint = "/auth/signup";

        fetch(this.baseUrl + endpoint, {
            method: 'POST',
            body: JSON.stringify({'username': username, 'email': email, 'password': password})
        })
        .then(resp => {
            console.log(resp);
        });
    }

    async getNFT(contractAddress, tokenId) {
        var endpoint = this.baseUrl + "/opensea/nft?contract_address=" + contractAddress + '&token_id=' + tokenId;

        return fetch(endpoint)
        .then(response => response.json())
        .then(data => data);
    }



    makeRequest = function(endpoint) {

    }
}

