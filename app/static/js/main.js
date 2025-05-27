// Add client-side validation for image upload
document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.querySelector('input[type="file"]');
  const submitButton = document.querySelector('button[type="submit"]');

  fileInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      if (!file.type.startsWith("image/")) {
        alert("Please upload an image file");
        this.value = "";
        return;
      }

      if (file.size > 5 * 1024 * 1024) {
        alert("File size should be less than 5MB");
        this.value = "";
        return;
      }
    }
  });
});
