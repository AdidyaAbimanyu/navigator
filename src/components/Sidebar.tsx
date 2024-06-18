import React from 'react';
import { ListGroup, Dropdown } from 'react-bootstrap';

const Sidebar = () => {
  return (
    <div className="bg-primary text-white vh-100">
      <ListGroup variant="flush">
        <ListGroup.Item className="bg-primary text-white border-0 mt-4">
          <input type="text" className="form-control" placeholder="Search" />
        </ListGroup.Item>
        <ListGroup.Item className="bg-primary text-white border-0">
          <Dropdown>
            <Dropdown.Toggle variant="primary" id="dropdown-kota">
              Kota
            </Dropdown.Toggle>
            <Dropdown.Menu>
              <Dropdown.Item href="#/action-1">Semarang</Dropdown.Item>
              <Dropdown.Item href="#/action-2">Surakarta</Dropdown.Item>
              <Dropdown.Item href="#/action-3">Yogyakarta</Dropdown.Item>
              <Dropdown.Item href="#/action-4">Magelang</Dropdown.Item>
              <Dropdown.Item href="#/action-5">Purwokerto</Dropdown.Item>
              <Dropdown.Item href="#/action-6">Kudus</Dropdown.Item>
              <Dropdown.Item href="#/action-7">Klaten</Dropdown.Item>
              <Dropdown.Item href="#/action-8">Tegal</Dropdown.Item>
              <Dropdown.Item href="#/action-9">Pekalongan</Dropdown.Item>
              <Dropdown.Item href="#/action-10">Salatiga</Dropdown.Item>
              <Dropdown.Item href="#/action-11">Cilacap</Dropdown.Item>
              <Dropdown.Item href="#/action-12">Sukoharjo</Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </ListGroup.Item>
        <ListGroup.Item className="bg-primary text-white border-0">
          <Dropdown>
            <Dropdown.Toggle variant="primary" id="dropdown-bencana">
              Bencana Alam
            </Dropdown.Toggle>
            <Dropdown.Menu>
              <Dropdown.Item href="#/action-1">Erupsi</Dropdown.Item>
              <Dropdown.Item href="#/action-2">Tsunami</Dropdown.Item>
              <Dropdown.Item href="#/action-3">Gempa</Dropdown.Item>
              <Dropdown.Item href="#/action-4">Banjir</Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </ListGroup.Item>
      </ListGroup>
    </div>
  );
};

export default Sidebar;
