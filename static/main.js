function myFunction() {
  var copyText = document.getElementById("link");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
  alert("Link Copied: " + copyText.value);
}