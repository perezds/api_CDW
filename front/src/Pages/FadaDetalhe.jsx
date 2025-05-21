import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './FadaDetalhe.css';

const FadaDetalhe = () => {
  const { nome } = useParams();
  const [fada, setFada] = useState(null);

  useEffect(() => {
<<<<<<< HEAD
    axios.get(`http://127.0.0.1:8000/fada/${nome}`)
=======
    axios.get(`http://localhost:8000/fada/${nome}`)
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
      .then((response) => {
        setFada(response.data);
      })
      .catch((error) => {
        console.error('Erro ao buscar dados da fada:', error);
      });
  }, [nome]);

  if (!fada) {
    return <p>Carregando magia...</p>;
  }

  return (
    <div className="fada-detalhe-container">
      <img src={`/images/${fada.nome.toLowerCase()}.jpg`} alt={fada.nome} />
      <div className="info">
        <h1>{fada.nome}</h1>
        <p><strong>Poder:</strong> {fada.poder}</p>
        <p><strong>Mundo:</strong> {fada.mundo.nome}</p>
        <p><strong>Transformações:</strong> {fada.transformacoes?.map(t => t.nome).join(', ') || 'Nenhuma'}</p>
        <p><strong>Episódios:</strong> {fada.episodios?.length || 0} aparições</p>
      </div>
    </div>
  );
};

export default FadaDetalhe;
