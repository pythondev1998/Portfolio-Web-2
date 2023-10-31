$(document).ready(function() {
    // Capturar el evento de envío del formulario
    $("form").submit(function(event) {
        event.preventDefault(); // Evitar que se envíe el formulario de manera predeterminada

        // Ocultar mensajes anteriores
        $(".error-message").empty();
        $(".success-message").empty();

        // Mostrar mensaje de carga
        $("#loading-icon").show();

        // Realizar la solicitud POST utilizando jQuery.ajax()
        $.ajax({
            type: "POST",
            url: "/send_email",
            data: $(this).serialize(), // Serializar los datos del formulario
            success: function(response) {
                // Ocultar mensaje de carga
                $(".loading").empty();

                // Mostrar mensaje de éxito o error si es necesario
                if (response.success) {
                    $(".success-message").text(response.message);
                    setTimeout(function() {
                        $(".success-message").empty();
                        location.reload(); // Recargar la página después de 2 segundos
                    }, 5000); // Mostrar mensaje durante 2 segundos
                } else {
                    $(".error-message").text(response.message);
                }
            },
            error: function() {
                // Ocultar mensaje de carga
                $(".loading").empty();

                $(".error-message").text("An error occurred. Please try again later.");
            }
        });
    });
});