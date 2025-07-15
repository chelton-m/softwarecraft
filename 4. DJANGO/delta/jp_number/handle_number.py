<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Japanese Number Input Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .test-section {
            margin: 20px 0;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
        .input-group {
            margin: 10px 0;
        }
        label {
            display: inline-block;
            width: 150px;
            font-weight: bold;
        }
        input[type="text"] {
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 200px;
        }
        .result {
            margin-top: 10px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Japanese Number Input Test</h1>
    
    <div class="test-section">
        <h2>Test 1: Basic Japanese Number Input</h2>
        <div class="input-group">
            <label>Quantity:</label>
            <input type="text" id="quantity1" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="input-group">
            <label>Unit Price:</label>
            <input type="text" id="price1" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="result">
            <strong>Result:</strong> <span id="result1">0</span>
        </div>
    </div>

    <div class="test-section">
        <h2>Test 2: Assembly Fields</h2>
        <div class="input-group">
            <label>Assembly Quantity:</label>
            <input type="text" id="assembly_qty" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="input-group">
            <label>Assembly Unit Price:</label>
            <input type="text" id="assembly_price" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="result">
            <strong>Assembly Total:</strong> <span id="assembly_total">0</span>
        </div>
    </div>

    <div class="test-section">
        <h2>Test 3: Product Fields</h2>
        <div class="input-group">
            <label>Product Quantity:</label>
            <input type="text" id="product_qty" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="input-group">
            <label>Product Unit Price:</label>
            <input type="text" id="product_price" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="result">
            <strong>Product Total:</strong> <span id="product_total">0</span>
        </div>
    </div>

    <div class="test-section">
        <h2>Test 4: Simple Fields</h2>
        <div class="input-group">
            <label>Simple Quantity:</label>
            <input type="text" id="simple_qty" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="input-group">
            <label>Simple Unit Price:</label>
            <input type="text" id="simple_price" placeholder="Type いち, に, さん..." oninput="window.handleNumberInput(this)">
        </div>
        <div class="result">
            <strong>Simple Total:</strong> <span id="simple_total">0</span>
        </div>
    </div>

    <div class="test-section">
        <h2>Instructions</h2>
        <p>Try typing these Japanese numbers in any input field:</p>
        <ul>
            <li><strong>いち</strong> → should convert to <strong>1</strong></li>
            <li><strong>に</strong> → should convert to <strong>2</strong></li>
            <li><strong>さん</strong> → should convert to <strong>3</strong></li>
            <li><strong>よん</strong> → should convert to <strong>4</strong></li>
            <li><strong>ご</strong> → should convert to <strong>5</strong></li>
            <li><strong>ろく</strong> → should convert to <strong>6</strong></li>
            <li><strong>なな</strong> → should convert to <strong>7</strong></li>
            <li><strong>はち</strong> → should convert to <strong>8</strong></li>
            <li><strong>きゅう</strong> → should convert to <strong>9</strong></li>
            <li><strong>じゅう</strong> → should convert to <strong>10</strong></li>
        </ul>
    </div>

    <!-- Include the formatters.js file -->
    <script src="apps/business/static/business/js/utils/formatters.js"></script>
    
    <script>
        // Test calculation functions
        function calculateTotal(input1, input2, resultSpan) {
            const qty = parseFloat(input1.value.replace(/,/g, '')) || 0;
            const price = parseFloat(input2.value.replace(/,/g, '')) || 0;
            const total = qty * price;
            resultSpan.textContent = total.toLocaleString();
        }

        // Add event listeners for calculations
        document.getElementById('quantity1').addEventListener('input', function() {
            calculateTotal(this, document.getElementById('price1'), document.getElementById('result1'));
        });
        document.getElementById('price1').addEventListener('input', function() {
            calculateTotal(document.getElementById('quantity1'), this, document.getElementById('result1'));
        });

        document.getElementById('assembly_qty').addEventListener('input', function() {
            calculateTotal(this, document.getElementById('assembly_price'), document.getElementById('assembly_total'));
        });
        document.getElementById('assembly_price').addEventListener('input', function() {
            calculateTotal(document.getElementById('assembly_qty'), this, document.getElementById('assembly_total'));
        });

        document.getElementById('product_qty').addEventListener('input', function() {
            calculateTotal(this, document.getElementById('product_price'), document.getElementById('product_total'));
        });
        document.getElementById('product_price').addEventListener('input', function() {
            calculateTotal(document.getElementById('product_qty'), this, document.getElementById('product_total'));
        });

        document.getElementById('simple_qty').addEventListener('input', function() {
            calculateTotal(this, document.getElementById('simple_price'), document.getElementById('simple_total'));
        });
        document.getElementById('simple_price').addEventListener('input', function() {
            calculateTotal(document.getElementById('simple_qty'), this, document.getElementById('simple_total'));
        });
    </script>
</body>
</html> 