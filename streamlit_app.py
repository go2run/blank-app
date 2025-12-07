import streamlit as st
from st_audiorec import st_audiorec


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    **There's :rainbow[so much] you can build!**

    * [about-code-owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
    * [codespaces](https://github.com/codespaces)
    """
)

_ = st.button("Send balloons!") and st.balloons()

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
   st.audio(wav_audio_data, format='audio/wav')