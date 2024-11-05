document.getElementById('logout').addEventListener('click', function (event) {
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
            window.location.href = '/logout/'; // Redirige a la URL de logout si se confirma
        }
    });
});