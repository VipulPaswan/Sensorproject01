document.addEventListener("DOMContentLoaded", function() {
    const dropzone = document.querySelector(".dropzone");
    const input = document.querySelector(".upload-input");

    dropzone.addEventListener("click", () => input.click());
});
