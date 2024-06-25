import React, { useState } from 'react';
import { FaBars } from 'react-icons/fa'; // Install react-icons if you haven't already: npm install react-icons

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  const handleSearch = () => {
    // Tambahkan logika pencarian di sini sesuai kebutuhan
    console.log('Searching...');
    // Misalnya, lakukan sesuatu seperti pencarian data atau navigasi ke halaman pencarian
  };

  return (
    <div>
      <div className='flex flex-col'>
        <div className="absolute top-4 left-4 cursor-pointer z-50" onClick={toggleSidebar}>
          <FaBars size={24} color="#000" />
        </div>
        {isOpen && (
          <div className="bg-blue-500 text-white w-64 h-full fixed top-0 left-0 z-40">
            <div className="p-4">
              <label className="block mb-2 pt-10">Kota</label>
              <select className="w-full p-2 rounded bg-blue-600">
                <option>Semarang</option>
                <option>Solo</option>
                <option>Yogyakarta</option>
                <option>Magelang</option>
                <option>Purwokerto</option>
                <option>Kudus</option>
                <option>Klaten</option>
                <option>Tegal</option>
                <option>Pekalongan</option>
                <option>Salatiga</option>
                <option>Cilacap</option>
                <option>Sukoharjo</option>
              </select>
            </div>
            <div className="p-4">
              <label className="block mb-2">Bencana Alam</label>
              <select className="w-full p-2 rounded bg-blue-600">
                <option>Erupsi</option>
                <option>Tsunami</option>
                <option>Gempa</option>
                <option>Banjir</option>
              </select>
            </div>
            <div className='p-4'>
              <button onClick={handleSearch} className="bg-blue-600 text-white rounded w-full p-2">
                Search!
              </button>
            </div>
          </div>
        )}
      </div>
      <div className="flex justify-center mt-4">
      </div>
    </div>
  );
};

export default Sidebar;
