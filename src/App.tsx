import React from 'react';
import Sidebar from './components/Sidebar';
import Main from './components/Main';
import { Container, Row, Col } from 'react-bootstrap';

function App() {
  return (
    <Container fluid>
      <Row>
        <Col xs={2} className="p-0">
          <Sidebar />
        </Col>
        <Col xs={10} className="p-0">
          <Main />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
