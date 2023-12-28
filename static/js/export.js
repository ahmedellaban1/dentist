import domtoimage from 'dom-to-image';
import html2canvas from 'html2canvas';

// Get a reference to the export button
const exportButton = document.getElementById('exportButton');

// Add a click event listener to the export button
exportButton.addEventListener('click', () => {
  // Get a reference to the HTML element you want to export (e.g., the container div of your page)
  const container = document.getElementById('container');

  // Use dom-to-image to convert the HTML element to a canvas image
  domtoimage.toCanvas(container)
    .then((canvas) => {
      // Convert the canvas image to a data URL
      const dataURL = canvas.toDataURL('image/png');

      // Create a temporary link element
      const link = document.createElement('a');
      link.href = dataURL;
      link.download = 'exported_image.png';

      // Simulate a click event on the link to trigger the download
      link.click();
    })
    .catch((error) => {
      console.error('An error occurred while exporting the image:', error);
    });
});