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
  const navigate = useNavigate();

  return (
    <div className="carousel-page">
      <h1 className="carousel-title">✨ Bem-vinda ao Universo Winx ✨</h1>
      <p className="carousel-subtitle">Escolha sua fada favorita e explore seus poderes mágicos!</p>
      <div className="carousel-grid">
        {winxFadas.map((fada, index) => (
          <div
            key={index}
            className="fada-card"
            onClick={() => navigate(`/fada/${fada.nome.toLowerCase()}`)}
          >
            <div className="fada-img-container">
              <img src={fada.imagem} alt={fada.nome} />
            </div>
            <h3>{fada.nome}</h3>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WinxCarousel;
