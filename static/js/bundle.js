const path = require('path');

module.exports = {
  entry: './path/to/export.js', // Replace with the correct path to your export.js file
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/js'), // Replace with the path to your static/js folder
  },
  mode: 'production',
};
