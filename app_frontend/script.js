
const loginPage = document.getElementById('login-page');
const registerPage = document.getElementById('register-page');
const homePage = document.getElementById('home-page');
const welcomeMessage = document.getElementById('welcome-message');

const registerLink = document.getElementById('show-register');
const loginLink = document.getElementById('show-login');
const loginBtn = document.getElementById('login-btn');
const signupBtn = document.getElementById('signup-btn');

const loginUsername = document.getElementById('login-username');
const loginPassword = document.getElementById('login-password');
const registerUsername = document.getElementById('register-username');
const registerEmail = document.getElementById('register-email');
const registerPassword = document.getElementById('register-password');

registerLink.onclick = () => {
    loginPage.style.display = 'none';
    registerPage.style.display = 'block';
    homePage.style.display = 'none';
};


loginLink.onclick = () => {
    loginPage.style.display = 'block';
    registerPage.style.display = 'none';
    homePage.style.display = 'none';
};

signupBtn.onclick = () => {
    const username = registerUsername.value;
    const email = registerEmail.value;
    const password = registerPassword.value;

    if (username && email && password) {
        const user = { username, email, password };
        localStorage.setItem(username, JSON.stringify(user));

        alert('Registration successful! You can now log in.');
        registerUsername.value = '';
        registerEmail.value = '';
        registerPassword.value = '';
        loginPage.style.display = 'block';
        registerPage.style.display = 'none';
    } else {
        alert('Please fill in all fields.');
    }
};

loginBtn.onclick = () => {
    const username = loginUsername.value;
    const password = loginPassword.value;

    const storedUser = localStorage.getItem(username);

    if (storedUser) {
        const user = JSON.parse(storedUser);

        if (user.password === password) {
            loginPage.style.display = 'none';
            homePage.style.display = 'block';
            welcomeMessage.textContent = `Welcome, ${user.username}!`;

            loginUsername.value = '';
            loginPassword.value = '';
        } else {
            alert('Incorrect password.');
        }
    } else {
        alert('No user found with that username.');
    }
};

const weatherData = [
    { day: 'Monday', temp: '25°C', condition: 'Sunny' },
    { day: 'Tuesday', temp: '22°C', condition: 'Cloudy' },
    { day: 'Wednesday', temp: '18°C', condition: 'Rainy' },
    { day: 'Thursday', temp: '20°C', condition: 'Partly Cloudy' },
    { day: 'Friday', temp: '24°C', condition: 'Sunny' },
    { day: 'Saturday', temp: '26°C', condition: 'Sunny' },
    { day: 'Sunday', temp: '23°C', condition: 'Windy' }
];


let soilMoisture = Math.floor(Math.random() * 1000);
const weatherForecastContainer = document.getElementById('weather-forecast');
const soilMoistureLevel = document.getElementById('soil-moisture-level');
const checkMoistureBtn = document.getElementById('check-moisture-btn');
const modal = document.getElementById('moisture-modal');
const modalMessage = document.getElementById('modal-message');
const closeBtn = document.querySelector('.close-btn');
function populateWeatherForecast() {
    weatherData.forEach((dayData) => {
        const dayDiv = document.createElement('div');
        dayDiv.classList.add('day');

        dayDiv.innerHTML = `
            <h3>${dayData.day}</h3>
            <p>${dayData.temp}</p>
            <p>${dayData.condition}</p>
        `;

        weatherForecastContainer.appendChild(dayDiv);
    });
}
function displaySoilMoisture() {
    soilMoistureLevel.textContent = soilMoisture;
}
function checkSoilCondition() {
    if (soilMoisture < 100) {
        modalMessage.textContent = "Soil is too dry. Add water.";
    } else if (soilMoisture > 700) {
        modalMessage.textContent = "Soil is too wet. Don't add water.";
    } else {
        modalMessage.textContent = "Soil moisture is optimal.";
    }
    modal.style.display = "block";
}
closeBtn.onclick = function() {
    modal.style.display = "none";
};
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
checkMoistureBtn.onclick = checkSoilCondition;
populateWeatherForecast();
displaySoilMoisture();
