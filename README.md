# AS05: Assistente Conversacional Baseado em LLM
Um app em Streamlit que permite fazer perguntas sobre o conteúdo de arquivos PDF, retornando trechos relevantes usando modelos de linguagem e embeddings.
## Como funciona
1. O usuário faz upload de um PDF;
2. O texto do PDF é lido e dividido em trechos menores (chunks);
3. Cada trecho é convertido em embeddings BERT (modelo sentence-transformers/all-MiniLM-L6-v2);
4. É criada uma base vetorial local usando FAISS para busca rápida;
5. O usuário digita sua pergunta;
6. O sistema faz uma busca semântica e exibe os trechos mais relevantes do PDF.

## Como rodar localmente
1. Clone ou baixe este repositório;
2. Instale dependências:
   pip install -r requirements.txt
4. Rode usando:
   streamlit run app.py

## Dependências:
- streamlit: interface web interativa
- langchain: carregamento e divisão do PDF
- sentence-transformers: geração de embeddings
- faiss: banco vetorial para busca semântica

## Link do app
[Link para a aplicação em funcionamento](https://assistentellm-c4ryuvobkuh2bhekspb3xu.streamlit.app)
## Link do GitHub
[Link para o github](https://github.com/LeticiaBianca/AssistenteLLM)