var elementID = document.querySelector('#tts').innerHTML;


const message = new SpeechSynthesisUtterance();

// set the text to be spoken
message.text = elementID ;

// create an instance of the speech synthesis object
const speechSynthesis = window.speechSynthesis;

// start speaking
speechSynthesis.speak(message);