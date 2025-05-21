import React, { useEffect, useState } from "react";
import { getEpisodios } from "../api/api";
import "../styles/Episodios.css"; // Importando o CSS global

const Episodios = () => {
  const [episodios, setEpisodios] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchEpisodios = async () => {
      try {
        const data = await getEpisodios();
        setEpisodios(data);
      } catch (error) {
        console.error("Erro ao buscar episódios:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchEpisodios();
  }, []);

  if (loading) return <p className="loading">Carregando episódios...</p>;

  return (
    <div className="episodios-container">
      {episodios.map((ep) => (
        <div key={ep.id} className="episodio-card">
          <h2 className="episodio-title">{ep.nome}</h2>
          <p className="episodio-info">Número: {ep.numero}</p>
          <p className="episodio-info">Temporada: {ep.temporada}</p>
          <p className="episodio-sinopse">{ep.sinopse}</p>
        </div>
      ))}
    </div>
  );
};

export default Episodios;
