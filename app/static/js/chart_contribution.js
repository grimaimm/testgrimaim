function getCurrentTheme() {
    return document.documentElement.classList.contains('dark') ? 'dark' : 'light';
}

// Fungsi untuk mendapatkan warna batas yang sesuai dengan tema
function getBorderColor(theme) {
    if (theme === 'dark') {
        return 'rgba(74, 222, 128, 1)';
    } else {
        return 'rgba(21, 128, 61, 1)';
    }
}
function getbackgroundColor(theme) {
    if (theme === 'dark') {
        return 'rgba(74, 222, 128, 0.2)';
    } else {
        return 'rgba(21, 128, 61, 0.2)';
    }
}
// Data kontribusi (sesuaikan dengan data yang Anda terima dari Flask)
var contributionsData = {
    labels: {{ weekly_contributions.keys() | list | tojson | safe }},
    datasets: [{
        label: 'Contributions',
        data: {{ weekly_contributions.values() | list | tojson | safe }},
        backgroundColor: getbackgroundColor(getCurrentTheme()),
        borderColor: getBorderColor(getCurrentTheme()),
        borderWidth: 1
    }]
};

// Mengubah nama bulan menjadi tiga karakter pertama
contributionsData.labels = contributionsData.labels.map(function(label) {
    return label.split(" ")[0].substring(0, 3);
});

// Mengubah nama hari menjadi tiga karakter pertama
var dayLabels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

// Inisialisasi grafik
var ctx = document.getElementById('userActivityChart').getContext('2d');
var userActivityChart = new Chart(ctx, {
    type: 'bar',
    data: contributionsData,
    options: {
        scales: {
            x: {
                type: 'category',
                position: 'bottom',
                labels: contributionsData.labels,
            },
            y: {
                ticks: {
                    callback: function (value, index, values) {
                        // Menampilkan hanya hari
                        return dayLabels[index];
                    }
                }
            }
        }
    }
});