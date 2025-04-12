document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const city = document.querySelector('input[name="city"]').value;
    const resultsDiv = document.getElementById('results');

    resultsDiv.innerHTML = '<p>Loading...</p>';

    try {
        const response = await fetch('/get_weather_image', {
            method: 'POST',
            body: new URLSearchParams({ city }),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }

        const data = await response.json();
        if (data.error) {
            resultsDiv.innerHTML = `<p>${data.error}</p>`;
            return;
        }

        resultsDiv.innerHTML = `
            <h2>Weather in ${data.city}</h2>
            <p>Condition: ${data.weather_condition}</p>
            <img src="${data.image_url}" alt="Weather Image" style="max-width:100%;border-radius:8px;">
        `;
    } catch (error) {
        resultsDiv.innerHTML = `<p>${error.message}</p>`;
    }
});
