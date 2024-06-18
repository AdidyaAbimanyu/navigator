import React, { useState } from 'react';
import { FaBars } from 'react-icons/fa'; // Install react-icons if you haven't already: npm install react-icons

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <div className="absolute top-4 left-4 cursor-pointer z-50" onClick={toggleSidebar}>
        <FaBars size={24} color="#fff" />
      </div>
      {isOpen && (
        <div className="bg-blue-500 text-white w-64 h-full fixed top-0 left-0 z-40">
          <div className="p-4 mt-10">
            <input type="text" className="w-full p-2 rounded" placeholder="Search" />
          </div>
          <div className="p-4">
            <label className="block mb-2">Kota</label>
            <select className="w-full p-2 rounded bg-blue-600">
              <option>Semarang</option>
              <option>Surakarta</option>
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
        </div>
      )}
    </>
  );
};

export default Sidebar;
