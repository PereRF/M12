const constraints = {
  name: {
    presence: true,
  },
  email: {
    presence: true,
    email: true,
  },
  password: {
    presence: true,
    length: {
      minimum: 6,
      maximum: 12,
    },
    format: {
      pattern: /^(?=.*[a-z])(?=.*[A-Z])/,
      message: "debe contener al menos una letra minúscula y una letra mayúscula",
    },
  },
};

$(document).ready(function () {
  const form = document.getElementById("myForm");

  form.addEventListener("input", function (event) {
    const fieldName = event.target.getAttribute("name");
    const errors = validate(
      {
        [fieldName]: event.target.value,
      },
      {
        [fieldName]: constraints[fieldName],
      }
    );

    if (errors) {
      document.getElementById(`${fieldName}-error`).textContent = errors[fieldName][0];
    } else {
      document.getElementById(`${fieldName}-error`).textContent = "";
    }
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(form);
    const errors = validate(formData, constraints);

    if (errors) {
      // Muestra errores generales o toma medidas, como bloquear el envío del formulario.
    } else {
      // Envía el formulario si no hay errores.
      // Puedes agregar tu lógica de envío aquí.
    }
  });
});





