var form_fields = document.getElementsByTagName("input");
form_fields[1].placeholder = "First Name";
form_fields[2].placeholder = "Last Name";
form_fields[3].placeholder = "Enter Email";
form_fields[4].placeholder = "Create Username";
form_fields[5].placeholder = "Create Password";

for (var field in form_fields) {
  form_fields[form_fields].className += "form-control";
}
