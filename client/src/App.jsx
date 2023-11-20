import React from 'react';
import Button from './components/Button';
import Table from "./components/Table";
import { useState, useEffect } from 'react'; //importatnte para la Table
import Form from "./components/Form"; //formulario
import SearchBar from './components/SearchBar'; //para buscar o filtar datos de una tabla

function App() {
  const [backendData, setBackendData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    // Simula una llamada a la API o al backend
    // Reemplázalo con la lógica de llamada a tu backend real
    const fetchData = async () => {
      try {
        // Aquí puedes realizar una llamada a tu backend para obtener datos
        // const response = await fetch('URL_DE_TU_API');
        // const data = await response.json();

        // Simulación de datos para el ejemplo
        const data = [
          { id: 1, nombre: 'Producto A', descripcion: 'Descripción del Producto A' },
          { id: 2, nombre: 'Producto B', descripcion: 'Descripción del Producto B' },
          { id: 3, nombre: 'Producto C', descripcion: 'Descripción del Producto C' },
          { id: 4, nombre: 'Producto D', descripcion: 'Descripción del Producto D' },
        ];

        setBackendData(data);
        setFilteredData(data); //! para el buscador Inicialmente, muestra todos los datos 
      } catch (error) {
        console.error('Error al obtener datos del backend:', error);
      }
    };

    fetchData();
  }, []);

  //! Botones de editar y eliminar en la tabla
  const handleEdit = (item) => {
    // Lógica para editar el elemento (puedes abrir un modal, por ejemplo)
    console.log('Editar:', item);
  };

  const handleDelete = (itemId) => {
    // Lógica para eliminar el elemento con el ID proporcionado
    console.log('Eliminar:', itemId);
  };

  //!---------Para el formulario-------//
  const handleFormSubmit = async (formData) => {
    try {
      // Aquí puedes realizar una llamada a tu backend para enviar los datos del formulario
      // const response = await fetch('URL_DE_TU_API', {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      //   body: JSON.stringify(formData),
      // });
      // const result = await response.json();
      
      // Simulación de éxito para el ejemplo
      console.log('Formulario enviado con éxito:', formData);
    } catch (error) {
      console.error('Error al enviar el formulario:', error);
    }
  };
// ! Para el buscador o fitrar datos
const handleSearch = (searchTerm) => {
  // Filtra los datos según el término de búsqueda
  const filteredResults = backendData.filter((item) =>
    item.nombre.toLowerCase().includes(searchTerm.toLowerCase())
  );
  setFilteredData(filteredResults);
};
//! para filtrar y volver a dejar la tabla como antes
const handleReset = () => {
  // Restablece la búsqueda para mostrar todos los datos
  setFilteredData(backendData);
};


  return (
    <>
     <h1 className="text-white">hOLA mUNDO</h1>
     <div className="flex justify-center items-center h-screen">
      <form className="bg-gray-200 p-6 rounded shadow-md">
        {/* Botón "Crear" (verde) */}
        <Button color="green" text="Crear" />

        {/* Botón "Editar" (naranja) */}
        <Button color="orange" text="Editar" />
        {/* Botón "Actualizar" (amarillo) */}
        <Button color="yellow" text="Actualizar" />
        {/* Botón "Eliminar" (rojo) */}
        <Button color="red" text="Eliminar" />
      </form>
      {/*! El FORMULARIO----------------------- */}
      <div className="flex justify-center items-center h-screen">
        <div className="bg-gray-200 p-6 rounded shadow-md">
          <h2 className="text-xl font-bold mb-4">Formulario de Datos</h2>
          <Form onSubmit={handleFormSubmit} />
        </div>
      </div>

       {/*! Aqui etsa la tabla */}
      <div className="flex justify-center items-center h-screen">
        <div className="bg-gray-200 p-6 rounded shadow-md">
          <h2 className="text-xl font-bold mb-4">Tabla de Datos</h2>
           {/*! el filtro o buscador */}
           <SearchBar onSearch={handleSearch} onReset={handleReset}/>
          
          {/*<Table data={backendData} onEdit={handleEdit} onDelete={handleDelete} /> */}
          <Table data={filteredData}  onEdit={handleEdit} onDelete={handleDelete}/>
        </div>
      </div>
    </div>
    </>
  )
}

export default App
