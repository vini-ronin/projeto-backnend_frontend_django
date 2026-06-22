import React, { useEffect, useState } from 'react';
import { ActivityIndicator, Image, StyleSheet, Text, View } from 'react-native';
import { API_BASE_URL, getEstudantes } from '../services/api';

export default function Index() {
  const [estudante, setEstudante] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let mounted = true;

    const carregarEstudante = async () => {
      try {
        const estudantes = await getEstudantes();
        if (mounted) {
          setEstudante(estudantes?.[0] ?? null);
          setError(null);
        }
      } catch (err) {
        console.log('Erro de conexao com a API:', err);
        if (mounted) {
          setError('Nao foi possivel conectar ao Django. Verifique se o backend esta rodando.');
        }
      } finally {
        if (mounted) {
          setLoading(false);
        }
      }
    };

    carregarEstudante();

    return () => {
      mounted = false;
    };
  }, []);

  const renderContent = () => {
    if (loading) {
      return (
        <View style={styles.feedback}>
          <ActivityIndicator color="#ffffff" />
          <Text style={styles.feedbackText}>Conectando ao Django...</Text>
        </View>
      );
    }

    if (error) {
      return <Text style={styles.errorText}>{error}</Text>;
    }

    if (!estudante) {
      return <Text style={styles.feedbackText}>Nenhum estudante cadastrado na API.</Text>;
    }

    return (
      <>
        <Info label="Nome" value={estudante.nome} />
        <Info label="CPF" value={estudante.cpf} />
        <Info label="E-mail" value={estudante.email} />
        <Info label="Celular" value={estudante.celular} />
      </>
    );
  };

  return (
    <View style={styles.container}>
      <Image source={require('./long.png')} style={styles.logo} resizeMode="contain" />

      <View style={styles.actions}>
        <Text style={styles.title}>Backend conectado</Text>
        <Text style={styles.apiUrl}>{API_BASE_URL}</Text>
        {renderContent()}
      </View>
    </View>
  );
}

function Info({ label, value }) {
  return (
    <View style={styles.textContainer}>
      <Text style={styles.label}>{label}</Text>
      <Text style={styles.text}>{value || '-'}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#021123',
    padding: 24,
  },
  logo: {
    width: 220,
    height: 110,
    marginBottom: 24,
  },
  actions: {
    width: '100%',
    maxWidth: 420,
    gap: 16,
    paddingVertical: 24,
    paddingHorizontal: 24,
    backgroundColor: '#14448080',
    borderRadius: 24,
    borderWidth: 2,
    borderColor: '#144480',
  },
  title: {
    color: '#ffffff',
    fontSize: 22,
    fontWeight: '700',
  },
  apiUrl: {
    color: '#88a1c4',
    fontSize: 12,
    marginBottom: 4,
  },
  feedback: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  feedbackText: {
    color: '#ffffff',
    fontSize: 15,
    lineHeight: 22,
  },
  errorText: {
    color: '#ffb3b3',
    fontSize: 15,
    lineHeight: 22,
  },
  textContainer: {
    gap: 6,
  },
  label: {
    color: '#88a1c4',
    fontSize: 13,
    fontWeight: '700',
  },
  text: {
    minHeight: 44,
    paddingHorizontal: 14,
    paddingVertical: 12,
    color: '#ffffff',
    borderRadius: 10,
    backgroundColor: '#0b2546',
  },
});
