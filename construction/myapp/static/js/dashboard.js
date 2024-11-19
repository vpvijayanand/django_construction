
const adminPanelButton = document.getElementById('adminPanelButton');
const adminPanel = document.getElementById('adminPanel');
const closeAdminPanel = document.getElementById('closeAdminPanel');

adminPanelButton.addEventListener('click', () => {
    adminPanel.style.display = 'block';
});

closeAdminPanel.addEventListener('click', () => {
    adminPanel.style.display = 'none';
});

// New Entry Modal functionality
const newEntryButton = document.getElementById('newEntryButton');
const newEntryModal = document.getElementById('newEntryModal');
const closeNewEntryModal = document.getElementById('closeNewEntryModal');

newEntryButton.addEventListener('click', () => {
    newEntryModal.style.display = 'block';
});

closeNewEntryModal.addEventListener('click', () => {
    newEntryModal.style.display = 'none';
});

// Close modals when clicking outside
window.addEventListener('click', (event) => {
    if (event.target === adminPanel) {
        adminPanel.style.display = 'none';
    }
    if (event.target === newEntryModal) {
        newEntryModal.style.display = 'none';
    }
});

// Chart.js implementation
const ctx = document.getElementById('projectChart').getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Office Tower A', 'Residential Complex B', 'Shopping Mall C'],
        datasets: [{
            label: 'Budget',
            data: [25, 18, 32],
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }, {
            label: 'Spent',
            data: [12, 9, 28.8],
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }, {
            label: 'Remaining',
            data: [13, 9, 3.2],
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Amount (Cr ₹)'
                }
            }
        }
    }
});