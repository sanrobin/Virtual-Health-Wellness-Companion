// Handle form submission
document.getElementById('meal-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/add_meal', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            // Reload the page to show the updated meal log
            window.location.reload();
        } else {
            console.error('Failed to add meal');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});