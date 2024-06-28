/* jshint esversion: 6 */
// Import necessary modules
const mongoose = require('mongoose');

// Define the schema for cars
const carSchema = new mongoose.Schema({
  dealer_id: {
    type: Number,
    required: true,
  },
  make: {
    type: String,
    required: true,
  },
  model: {
    type: String,
    required: true,
  },
  bodyType: {
    type: String,
    required: true,
  },
  year: {
    type: Number,
    required: true,
  },
  mileage: {
    type: Number,
    required: true,
  },
});

// Export the model
module.exports = mongoose.model('Car', carSchema);
