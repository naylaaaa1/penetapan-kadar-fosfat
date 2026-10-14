<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Fosfat - Spektrofotometer UV-Vis</title>
    <!-- Tailwind CSS untuk tampilan modern -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <!-- Chart.js untuk grafik kurva kalibrasi -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans leading-relaxed">
    <div class="max-w-6xl mx-auto p-6">
        <header class="mb-8 text-center">
            <h1 class="text-3xl font-bold text-blue-800 mb-2">🧪 Penetapan Kadar Fosfat Metode Asam Askorbat</h1>
            <p class="text-gray-600">Aplikasi web interaktif untuk kurva kalibrasi dan analisis kadar fosfat menggunakan Spektrofotometer UV-Vis.</p>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Card 1: Kurva Kalibrasi -->
            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
                <h2 class="text-xl font-semibold text-gray-700 mb-4">1. Data Kurva Kalibrasi (Deret Standar)</h2>
                <div class="overflow-x-auto mb-4">
                    <table class="w-full border-collapse text-left text-sm">
                        <thead>
                            <tr class="bg-blue-50 text-blue-900 border-b">
                                <th class="p-2">Konsentrasi (mg/L)</th>
                                <th class="p-2">Absorbansi (A)</th>
                                <th class="p-2 text-center">Aksi</th>
                            </tr>
                        </thead>
                        <tbody id="stdTableBody">
                            <!-- Baris tabel di-generate via JavaScript -->
                        </tbody>
                    </table>
                </div>
                <button onclick="addStandardRow()" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition cursor-pointer mb-4">+ Tambah Titik Standar</button>
                
                <div id="regressionResult" class="bg-blue-50 p-4 rounded-lg border border-blue-200 text-sm space-y-1">
                    <p><strong>Persamaan Regresi:</strong> <span id="eqText">y = 0.0000x + 0.0000</span></p>
                    <p><strong>Koefisien Korelasi (R²):</strong> <span id="r2Text">0.0000</span></p>
                </div>
            </div>

            <!-- Card 2: Grafik & Perhitungan Sampel -->
            <div class="space-y-6">
                <!-- Grafik -->
                <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
                    <h2 class="text-xl font-semibold text-gray-700 mb-4">📈 Grafik Kurva Kalibrasi</h2>
                    <div class="relative h-64">
                        <canvas id="calibrationChart"></canvas>
                    </div>
                </div>

                <!-- Perhitungan Sampel -->
                <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
                    <h2 class="text-xl font-semibold text-gray-700 mb-4">2. Perhitungan Kadar Sampel</h2>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-600 mb-1">Absorbansi Sampel ($A_s$)</label>
                            <input type="number" id="sampleAbs" step="0.0001" value="0.3100" class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-600 mb-1">Faktor Pengenceran (FP)</label>
                            <input type="number" id="dilutionFactor" step="1" value="10" class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none">
                        </div>
                        <button onclick="calculateSample()" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white py-2.5 rounded-lg font-medium transition cursor-pointer">Hitung Kadar Fosfat</button>
                        
                        <div id="sampleResult" class="hidden bg-emerald-50 p-4 rounded-lg border border-emerald-200 space-y-2">
                            <p class="text-sm text-emerald-800">Konsentrasi dalam Kurva ($x$): <strong id="resX">0.00 mg/L</strong></p>
                            <p class="text-base font-bold text-emerald-900">Kadar Fosfat Akhir ($C \times FP$): <span id="resFinal" class="text-emerald-700">0.00 mg/L</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let initialData = [
            { conc: 0.0, abs: 0.000 },
            { conc: 0.2, abs: 0.122 },
            { conc: 0.4, abs: 0.245 },
            { conc: 0.6, abs: 0.370 },
            { conc: 0.8, abs: 0.495 },
            { conc: 1.0, abs: 0.620 }
        ];

        let chartInstance = null;
        let currentSlope = 0;
        let currentIntercept = 0;

        function renderTable() {
            const tbody = document.getElementById('stdTableBody');
            tbody.innerHTML = '';
            initialData.forEach((item, index) => {
                const tr = document.createElement('tr');
                tr.className = 'border-b hover:bg-gray-50';
                tr.innerHTML = `
                    <td class="p-2"><input type="number" step="any" value="${item.conc}" onchange="updateData(${index}, 'conc', this.value)" class="w-full p-1 border rounded"></td>
                    <td class="p-2"><input type="number" step="any" value="${item.abs}" onchange="updateData(${index}, 'abs', this.value)" class="w-full p-1 border rounded"></td>
                    <td class="p-2 text-center"><button onclick="deleteRow(${index})" class="text-red-500 hover:text-red-700 font-bold">×</button></td>
                `;
                tbody.appendChild(tr);
            });
            processRegression();
        }

        function addStandardRow() {
            initialData.push({ conc: 0.0, abs: 0.0 });
            renderTable();
        }

        function deleteRow(index) {
            if (initialData.length > 2) {
                initialData.splice(index, 1);
                renderTable();
            } else {
                alert("Minimal harus ada 2 titik standar!");
            }
        }

        function updateData(index, field, value) {
            initialData[index][field] = parseFloat(value) || 0;
            processRegression();
        }

        function processRegression() {
            const x = initialData.map(d => d.conc);
            const y = initialData.map(d => d.abs);
            const n = x.length;

            let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0, sumY2 = 0;
            for (let i = 0; i < n; i++) {
                sumX += x[i];
                sumY += y[i];
                sumXY += x[i] * y[i];
                sumX2 += x[i] * x[i];
                sumY2 += y[i] * y[i];
            }

            const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
            const intercept = (sumY - slope * sumX) / n;

            const numerator = (n * sumXY - sumX * sumY);
            const denominator = Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));
            const r = denominator === 0 ? 0 : numerator / denominator;
            const r2 = r * r;

            currentSlope = slope;
            currentIntercept = intercept;

            document.getElementById('eqText').innerText = `y = ${slope.toFixed(4)}x + ${intercept.toFixed(4)}`;
            document.getElementById('r2Text').innerText = r2.toFixed(4);

            updateChart(x, y, slope, intercept);
        }

        function updateChart(x, y, slope, intercept) {
            const ctx = document.getElementById('calibrationChart').getContext('2d');
            
            const scatterData = x.map((val, i) => ({ x: val, y: y[i] }));
            const minX = Math.min(...x);
            const maxX = Math.max(...x);
            const lineData = [
                { x: minX, y: slope * minX + intercept },
                { x: maxX, y: slope * maxX + intercept }
            ];

            if (chartInstance) {
                chartInstance.destroy();
            }

            chartInstance = new Chart(ctx, {
                type: 'scatter',
                data: {
                    datasets: [
                        {
                            label: 'Data Standar',
                            data: scatterData,
                            backgroundColor: '#2563eb',
                            pointRadius: 6
                        },
                        {
                            label: 'Garis Regresi',
                            data: lineData,
                            type: 'line',
                            borderColor: '#dc2626',
                            borderWidth: 2,
                            borderDash: [5, 5],
                            pointRadius: 0
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: { title: { display: true, text: 'Konsentrasi (mg/L)' } },
                        y: { title: { display: true, text: 'Absorbansi' } }
                    }
                }
            });
        }

        function calculateSample() {
            const absSampel = parseFloat(document.getElementById('sampleAbs').value) || 0;
            const fp = parseFloat(document.getElementById('dilutionFactor').value) || 1;

            if (currentSlope === 0) {
                alert("Slope tidak boleh bernilai nol.");
                return;
            }

            const xVal = (absSampel - currentIntercept) / currentSlope;
            const finalVal = xVal * fp;

            document.getElementById('sampleResult').classList.remove('hidden');
            document.getElementById('resX').innerText = `${xVal.toFixed(4)} mg/L`;
            document.getElementById('resFinal').innerText = `${finalVal.toFixed(4)} mg/L`;
        }

        window.onload = function() {
            renderTable();
        };
    </script>
</body>
</html>
