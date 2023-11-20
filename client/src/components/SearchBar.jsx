import { useState } from "react";

const SearchBar = ({ onSearch }) => {
    const [searchTerm, setSearchTerm] = useState('');
  
    const handleInputChange = (e) => {
      setSearchTerm(e.target.value);
    };
  
    const handleSearch = () => {
      onSearch(searchTerm);
    };

    const handleReset = () => {
        setSearchTerm('');
        onReset();
      };
  
    return (
      <div className="flex items-center mb-4">
        <input
          type="text"
          placeholder="Buscar..."
          value={searchTerm}
          onChange={handleInputChange}
          className="border border-gray-300 py-2 px-4 mr-2 rounded"
        />
        <button
          type="button"
          onClick={handleSearch}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Buscar
        </button>
        <button
        type="button"
        onClick={handleReset}
        className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
        >
        Restablecer
        </button>
      </div>
    );
  };
  
  export default SearchBar;