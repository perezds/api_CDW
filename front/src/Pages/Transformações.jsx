import React, { useEffect, useState } from 'react';

const Transformacoes = () => {
    const [transformacoes, setTransformacoes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [erro, setErro] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/transformacoes')
            .then(response => {
                if (!response.ok) throw new Error('Erro ao buscar transformações');
                return response.json();
            })
            .then(data => {
                setTransformacoes(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setErro('A magia falhou... tente de novo mais tarde 🧙‍♀️');
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p>Carregando transformações...</p>;
    }

    if (erro) {
        return <p>{erro}</p>;
    }

    return (
        <div>
            <h1>Transformações</h1>
            <ul>
                {transformacoes.map((transformacao, index) => (
                    <li key={index}>{transformacao.nome}</li>
                ))}
            </ul>
        </div>
    );
};

export default Transformacoes;
