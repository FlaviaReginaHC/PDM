import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="PetShop PRO",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "pets.csv"


IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1552053831-71594a27632d"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_PETS = (
    "https://images.unsplash.com/"
    "photo-1450778869180-41d0601e046e"
    "?auto=format&fit=crop&w=1200&q=85"
)


st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        linear-gradient(
            135deg,
            #F5EBDD 0%,
            #E8D2B5 50%,
            #D8B98C 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* SIDEBAR */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #3B2418,
            #5A3422
        );

    border-right:
        2px solid #C47A44;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #E7B887 !important;
    letter-spacing: 1px;
}


/* TÍTULOS */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #4A2C20 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #6B4A38 !important;
    margin-bottom: 30px;
}


/* HERO */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(70,40,20,0.25);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(55,32,22,0.97) 0%,
            rgba(70,40,25,0.86) 45%,
            rgba(70,40,25,0.18) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #E8A15A !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #F6E9D8 !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #B86635;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* CARDS */

.info-card {
    background: #FFF9F1;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(180,105,55,0.30);

    box-shadow:
        0 10px 25px rgba(80,45,25,0.10);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #4A2C20 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #75563F !important;

    margin-top: 5px;
}


/* CARD ESCURA */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #3A2419,
            #60402D
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(60,35,20,0.18);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #F0DFCC !important;
    line-height: 1.7;
}


/* FORMULÁRIO */

[data-testid="stForm"] {
    background:
        rgba(255,249,241,0.90);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #CDA77D;

    box-shadow:
        0 10px 30px rgba(80,45,25,0.10);
}


/* LABELS */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #4A2C20 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #3A2A22 !important;

    -webkit-text-fill-color:
        #3A2A22 !important;

    border:
        2px solid #B9825B !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #A4512B !important;

    box-shadow:
        0 0 0 3px rgba(164,81,43,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #806D5E !important;
    opacity: 1 !important;
}


/* SELECTBOX */

[data-baseweb="select"] > div {
    background-color: #5A4030 !important;

    border:
        2px solid #B9825B !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #D9965D !important;
}

[data-baseweb="popover"] {
    background-color: #5A4030 !important;
}

[data-baseweb="menu"] {
    background-color: #5A4030 !important;
}

[role="option"] {
    background-color: #5A4030 !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #8A5738 !important;

    color: #FFFFFF !important;
}


/* BOTÕES */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #A4512B,
            #C97942
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(150,75,40,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #873F22,
            #A95D31
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* TABELA */

[data-testid="stDataFrame"] {
    background: #FFF9F1;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #CDA77D;
}


/* RODAPÉ */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #72513B !important;

    font-size: 14px;

    font-weight: 600;
}


/* RESPONSIVIDADE */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==============================
# FUNÇÕES
# ==============================

