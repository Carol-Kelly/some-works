const input1 = document.getElementById('number_of_completed_surveys');
const input2 = document.getElementById('survey_response_rate_percent');

input1.addEventListener('input', () => {
  if (input1.value < 0 || input1.value > 11840) {
    alert('Please enter a number between 0 and 11840');
    input1.value = '';
  }
});

input2.addEventListener('input', () => {
  if (input2.value < 0 || input2.value > 70) {
    alert('Please enter a number between 0 and 70');
    input2.value = '';
  }
});




