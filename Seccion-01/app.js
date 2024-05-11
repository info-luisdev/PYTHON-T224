document.addEventListener("DOMContentLoaded", function() {
    const facturacionForm = document.getElementById("facturacionForm");
    const facturaOutput = document.getElementById("facturaOutput");
    let clientes = [];

    facturacionForm.addEventListener("submit", function(event) {
        event.preventDefault();
    });

    document.getElementById("facturarBtn").addEventListener("click", function() {
        const clienteName = document.getElementById("clienteName").value;
        const seccion = document.querySelector("input[name='seccion']:checked").value;
        const factura = {
            nombre: clienteName,
            seccion: seccion,
            totalPagado: "$2000",
            fecha: new Date().toLocaleDateString()
        };
        clientes.push(factura);
        mostrarFactura(factura);
    });

    document.getElementById("cuadreCajaBtn").addEventListener("click", function() {
        const totalPagado = clientes.reduce((total, factura) => total + parseFloat(factura.totalPagado.slice(1)), 0);
        mostrarResultado(`Total Pagado: $${totalPagado.toFixed(2)}`);
    });

    document.getElementById("cuadreSeccionBtn").addEventListener("click", function() {
        const seccion = prompt("Ingrese la sección (1ro, 2do, 3ro, 4to, 5to, 6to):");
        const totalPagado = clientes.filter(factura => factura.seccion === seccion)
                                    .reduce((total, factura) => total + parseFloat(factura.totalPagado.slice(1)), 0);
        mostrarResultado(`Total Pagado para Sección ${seccion}: $${totalPagado.toFixed(2)}`);
    });

    document.getElementById("resetBtn").addEventListener("click", function() {
        const password = prompt("Ingrese la contraseña para resetear:");
        if (password === "admin1234") {
            clientes = [];
            facturaOutput.innerHTML = "";
        } else {
            alert("Contraseña incorrecta. Operación cancelada.");
        }
    });

    document.getElementById("reportesBtn").addEventListener("click", function() {
        let totalEstudiantes = clientes.length;
        let totalPagado = clientes.reduce((total, factura) => total + parseFloat(factura.totalPagado.slice(1)), 0);
        let reporte = `Total Estudiantes: ${totalEstudiantes}\nTotal Pagado por Todos: $${totalPagado.toFixed(2)}`;
        const secciones = ["1ro", "2do", "3ro", "4to", "5to", "6to"];
        secciones.forEach(seccion => {
            const totalSeccion = clientes.filter(factura => factura.seccion === seccion)
                                        .reduce((total, factura) => total + parseFloat(factura.totalPagado.slice(1)), 0);
            reporte += `\nTotal Pagado para Sección ${seccion}: $${totalSeccion.toFixed(2)}`;
        });
        mostrarResultado(reporte);
    });

    function mostrarFactura(factura) {
        facturaOutput.innerHTML += `
            <div class="factura">
                <p><strong>Nombre:</strong> ${factura.nombre}</p>
                <p><strong>Sección:</strong> ${factura.seccion}</p>
                <p><strong>Total Pagado:</strong> ${factura.totalPagado}</p>
                <p><strong>Fecha:</strong> ${factura.fecha}</p>
            </div>
        `;
    }

    function mostrarResultado(resultado) {
        facturaOutput.innerHTML += `<div class="resultado">${resultado}</div>`;
    }
});
