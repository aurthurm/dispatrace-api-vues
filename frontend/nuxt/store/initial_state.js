export function initialState() {
    return{
        auth: {
            token: null,
            refresh: null,
            user: {
                username: '',
                user_id: ''
            },
            loggedIn: false
        },
        timeLeft: { hours: 0, minutes: 0 },
        accounts: [],    
        options: {                
            countries: {
                options: [
                    { value: null, text: "Select a Country" }
                ]
            },                 
            cities: {
                options: [
                    { value: null, text: "Select a City" }
                ]
            },                
            departments: {
                options: [
                    { value: null, text: "Select a Department" },
                ]
            },                
            offices: {
                options: [
                    { value: null, text: "Select an Office" },
                ]
            },               
            categories: {
                options: [
                    { value: null, text: "Select a Category" },
                ]
            },               
            levels: {
                options: [
                    { value: null, text: "Select a Level" },
                ]
            }
        }
    }
}
