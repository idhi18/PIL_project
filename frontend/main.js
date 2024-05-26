var welcomeTranslations = [
    "Namaste!",
    "Welcome",
    "Bienvenue",
    "Willkommen",
    "Benvenuto/a",
    "Bem-vindo/a",
    "欢迎",
    "ようこそ",
    "환영합니다",
    "Hoş geldiniz",
    "Welkom",
    "Välkommen",
    "Velkommen",
    "स्वागतम्" 
  ];

  var headingElement = document.getElementById('greet');
  var currentIndex = 0;

  function changeWelcomeHeading( ){
    headingElement.textContent = welcomeTranslations[currentIndex];
    currentIndex = (currentIndex+1) % welcomeTranslations.length;
  }

  setInterval(changeWelcomeHeading, 700);


const login_email = document.getElementById("login-email");
var input_el = login_email.getAttribute("placeholder");

function email_click_handler(){
  input_el.value = "";
}