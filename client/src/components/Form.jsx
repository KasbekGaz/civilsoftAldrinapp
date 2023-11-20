import React, { useState } from 'react';
import Button from './Button'



const Form = ({ onSubmit }) => {
  const [formData, setFormData] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Agrega tus campos de formulario aquí */}
      <label>
        Nombre:
        <input type="text" name="nombre" onChange={handleChange} />
      </label>
      <label>
        Descripción:
        <input type="text" name="descripcion" onChange={handleChange} />
      </label>

      {/* Agrega más campos según tus necesidades */}

      <Button color="green" text="Crear" type="submit" />
    </form>
  );
};

export default Form;