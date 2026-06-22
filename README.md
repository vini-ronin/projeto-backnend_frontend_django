# Projeto Front + Backend

Esta pasta tem duas partes:

- `frontend`: app Expo/React Native.
- `backend`: API Django.

## Rodar o backend

```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

A API fica em `http://127.0.0.1:8000/api/`.

## Rodar o frontend

Abra outro terminal:

```powershell
cd frontend
npm install
npx expo start --web
```

Se o Expo abrir em outra porta, confira se ela esta liberada no `backend/setup/settings.py` em `CORS_ALLOWED_ORIGINS`.
