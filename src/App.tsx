import React from 'react';
import Sidebar from './components/Sidebar';
import Main from './components/Main';

function App() {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-grow">
        <Main />
      </div>
    </div>
  );
}

export default App;
