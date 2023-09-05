function exportAsPdf() {
  const pageWidth = 10; // in cm
  const pageHeight = 7; // in cm

  // Create a new jsPDF instance with the desired page size
  const doc = new jsPDF({
    unit: 'cm',
    format: [pageWidth, pageHeight]
  });

  // Convert the HTML content to a canvas element
  html2canvas(document.getElementById('contentToExport'))
    .then(canvas => {
      const imgData = canvas.toDataURL('image/png');

      // Add the image to the PDF document
      doc.addImage(imgData, 'PNG', 0, 0, pageWidth, pageHeight);

      // Save the PDF document
      doc.save('export.pdf');
    });
}