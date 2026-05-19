const ctx = document.getElementById('expenseChart');

new Chart(ctx, {
    type: 'doughnut',

    data: {
        labels: ['Income', 'Expense'],

        datasets: [{
            data: [income, expense],

            backgroundColor: [
                '#22c55e',
                '#ef4444'
            ],

            borderWidth: 0
        }]
    },

    options: {
        responsive: true,

        plugins: {
            legend: {
                labels: {
                    color: 'white',
                    font: {
                        size: 14
                    }
                }
            }
        }
    }
});