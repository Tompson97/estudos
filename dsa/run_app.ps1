Set-Location "C:\Users\tomps\OneDrive\Documentos\GitHub\Material de estudo\estudos\dsa\"

# 1. Define o caminho do script de ativação
$venvPath = "C:\Users\tomps\OneDrive\Documentos\GitHub\Material de estudo\estudos\dsa\venv\scripts\Activate.ps1"

# 2. Ativa o ambiente virtual
Write-Host "Ativando o ambiente virtual..." -ForegroundColor Cyan
& $venvPath

# 3. Executa o Streamlit
Write-Host "Iniciando o Streamlit..." -ForegroundColor Green
streamlit run dsa_assistente.py