import axios from 'axios';
import { useEffect, useState } from 'react';

function App() {
  const [viloes, setViloes] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/viloes")
      .then(response => setViloes(response.data))
      .catch(err => console.error("Erro ao carregar vilões:", err));
  }, []);

  return (
    <div>
      <h1>Lista de Vilões</h1>
      <ul>
        {viloes.map((vilao, index) => (
          <li key={index}>{vilao.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
