import cv2
import numpy as np
import mediapipe as mp
import streamlit as st

def detect_keypoints(image):
    # 这里应该包含使用你的预训练模型检测关键点的代码
    # 例如，你可以使用 OpenPose 或其他人体姿态估计库
    # 初始化 MediaPipe 人体姿态估计模型
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False,
                    model_complexity=1,
                    smooth_landmarks=True)

    # 加载图像
    #image = cv2.imread('path_to_your_image.jpg')

    # 使用 MediaPipe 检测关键点
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # 获取关键点
    landmarks = results.pose_landmarks
    return landmarks
def draw_keypoints(image,landmarks):
    mp_pose = mp.solutions.pose
    # 绘制关键点
    if landmarks:
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(image, landmarks, mp_pose.POSE_CONNECTIONS)
    # # 保存图片
    # output_path = 'path_to_save_image.jpg'
    # cv2.imwrite(output_path, image)
    return image

  

def calculate_measurements(landmarks):
    # 根据关键点计算三围尺寸
    # 这里应该包含计算三围尺寸的代码
    # 示例：
    # 胸围：肩膀点（16, 18）
    # 腰围：腰部点（27）
    # 臀围：臀部点（28, 30）
    # 胸围：肩膀点（11, 12）
    # 腰围：腰部点（23,24）
    # 臀围：臀部点（25, 26）
    chest_width = np.linalg.norm(landmarks.landmark[11].x - landmarks.landmark[12].x)
    #waist_width = np.linalg.norm(landmarks.landmark[27].x - (landmarks.landmark[16].x + landmarks.landmark[18].x) / 2)
    waist_width = np.linalg.norm(landmarks.landmark[23].x -landmarks.landmark[24].x)
    # 23 ,24
    hips_width = np.linalg.norm(landmarks.landmark[26].x - landmarks.landmark[25].x)

    return chest_width, waist_width, hips_width



# 创建 Streamlit 应用
st.title("人体三围数据预测衣服尺码")
# 创建一个性别选择的下拉菜单
gender = st.selectbox('请选择您的性别', ('男', '女'))

# 创建一个身高输入框
height = st.number_input('请输入您的身高（厘米）', min_value=50, max_value=300, value=170)

# 定义一个函数，根据腰围、臀围和身高推荐裤子尺码
def recommend_pants_size(waist, hips, height):
    # 假设尺码系统为：S, M, L, XL, XXL
    sizes = ['S', 'M', 'L', 'XL', 'XXL']
    
    # 根据身高推荐尺码范围
    if height < 160:
        size_range = [0, 1]  # S, M
    elif height < 170:
        size_range = [1, 2]  # M, L
    elif height < 180:
        size_range = [2, 3]  # L, XL
    else:
        size_range = [3, 4]  # XL, XXL
    
    # 根据腰围和臀围确定尺码
    if waist < 76:
        waist_size = 0
    elif waist < 81:
        waist_size = 1
    elif waist < 86:
        waist_size = 2
    elif waist < 91:
        waist_size = 3
    else:
        waist_size = 4
    
    if hips < 91:
        hips_size = 0
    elif hips < 96:
        hips_size = 1
    elif hips < 101:
        hips_size = 2
    elif hips < 106:
        hips_size = 3
    else:
        hips_size = 4
    
    # 选择腰围和臀围尺码中的较大值，并在身高推荐范围内确定最终尺码
    final_size = max(waist_size, hips_size)
    final_size = sizes[max(size_range[0], min(final_size, size_range[1]))]
    
    return final_size
# 显示用户选择的性别
#st.write('您选择的性别是：', gender)
# 创建一个图像上传组件
uploaded_file = st.file_uploader("选择图片以预测三围数据", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 读取上传的图片
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # 显示原始图片
    #st.image(image, channels="RGB")

    # 使用模型检测关键点
    keypoints = detect_keypoints(image)

   

    # 计算三围尺寸
    measurements = calculate_measurements(keypoints)

    # #绘制后的关键点图
    new_image=draw_keypoints(image,keypoints)
    st.image(new_image, channels="RGB")
    #st.image(image, channels="RGB")
    if gender=='男':
        value=600
    else:
        value=400


    # 显示预测结果
    # st.write(f"胸围: {measurements[0]*value:.2f} 厘米")
    # st.write(f"腰围: {measurements[1]*value:.2f} 厘米")
    # st.write(f"臀围: {measurements[2]*value:.2f} 厘米")
    #肩宽
    shoulder_width=measurements[0]*value
    #胸围
    chest=measurements[1]*value
    #腰围
    waist=measurements[2]*value
    hips=measurements[2]*value
    # 推荐衣服尺寸
    # 这里需要一个规则或者算法来根据三围数据推荐尺寸
    # 示例推荐规则（需要根据实际数据调整）
    shirt_size="S"
    if gender=='男':
        if shoulder_width <= 42 and chest <= 85  and waist <= 75 and height<=167:
            shirt_size="S"
        elif shoulder_width <= 44 and chest <= 89  and waist <= 79 and height<=172:
            shirt_size="M"
        elif shoulder_width <= 46 and chest <= 93  and waist <= 84 and height<=177:
            shirt_size="L"
        elif shoulder_width <= 48 and chest <= 97  and waist <= 88 and height<=182:
            shirt_size="XL"
        elif shoulder_width <= 50 and chest <= 102  and waist <= 92 and height<=187:
            shirt_size="XXL"
        elif shoulder_width <= 52 and chest <= 107  and waist <= 96 and height<=190:
            shirt_size="XXXL"
        

    pants_size=recommend_pants_size(waist, hips, height)

    # shirt_size = "M" if measurements[0]*value > 90 else "S"
    # pants_size = "32" if measurements[1]*value > 80 else "28"
    st.write(f"推荐衣服尺寸: {shirt_size}")
    st.write(f"推荐裤子尺寸: {pants_size}")
    # scp -o StrictHostKeyChecking=no -r -P 46389 C:\Users\moyam\Desktop\R-C.jpg root@ssh.intern-ai.org.cn:/root/liftrolu
