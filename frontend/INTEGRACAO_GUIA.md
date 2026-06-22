# 🚀 Guia de Integração Frontend + Backend

## Pré-requisitos
- Python 3.8+ instalado
- Node.js instalado
- Django rodando em `http://localhost:8000`

---

## ⚙️ Passo 1: Configurar e rodar o Backend (Django)

### 1.1 Abra um terminal e vá para a pasta do Django
```bash
cd C:\Users\ALUNO\Desktop\APIDJANGO
```

### 1.2 Ative o ambiente virtual
```bash
.\venv\Scripts\activate
```

### 1.3 Rode as migrações (se necessário)
```bash
python manage.py migrate
```

### 1.4 Inicie o servidor Django
```bash
python manage.py runserver
```

Você deve ver algo como:
```
Starting development server at http://127.0.0.1:8000/
```

✅ **Django rodando em `http://localhost:8000`**

---

## 📱 Passo 2: Configurar e rodar o Frontend (Expo)

### 2.1 Abra outro terminal e vá para a pasta do app
```bash
cd c:\Users\ALUNO\Desktop\aula22_06
```

### 2.2 Instale as dependências
```bash
npm install
```

### 2.3 Inicie o Expo
```bash
npx expo start
```

Você verá um QR code no terminal. Escolha uma opção:
- **Web**: Pressione `w`
- **Android**: Pressione `a` (precisa de Android Studio ou emulador)
- **iOS**: Pressione `i` (somente Mac)

---

## 🔌 Passo 3: Testar a Integração

### No app:
1. Se for web, ele abrirá automaticamente em `http://localhost:8081`
2. Navegue para a tela de tarefas (ou importe o `TarefasScreen.jsx`)
3. Você deve ver as tarefas do Django carregando

### Se não funcionar:
- **Erro de conexão**: Verifique se Django está rodando (`http://localhost:8000`)
- **CORS**: Já está configurado no Django ✅
- **Firewall**: Pode estar bloqueando a conexão

---

## 🔧 Usar a API em suas telas

### Importar e usar:
```jsx
import { getTarefas, criarTarefa } from '../services/api';

// Buscar tarefas
const tarefas = await getTarefas();

// Criar tarefa
await criarTarefa({
  titulo: 'Minha tarefa',
  descricao: 'Descrição',
  categoria: 1,
});
```

---

## 📡 Mudar URL da API para outro IP/Porta

Se está usando em device físico, edite `src/services/api.js`:

```javascript
// Para acessar do seu PC na rede
const API_BASE_URL = 'http://192.168.1.100:8000/api'; // use seu IP
```

Para descobrir seu IP:
```bash
ipconfig  # Windows
# ou
ifconfig  # Mac/Linux
```

---

## 🛑 Parar os servidores

- **Django**: Pressione `Ctrl + C` no terminal do Django
- **Expo**: Pressione `Ctrl + C` no terminal do Expo

---

## 📝 Endpoints Disponíveis

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/api/tarefas/` | GET, POST | Listar/criar tarefas |
| `/api/tarefas/{id}/` | PUT, DELETE | Atualizar/deletar tarefa |
| `/api/categorias-box/` | GET | Listar categorias |
| `/api/estudantes/` | GET | Listar estudantes |
| `/api/cursos/` | GET | Listar cursos |
| `/api/boxes/` | GET, POST | Listar/criar boxes |
| `/api/recomendacoes/` | GET | Listar recomendações |
| `/api/estatisticas/boxes/` | GET | Estatísticas dos boxes |

---

## ✨ Próximos passos

1. Criar telas adicionais (Cursos, Estudantes, Estatísticas)
2. Adicionar autenticação
3. Implementar funcionalidades CRUD completas
4. Deploy para produção

---

Qualquer dúvida, é só chamar! 🚀
