function fetchData() {
    fetch('http://192.168.1.100/data')
        .then(response => response.text())
        .then(data => {
            document.getElementById('moistureLevel').textContent = data;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}
