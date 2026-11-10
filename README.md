# Closetiq — protótipo de combinação de roupas

Protótipo local com backend FastAPI e interface HTML. O endpoint `POST /generate-look` combina peças de roupa e calcula uma pontuação básica de compatibilidade de cores.

## Estrutura

- `backend/app/main.py`: cria a aplicação FastAPI.
- `backend/app/routes/look_routes.py`: demonstração do endpoint.
- `backend/app/services/`: combinação e pontuação.
- `frontend/index.html`: botão para chamar a API.

## Executar o backend

Requer Python 3.10+ e pip. Dependências Python registradas em `requirements.txt` (Python 3.10+):

```sh
python -m pip install -r requirements.txt
cd backend
python -m uvicorn app.main:app --reload
```

A documentação interativa fica em `http://127.0.0.1:8000/docs`. Para abrir a interface, sirva `frontend/` em outro terminal:

```sh
cd frontend
python -m http.server 5500
```

A interface atual tenta chamar `http://localhost:8000`; o backend não configura CORS. O navegador pode bloquear essa chamada entre origens, então a interface ainda precisa de configuração de origem antes de funcionar como demonstração web. O endpoint funciona apenas com um conjunto fixo de quatro peças e não recebe dados do usuário.

## Limitações conhecidas

- `desired_style` é aceito pelo motor, mas não influencia a pontuação.
- Temperatura só acrescenta pontos acima de 25 °C; não muda recomendações de peças.
- Não há validação de entrada, persistência, testes ou tratamento de erros da interface.
- Não há licença definida nem dependência de desenvolvimento registrada.
