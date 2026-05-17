import streamlit as st

# --- USUÁRIO FIXO (simples) ---
USUARIO = "joao victor"
SENHA = "31072006"

# --- FUNÇÃO DE LOGIN ---
def login():
    st.title("🔐 Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == USUARIO and senha == SENHA:
            st.session_state["logado"] = True
        else:
            st.error("Usuário ou senha incorretos")

# --- DADOS ---
alunos = [
    ("Joao", 7, 8),
    ("Maria", 6, 5),
    ("Pedro", 9, 10),
    ("Ana", 4, 6),
    ("Lucas", 8, 7),
    ("Julia", 5, 5),
    ("Carlos", 10, 9),
    ("Mariana", 6, 7),
    ("Gabriel", 3, 4),
    ("Larissa", 8, 8),
    ("Rafael", 7, 6),
    ("Beatriz", 9, 9),
    ("Bruno", 2, 5),
    ("Camila", 6, 6),
    ("Felipe", 10, 10),
    ("Isabela", 5, 7),
    ("Gustavo", 8, 9),
    ("Amanda", 4, 5),
    ("Diego", 7, 7),
    ("Leticia", 6, 8),
    ("Rodrigo", 9, 6),
    ("Fernanda", 3, 3),
    ("Eduardo", 8, 7),
    ("Patricia", 5, 6),
    ("Thiago", 7, 9),
    ("Vanessa", 10, 8),
    ("Leonardo", 4, 4),
    ("Aline", 6, 7),
    ("Matheus", 9, 10),
    ("Carolina", 5, 8)
]

# --- INICIALIZA ESTADO ---
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# --- CONTROLE ---
if not st.session_state["logado"]:
    login()
else:
    st.title("📊 Sistema de Alunos")

    aprovados = []
    reprovados = []

    for nome, n1, n2 in alunos:
        media = (n1 + n2) / 2
        
        if media >= 7:
            aprovados.append((nome, media))
        else:
            reprovados.append((nome, media))

    opcao = st.sidebar.selectbox(
        "Ver:",
        ["Todos", "Aprovados", "Reprovados"]
    )

    if opcao == "Todos":
        for nome, n1, n2 in alunos:
            media = (n1 + n2) / 2
            status = "Aprovado" if media >= 7 else "Reprovado"
            st.write(f"{nome} - Média: {media:.1f} - {status}")

    elif opcao == "Aprovados":
        st.subheader("Aprovados ✅")
        for nome, media in aprovados:
            st.write(f"{nome} - {media:.1f}")

    elif opcao == "Reprovados":
        st.subheader("Reprovados ❌")
        for nome, media in reprovados:
            st.write(f"{nome} - {media:.1f}")

    # botão logout
    if st.sidebar.button("Sair"):
        st.session_state["logado"] = False