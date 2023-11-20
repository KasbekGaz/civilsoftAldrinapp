import React from 'react';
import Button from './Button' //importamos el componente boton

const Table = ({ data }) => {

    /*Este componente de tabla recibe un prop llamado data, que es un array de objetos. Cada objeto representa una fila de la tabla, y las claves del objeto corresponden a las columnas. */

  return (
    <table className="min-w-full border border-gray-300">
      <thead>
        <tr>
          <th className="border border-gray-300 py-2 px-4">ID</th>
          <th className="border border-gray-300 py-2 px-4">Nombre</th>
          <th className="border border-gray-300 py-2 px-4">Descripción</th>
          <th className="border border-gray-300 py-2 px-4">Acciones</th> {/* Nueva columna para acciones */}
          {/* Agrega más columnas según tus datos */}
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td className="border border-gray-300 py-2 px-4">{item.id}</td>
            <td className="border border-gray-300 py-2 px-4">{item.nombre}</td>
            <td className="border border-gray-300 py-2 px-4">{item.descripcion}</td>
            <td className="border border-gray-300 py-2 px-4">
              {/* Botón "Editar" */}
              <Button color="orange" text="Editar" onClick={() => onEdit(item)} />
              {/* Botón "Eliminar" */}
              <Button color="red" text="Eliminar" onClick={() => onDelete(item.id)} />
            </td>
            {/* Agrega más celdas según tus datos */}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;