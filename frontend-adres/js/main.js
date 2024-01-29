// funcion para registro la adquisiones de adres
function registrarDatos() {
   const formulario = document.getElementById('registroForm');
   const elementosFormulario = Array.from(formulario.elements);
   var id = document.getElementById('id').value;
    elementosFormulario.forEach(elemento => {
        if (elemento.tagName === 'INPUT' && (elemento.type === 'text' || elemento.type === 'number')) {
            elemento.value = elemento.value.replace(/[$,.]/g, '');
        }
    });

    const formData = new FormData(formulario);
    const jsonData = JSON.stringify(Object.fromEntries(formData));

    if (id) {
      fetch(`http://127.0.0.1:8000/api/actualizar/${id}`, {
          method: 'PUT',
          body: jsonData,
          headers: {
            'Content-Type': 'application/json',
          },
      })
      .then(response => {
          if (!response.ok) {
              throw new Error(`Error en la solicitud: ${response.statusText}`);
          }
          return response.json();
      })
      .then(data => {
          console.log('Registro actualizado con éxito:', data);
          formulario.reset();
          cargarHistorial();
          
      })
      .catch(error => console.error('Error al enviar la solicitud:', error));
  } else {
      // Si no hay un ID, es un nuevo registro
      fetch('http://127.0.0.1:8000/api/registrar', {
          method: 'POST',
          body: jsonData,
          headers: {
              'Content-Type': 'application/json',
          },
      })
      .then(response => {
          if (!response.ok) {
              throw new Error(`Error en la solicitud: ${response.statusText}`);
          }
          return response.json();
      })
      .then(data => {
          console.log('Registro creado con éxito:', data);
          formulario.reset();
          cargarHistorial();
      })
      .catch(error => console.error('Error al enviar la solicitud:', error));
  }
}

function cargarHistorial() {
   fetch('http://127.0.0.1:8000/api/historial')
       .then(response => {
           if (!response.ok) {
               throw new Error(`Error en la solicitud: ${response.statusText}`);
           }
           return response.json();
       })
       .then(data => {
           const historialTableBody = document.querySelector('.historialList');
           historialTableBody.innerHTML = '';

           // Datos del historial
           data.historial_adquisiciones.forEach(item => {
               const tableRow = document.createElement('tr');
               tableRow.innerHTML = `
                  <td>
                   <button onclick="editarRegistro(this)" data-id="${item.id}">Editar</button>
                   </td>
                   <td>${item.presupuesto}</td>
                   <td>${item.unidad}</td>
                   <td>${item.tipo}</td>
                   <td>${item.cantidad}</td>
                   <td>${item.valor_unitario}</td>
                   <td>${item.valor_total}</td>
                   <td>${item.fecha_adquisicion}</td>
                   <td>${item.proveedor}</td>
                   <td>${item.documentacion}</td>
               `;
               historialTableBody.appendChild(tableRow);
           });
       })
       .catch(error => console.error('Error al obtener el historial:', error));
}

// Llamar a cargarHistorial al cargar la página
document.addEventListener('DOMContentLoaded', cargarHistorial);

// edita registro seleccionado en adres
function editarRegistro(button) {
   var row = button.closest('tr');
   var id = button.getAttribute('data-id');
   var presupuesto = row.cells[1].innerText;
   var unidad = row.cells[2].innerText;
   var tipo = row.cells[3].innerText;
   var cantidad = row.cells[4].innerText;
   var valorUnitario = row.cells[5].innerText;
   var valorTotal = row.cells[6].innerText;
   var fechaAdquisicion = row.cells[7].innerText;
   var proveedor = row.cells[8].innerText;
   var documentacion = row.cells[9].innerText;
   document.getElementById('id').value = id;
   document.getElementById('presupuesto').value = presupuesto;
   document.getElementById('unidad').value = unidad;
   document.getElementById('tipo').value = tipo;
   document.getElementById('cantidad').value = cantidad;
   document.getElementById('valorUnitario').value = valorUnitario;
   document.getElementById('valorTotal').value = valorTotal;
   document.getElementById('fechaAdquisicion').value = fechaAdquisicion;
   document.getElementById('proveedor').value = proveedor;
   document.getElementById('documentacion').value = documentacion;

   // Puedes ocultar el botón de "Registrar" y mostrar uno de "Actualizar"
   var registrarButton = document.getElementById('registrarButton');
   var actualizarButton = document.getElementById('updateButton');

   registrarButton.style.display = 'none';
   actualizarButton.style.display = 'block';
}

function filtrarHistorial() {
   var filtro = document.getElementById('filtro').value.toLowerCase();
   var filas = document.querySelectorAll('.historialTable tbody tr');

   filas.forEach(function (fila) {
       var textoUnidad = fila.cells[2].innerText.toLowerCase();
       var textoTipo = fila.cells[3].innerText.toLowerCase();
       var textoProveedor = fila.cells[8].innerText.toLowerCase();

       var cumpleFiltro = textoUnidad.includes(filtro) || textoTipo.includes(filtro) || textoProveedor.includes(filtro);

       fila.style.display = cumpleFiltro ? 'table-row' : 'none';
   });
}

function limpiarFiltro() {
   document.getElementById('filtro').value = '';
   filtrarHistorial();
}

function deleteData() {
   const formulario = document.getElementById('registroForm');
   const elementosFormulario = Array.from(formulario.elements);

   elementosFormulario.forEach(elemento => {
       if (elemento.tagName === 'INPUT' && (elemento.type === 'text' || elemento.type === 'number')) {
           elemento.value = '';
       }
   });

   document.getElementById('registrarButton').style.display = 'block';
   document.getElementById('updateButton').style.display = 'none';
   document.getElementById('deleteButton').style.display = 'block';
}

