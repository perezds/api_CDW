import React from 'react';
import { useNavigate } from 'react-router-dom';
import './WinxCarrossel.css';

const winxFadas = [
  { nome: 'Bloom', imagem: '/images/bloom.jpg' },
  { nome: 'Flora', imagem: '/images/flora.webp' },
  { nome: 'Stella', imagem: '/images/stella.jpg' },
  { nome: 'Musa', imagem: '/images/musa.jpg' },
  { nome: 'Tecna', imagem: '/images/tecnajpg.jpg' },
  { nome: 'Aisha', imagem: '/images/aisha.webp' },
];

const WinxCarousel = () => {
  const navigate = useNavigate(); // <- agora sim, correto!

  return (
    <div className="carousel-container">
      {winxFadas.map((fada, index) => (
        <div
          key={index}
          className="fada-card"
          onClick={() => navigate(`/fada/${fada.nome.toLowerCase()}`)}
          style={{ cursor: 'pointer' }}
        >
          <img src={fada.imagem} alt={fada.nome} />
          <h3>{fada.nome}</h3>
        </div>
      ))}
    </div>
  );
};

export default WinxCarousel;
