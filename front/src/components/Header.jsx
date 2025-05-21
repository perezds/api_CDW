import React from 'react';
import '../styles/Header.css';

const Header = () => {
  return (
    <header className="winx-header">
      <h1>Apwinx</h1>
      <nav>
        <a href="/">Início</a>
        <a href="/personagens">Personagens</a>
        <a href="/viloes">Vilões</a>
        <a href="/poderes">Poderes</a>
      </nav>
    </header>
  );
};

export default Header;
