function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function ajaxpost () {
  var data = new FormData(document.getElementById("quote-form"));
 
  fetch("1c-server.html", { method:"POST", body:data })
  .then(res => res.text())
 
  .then(response => {
    console.log(response);
    //Hard coded until db finished
    if (response == "OK") { alert("Total Amount Due is: $2542.50"); }
    else { alert("FAILURE!"); }
  })
 
  .catch(err => console.error(err));
 
  return false;
}