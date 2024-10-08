const animationContainer = document.getElementById('animationContainer');
const trainButton = document.getElementById('trainButton');
const skipButton = document.getElementById('skipButton');
const outputValue = document.getElementById('outputValue');

let inputLayer = [];
let hiddenLayers = [];
let outputLayer = [];
let numHiddenLayers = 0;
let neuronsPerHiddenLayer = [];

// Function to create layers and neurons
function createNeuralNetwork() {
    // Clear previous layers
    animationContainer.innerHTML = '';

    const inputValues = document.getElementById('inputValues').value.split(',').map(Number);
    numHiddenLayers = parseInt(document.getElementById('hiddenLayers').value);
    const outputNeuronsCount = parseInt(document.getElementById('outputNeurons').value);

    // User input for neurons in each hidden layer
    for (let i = 0; i < numHiddenLayers; i++) {
        const neurons = parseInt(prompt(`Enter number of neurons for hidden layer ${i + 1}:`));
        neuronsPerHiddenLayer.push(neurons);
    }
    
    // Create input layer
    const inputDiv = document.createElement('div');
    inputDiv.className = 'layer';
    inputValues.forEach(value => {
        const neuron = createNeuron(value);
        inputLayer.push(neuron);
        inputDiv.appendChild(neuron);
    });
    animationContainer.appendChild(inputDiv);
    
    // Create hidden layers based on user input
    for (let i = 0; i < numHiddenLayers; i++) {
        const hiddenDiv = document.createElement('div');
        hiddenDiv.className = 'layer';
        const hiddenLayer = [];
        for (let j = 0; j < neuronsPerHiddenLayer[i]; j++) {
            const neuron = createNeuron(0);
            hiddenLayer.push(neuron);
            hiddenDiv.appendChild(neuron);
        }
        hiddenLayers.push(hiddenLayer);
        animationContainer.appendChild(hiddenDiv);
    }

    // Create output layer
    const outputDiv = document.createElement('div');
    outputDiv.className = 'layer';
    outputLayer = [];
    for (let i = 0; i < outputNeuronsCount; i++) {
        const outputNeuron = createNeuron(0);
        outputLayer.push(outputNeuron);
        outputDiv.appendChild(outputNeuron);
    }
    animationContainer.appendChild(outputDiv);

    // Initialize connections (for visual purposes)
    connectLayers(inputLayer, hiddenLayers[0]);
    for (let i = 0; i < hiddenLayers.length - 1; i++) {
        connectLayers(hiddenLayers[i], hiddenLayers[i + 1]);
    }
    connectLayers(hiddenLayers[hiddenLayers.length - 1], outputLayer);
}

// Function to create a neuron
function createNeuron(value) {
    const neuron = document.createElement('div');
    neuron.className = 'neuron';
    neuron.innerText = value.toFixed(2);
    return neuron;
}

// Function to connect layers visually
function connectLayers(layer1, layer2) {
    layer1.forEach((neuron1) => {
        layer2.forEach((neuron2) => {
            const connection = document.createElement('div');
            connection.className = 'connection';
            const left = neuron1.offsetLeft + 25; // Center of neuron1
            const top = neuron1.offsetTop + 25; // Center of neuron1
            const left2 = neuron2.offsetLeft + 25; // Center of neuron2
            const top2 = neuron2.offsetTop + 25; // Center of neuron2
            const height = top2 - top;

            connection.style.left = `${left}px`;
            connection.style.top = `${top}px`;
            connection.style.height = `${height}px`;
            animationContainer.appendChild(connection);
        });
    });
}

// Function to train the network and animate
async function trainNetwork() {
    const inputValues = document.getElementById('inputValues').value.split(',').map(Number);
    for (let epoch = 0; epoch < 10; epoch++) {
        for (let i = 0; i < inputLayer.length; i++) {
            const neuron = inputLayer[i];
            neuron.innerText = inputValues[i].toFixed(2);
            neuron.style.borderColor = 'blue'; // Highlight firing neuron
            await new Promise(resolve => setTimeout(resolve, 100));
            neuron.style.borderColor = 'white'; // Reset color
        }

        // Simulate hidden layer activations
        for (const layer of hiddenLayers) {
            for (const neuron of layer) {
                neuron.innerText = (Math.random()).toFixed(2); // Simulate output
                neuron.style.borderColor = 'blue'; // Highlight firing neuron
                await new Promise(resolve => setTimeout(resolve, 100));
                neuron.style.borderColor = 'white'; // Reset color
            }
        }

        // Simulate output layer activation
        for (const neuron of outputLayer) {
            const output = (Math.random()).toFixed(2); // Simulated output
            neuron.innerText = output;
            neuron.style.borderColor = 'blue'; // Highlight firing neuron
            await new Promise(resolve => setTimeout(resolve, 100));
            neuron.style.borderColor = 'white'; // Reset color
        }

        if (epoch === 9) {
            outputValue.innerText = (Math.random()).toFixed(2); // Show final output
        }
    }
}

// Event listeners
document.getElementById('generateNN').addEventListener('click', createNeuralNetwork);
trainButton.addEventListener('click', trainNetwork);
skipButton.addEventListener('click', () => {
    outputValue.innerText = (Math.random()).toFixed(2); // Skip to output
});
