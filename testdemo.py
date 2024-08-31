import gradio as gr
import os
import numpy as np
import streamlit as st
from scipy.io import wavfile

# 输入麦克风的音频，输出反向后的音频
def reverse_audio(audio_file):
    # 读取音频文件
    sample_rate, audio_data = wavfile.read(audio_file)
    
    # 反转音频数据
    reversed_audio_data = np.flipud(audio_data)
    
    # 创建一个新的 WAV 文件
    reversed_audio_file = "reversed_audio.wav"
    wavfile.write(reversed_audio_file, sample_rate, reversed_audio_data)
    
    return reversed_audio_file

# 创建一个 Streamlit 应用
st.title("音频反向应用")

# 创建一个上传组件用于上传音频文件
uploaded_audio = st.file_uploader("选择音频文件", type="wav")

# 如果用户上传了音频文件，则处理并显示反向后的音频
if uploaded_audio is not None:
    # 读取上传的音频文件
    reversed_audio_file = reverse_audio(uploaded_audio)
    
    # 显示反向后的音频文件
    st.audio(reversed_audio_file)
