document.addEventListener('DOMContentLoaded', function () {
    var dropArea = document.getElementById('dropArea');
    var fileInput = document.getElementById('fileInput');
  
    dropArea.addEventListener('click', function () {
      fileInput.click();
    });
  
    dropArea.addEventListener('dragover', function (e) {
      e.preventDefault();
      dropArea.classList.add('border-primary');
    });
  
    dropArea.addEventListener('dragleave', function (e) {
      e.preventDefault();
      dropArea.classList.remove('border-primary');
    });
  
    dropArea.addEventListener('drop', function (e) {
      e.preventDefault();
      dropArea.classList.remove('border-primary');
      var files = e.dataTransfer.files;
      handleFiles(files);
    });
  
    fileInput.addEventListener('change', function (e) {
      var files = fileInput.files;
      handleFiles(files);
    });
  
    function handleFiles(files) {
      // Handle the files (for example, using FormData to send it to a server)
      console.log(files);
    }
  });
  