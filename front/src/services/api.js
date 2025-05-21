import axios from "axios";

const apiUrl = "http://localhost:8000/api/v1/episodios/episodios"; 

export const getEpisodios = async () => {
  try {
    const response = await axios.get(apiUrl);
    return response.data;
  } catch (error) {
    console.error("Erro ao obter episódios", error);
    throw error;
  }
};

export const createEpisodio = async (episodio) => {
  try {
    const response = await axios.post(apiUrl, episodio);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar episódio", error);
    throw error;
  }
};
