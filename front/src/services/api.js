import axios from "axios";

<<<<<<< HEAD
const apiUrl = "http://localhost:8000/api/v1/episodios/episodios"; 
=======
const apiUrl = "http://localhost:8000/episodios"; 
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed

export const getEpisodios = async () => {
  try {
    const response = await axios.get(apiUrl);
    return response.data;
  } catch (error) {
    console.error("Erro ao obter episódios", error);
<<<<<<< HEAD
    throw error;
  }
};

=======
  }
};


>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
export const createEpisodio = async (episodio) => {
  try {
    const response = await axios.post(apiUrl, episodio);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar episódio", error);
<<<<<<< HEAD
    throw error;
=======
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
  }
};
