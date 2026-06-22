import { useEffect, useState } from 'react';
import { ActivityIndicator, FlatList, StyleSheet, Text, View } from 'react-native';
import { getTarefas } from '../services/api';

export default function TarefasScreen() {
  const [tarefas, setTarefas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    carregarTarefas();
  }, []);

  const carregarTarefas = async () => {
    try {
      setLoading(true);
      setError(null);
      const dados = await getTarefas();
      setTarefas(dados);
    } catch (err) {
      setError('Erro ao carregar tarefas. Verifique se o Django está rodando.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#007AFF" />
        <Text style={styles.loadingText}>Carregando tarefas...</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.center}>
        <Text style={styles.errorText}>{error}</Text>
      </View>
    );
  }

  const renderTarefa = ({ item }) => (
    <View style={styles.tarefaCard}>
      <Text style={styles.titulo}>{item.titulo || 'Sem título'}</Text>
      <Text style={styles.descricao} numberOfLines={2}>
        {item.descricao || 'Sem descrição'}
      </Text>
      {item.categoria && (
        <Text style={styles.categoria}>📁 {item.categoria}</Text>
      )}
      <View style={styles.footer}>
        <Text style={[styles.status, { color: item.concluida ? '#34C759' : '#FF9500' }]}>
          {item.concluida ? '✓ Concluída' : '⏳ Pendente'}
        </Text>
        {item.score_polaridade && (
          <Text style={styles.score}>Score: {item.score_polaridade.toFixed(2)}</Text>
        )}
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={tarefas}
        renderItem={renderTarefa}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.listContent}
        ListEmptyComponent={
          <Text style={styles.emptyText}>Nenhuma tarefa encontrada</Text>
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
  },
  listContent: {
    padding: 16,
  },
  tarefaCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  titulo: {
    fontSize: 16,
    fontWeight: '600',
    color: '#000',
    marginBottom: 8,
  },
  descricao: {
    fontSize: 14,
    color: '#666',
    marginBottom: 8,
    lineHeight: 20,
  },
  categoria: {
    fontSize: 12,
    color: '#007AFF',
    marginBottom: 8,
  },
  footer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: 8,
  },
  status: {
    fontSize: 12,
    fontWeight: '500',
  },
  score: {
    fontSize: 12,
    color: '#999',
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#666',
  },
  errorText: {
    fontSize: 14,
    color: '#FF3B30',
    textAlign: 'center',
    paddingHorizontal: 20,
  },
  emptyText: {
    textAlign: 'center',
    marginTop: 40,
    fontSize: 16,
    color: '#999',
  },
});
