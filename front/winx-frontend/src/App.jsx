import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import WinxCarousel from './components/WinxCarrossel';
import FadaDetalhe from './Pages/FadaDetalhe';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WinxCarousel />} />
        <Route path="/fada/:nome" element={<FadaDetalhe />} />
      </Routes>
    </Router>
  );
}

export default App;