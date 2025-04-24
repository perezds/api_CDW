import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import WinxCarousel from './components/WinxCarrossel';
import Header from './components/Header';
import FadaDetalhe from './pages/FadaDetalhe';
import './index.css';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<WinxCarousel />} />
        <Route path="/fada/:nome" element={<FadaDetalhe />} />
      </Routes>
    </Router>
  );
}

export default App;
