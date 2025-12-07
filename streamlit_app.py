import streamlit as st
from st_audiorec import st_audiorec

st.title("🎈 My new app")
st.write('''
         我想我以後會更加了解這個框架。
         
         而今天會是個好的開始。
         
         而且每一次部署都會是直接的自動化更新。

         所以我很期待。

         😂
''')
wav_audio_data = st_audiorec()
if wav_audio_data is not None:
   st.audio(wav_audio_data, format='audio/wav')