import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './FadaDetalhe.css';

const FadaDetalhe = () => {
  const { nome } = useParams();
  const [fada, setFada] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/fada/${nome}`)
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
