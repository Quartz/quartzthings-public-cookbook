const TSNE = require('tsne-js');
const fs = require('fs');

// =========
// By default we load our dummy data.
// 
// Replace these files if you'd like to run your own analysis.
// 
// The program expects an array of objects. The tSNE model
// requires an array of numbers. They are values for the key 
// 'stats' in this example.
const dummyData = '/dummy_data.json';
const contents = fs.readFileSync(__dirname + dummyData);
var dummy = JSON.parse(contents);
// =========


// =========
// This is necessary to take the output from our model to 
// make a new JSON
var inputData = []
var outputData = [];

dummy.forEach( function(data, i) {
    inputData.push(data.stats);
    outputData.push({ 'pokemon': data.pokemon, 'stats': data.stats } )
});
// =========


// =========
// This is where the magic happens... you can read more 
// about what's going on here: https://github.com/karpathy/tsnejs
let model = new TSNE({
    dim: 2,
    perplexity: 20,
    earlyExaggeration: 5.0,
    learningRate: 600.0,
    nIter: 5000,
    metric: 'euclidean'
});

model.init({
    data: inputData,
    type: 'dense'
});
// =========


// =========
// `error`, `iter`: final error and iteration number
// note: computation-heavy action happens here
let [error, iter] = model.run();
// =========


// =========
// `outputScaled` is `output` scaled to a range of [-1, 1]
let outputScaled = model.getOutputScaled();
// =========


// =========
// We store the output in our array in the key named coords
outputData.forEach(function (poke, i) {
    poke.coords = outputScaled[i];
});
// =========

// =========
// Finally we write to file the name of our data
// In this instance... it's poke_coords
fs.writeFileSync('poke_coords.json', JSON.stringify(outputData), function (err) {
    if (err) throw err;
    console.log('File written');
});
// =========