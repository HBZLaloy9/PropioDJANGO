document.getElementById('logout').addEventListener('click', function (event) {
    event.preventDefault(); // Previene la redirección inmediata

    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡Perderás tu sesión actual!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, desconectar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '{% url "logout" %}'; // Redirige solo si el usuario confirma
        }
    });
});