def carregar_dados():

    colunas = [
        "Nome",
        "Espécie",
        "Idade",
        "Pelagem",
        "Raça",
        "Peso",
        "Serviço",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


df = carregar_dados()


colunas_necessarias = [
    "Nome",
    "Espécie",
    "Idade",
    "Pelagem",
    "Raça",
    "Peso",
    "Serviço",
    "Observações"
]


for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


df["Idade"] = pd.to_numeric(
    df["Idade"],
    errors="coerce"
).fillna(0)


df["Peso"] = pd.to_numeric(
    df["Peso"],
    errors="coerce"
).fillna(0)


# ==============================
# SIDEBAR
# ==============================

st.sidebar.markdown(
"""
<div class="logo-title">
🐾 PetShop
</div>

<div class="logo-subtitle">
CUIDADO E CARINHO PARA SEU PET
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Pet",
        "🐾 Pets Cadastrados"
    ]
)


st.sidebar.markdown("---")


st.sidebar.caption(
    "PetShop PRO • 2026"
)


# ==============================
# DASHBOARD
# ==============================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Seu pet.<br>
Seu cuidado.
</div>

<div class="hero-text">
Tenha todos os seus pets organizados em um único lugar.<br>
Cadastre, consulte e acompanhe as informações
de forma simples, rápida e especial.
</div>

<div class="hero-badge">
🐾 CUIDADO COM AMOR
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
"""
<div class="page-title">
📊 Visão geral dos seus pets
</div>

<div class="page-subtitle">
Acompanhe seus animais e mantenha tudo organizado.
</div>
""",
        unsafe_allow_html=True
    )


    total_pets = len(df)

    peso_total = df["Peso"].sum()

    total_servicos = len(
        df[df["Serviço"].astype(str).str.strip() != ""]
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🐶
</div>

<div class="card-number">
{total_pets}
</div>

<div class="card-label">
PETS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
⚖️
</div>

<div class="card-number">
{peso_total:,.1f} kg
</div>

<div class="card-label">
PESO TOTAL REGISTRADO
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
✂️
</div>

<div class="card-number">
{total_servicos}
</div>

<div class="card-label">
ATENDIMENTOS REGISTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
🐾 Cuidado especial
</h2>

<p>
O PetShop PRO permite manter todos os seus pets
organizados em um único lugar.
</p>

<p>
Cadastre, consulte, pesquise e acompanhe as informações
dos seus animais de maneira simples, moderna e prática.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_PETS,
            use_container_width=True
        )


# ==============================
# CADASTRAR PET
# ==============================

elif menu == "➕ Cadastrar Pet":

    st.markdown(
"""
<div class="page-title">
➕ Novo pet
</div>

<div class="page-subtitle">
Adicione um novo animal ao seu PetShop PRO.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_pet",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            nome = st.text_input(
                "🐾 Nome do pet"
            )


            especie = st.selectbox(
                "🐶 Espécie",
                [
                    "Cachorro",
                    "Gato",
                    "Coelho",
                    "Hamster",
                    "Ave",
                    "Outro"
                ]
            )


            idade = st.number_input(
                "🎂 Idade",
                min_value=0,
                max_value=50,
                value=1,
                step=1
            )


            pelagem = st.selectbox(
                "🎨 Pelagem",
                [
                    "Preta",
                    "Branca",
                    "Marrom",
                    "Caramelo",
                    "Cinza",
                    "Dourada",
                    "Mesclada",
                    "Outra"
                ]
            )


        with col2:

            raca = st.text_input(
                "🏷️ Raça"
            )


            peso = st.number_input(
                "⚖️ Peso (kg)",
                min_value=0.0,
                value=1.0,
                step=0.5
            )


            servico = st.selectbox(
                "✂️ Serviço",
                [
                    "Banho",
                    "Tosa",
                    "Banho e Tosa",
                    "Consulta",
                    "Vacinação",
                    "Higiene",
                    "Outro"
                ]
            )


            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR PET"
        )


    if cadastrar:

        if (
            nome.strip()
            and raca.strip()
        ):

            novo_pet = pd.DataFrame(
                [{
                    "Nome": nome.strip(),
                    "Espécie": especie,
                    "Idade": int(idade),
                    "Pelagem": pelagem,
                    "Raça": raca.strip(),
                    "Peso": float(peso),
                    "Serviço": servico,
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_pet
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🐾 Pet cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha o Nome e a Raça do pet."
            )


# ==============================
# PETS CADASTRADOS
# ==============================

elif menu == "🐾 Pets Cadastrados":

    st.markdown(
"""
<div class="page-title">
🐾 Meus pets
</div>

<div class="page-subtitle">
Consulte e pesquise todos os animais cadastrados.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🐾 Nenhum pet cadastrado
</h2>

<p>
Sua lista de pets ainda está vazia.
Cadastre seu primeiro animal para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar pet",
            placeholder="Digite nome, espécie, raça ou pelagem..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        opcoes_pets = df.index.tolist()


        pet_excluir = st.selectbox(
            "🗑️ Selecione um pet para excluir",
            options=opcoes_pets,
            format_func=lambda indice:
                f"{df.loc[indice, 'Nome']} "
                f"({df.loc[indice, 'Espécie']}) - "
                f"{df.loc[indice, 'Raça']}"
        )


        if st.button(
            "🗑️ EXCLUIR PET"
        ):

            df = df.drop(
                pet_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🐾 Pet excluído com sucesso!"
            )


            st.rerun()


# ==============================
# FOOTER
# ==============================

st.markdown(
"""
<div class="footer">

🐾 PetShop PRO<br>
Cuidado e carinho para seu pet

</div>
""",
    unsafe_allow_html=True
        )
