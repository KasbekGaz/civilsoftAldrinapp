import React from 'react';

const Button = ({ color, text }) => {
  const getButtonStyle = () => {
    switch (color) {
      case 'green':
        return 'bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded';
      case 'orange':
        return 'bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded';
      case 'red':
        return 'bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded';
    case 'yellow':
        return 'bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded';
      default:
        return '';
    }
  };

  return (
    <button className={getButtonStyle()}>{text}</button>
  );
};

export default Button;