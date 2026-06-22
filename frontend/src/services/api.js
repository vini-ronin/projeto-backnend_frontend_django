import Constants from 'expo-constants';
import { Platform } from 'react-native';

const getApiBaseUrl = () => {
  if (process.env.EXPO_PUBLIC_API_URL) {
    return process.env.EXPO_PUBLIC_API_URL.replace(/\/$/, '');
  }

  if (Platform.OS === 'web' && globalThis.location?.hostname) {
    return `http://${globalThis.location.hostname}:8000/api`;
  }

  const expoHost = Constants.expoConfig?.hostUri?.split(':')[0];
  const host = expoHost || (Platform.OS === 'android' ? '10.0.2.2' : 'localhost');

  return `http://${host}:8000/api`;
};

export const API_BASE_URL = getApiBaseUrl();

const fetchAPI = async (endpoint, method = 'GET', data = null) => {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: data ? JSON.stringify(data) : undefined,
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Erro ${response.status}: ${errorText || response.statusText}`);
    }

    if (response.status === 204) {
      return null;
    }

    return await response.json();
  } catch (error) {
    console.error('Erro na API:', error);
    throw error;
  }
};

export const getTarefas = async () => {
  return fetchAPI('/tarefas/');
};

export const criarTarefa = async (tarefa) => {
  return fetchAPI('/tarefas/', 'POST', tarefa);
};

export const atualizarTarefa = async (id, tarefa) => {
  return fetchAPI(`/tarefas/${id}/`, 'PUT', tarefa);
};

export const deletarTarefa = async (id) => {
  return fetchAPI(`/tarefas/${id}/`, 'DELETE');
};

export const getCategorias = async () => {
  return fetchAPI('/categorias-box/');
};

export const getEstudantes = async () => {
  return fetchAPI('/estudantes/');
};

export const getEstudante = async (id) => {
  return fetchAPI(`/estudantes/${id}/`);
};

export const getCursos = async () => {
  return fetchAPI('/cursos/');
};

export const getBoxes = async () => {
  return fetchAPI('/boxes/');
};

export const criarBox = async (box) => {
  return fetchAPI('/boxes/', 'POST', box);
};

export const getEstatisticasBoxes = async () => {
  return fetchAPI('/estatisticas/boxes/');
};

export const getRecomendacoes = async () => {
  return fetchAPI('/recomendacoes/');
};

export default {
  API_BASE_URL,
  getTarefas,
  criarTarefa,
  atualizarTarefa,
  deletarTarefa,
  getCategorias,
  getEstudantes,
  getEstudante,
  getCursos,
  getBoxes,
  criarBox,
  getEstatisticasBoxes,
  getRecomendacoes,
};
