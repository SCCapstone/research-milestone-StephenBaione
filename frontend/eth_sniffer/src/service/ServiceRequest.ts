export class ServiceRequest {
    baseUrl = 'http://127.0.0.1:8000'

    loginUser = function(username: String, password: String) {
        var endpoint = '/auth/login';

        fetch(this.baseUrl + endpoint, {
            method: 'POST',
            body: JSON.stringify({'username': username, 'password': password})
        })
        .then(resp => {
            console.log(resp);
        });
    }

    signupUser = function(username: String, email: String, password: String) {
        var endpoint = "/auth/signup";

        fetch(this.baseUrl + endpoint, {
            method: 'POST',
            body: JSON.stringify({'username': username, 'email': email, 'password': password})
        })
        .then(resp => {
            console.log(resp);
        });
    }

    

    makeRequest = function(endpoint: String) {

    }
}

