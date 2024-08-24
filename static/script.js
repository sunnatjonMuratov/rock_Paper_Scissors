document.addEventListener('DOMContentLoaded', () => {
    const choices = document.querySelectorAll('.choice');
    const message = document.getElementById('message');
    const computerChoiceElement = document.getElementById('computer-choice');
    const resetButton = document.getElementById('reset');

    choices.forEach(choice => {
        choice.addEventListener('click', async () => {
            const userChoice = choice.getAttribute('data-choice');
            const response = await fetch('/play', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ choice: userChoice })
            });
            const data = await response.json();
            message.textContent = `You chose ${data.user_choice}. ${data.result}`;
            computerChoiceElement.textContent = data.computer_choice;
            resetButton.style.display = 'block';
        });
    });

    resetButton.addEventListener('click', () => {
        message.textContent = '';
        computerChoiceElement.textContent = '';
        resetButton.style.display = 'none';
    });
});
