// Handling Alert button
document.addEventListener('DOMContentLoaded', (event) => {
    const closeButtons = document.querySelectorAll('.close-btn');
    closeButtons.forEach(button => {
      button.addEventListener('click', function() {
        this.parentElement.style.display = 'none';
      });
    });
  });