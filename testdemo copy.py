
import os
import streamlit as st
from PIL import Image

# 输入一张图片，旋转45°后输出
def image_mod(image):
    return image.rotate(45)

# 创建一个 Streamlit 应用
st.title("图片旋转应用")

# 创建一个上传组件用于上传图片
uploaded_file = st.file_uploader("选择图片", type="jpg")

# 如果用户上传了图片，则处理并显示旋转后的图片
if uploaded_file is not None:
    # 读取上传的图片
    image = Image.open(uploaded_file)
    
    # 处理图片
    rotated_image = image.rotate(45)
    
    # 显示旋转后的图片
    st.image(rotated_image)
