import streamlit as st
import cv2
import numpy as np

# 假设的模型加载函数
def load_pretrained_model():
    # 加载你的预训练模型
    pass

# 假设的模型预测函数
def predict_sizes(image, model=None):
    # 预处理图片
    image_preprocessed = cv2.resize(image, (224, 224))
    
    # 使用模型进行预测
    #body_sizes = model.predict(image_preprocessed)
        # 加载图像
    img = cv2.imread('/root/liftrolu/test.png')

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 对图像进行边缘检测
    edges = cv2.Canny(gray, 100, 200)

    # 找到轮廓
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的轮廓
    max_contour = max(contours, key=cv2.contourArea)

    # 计算轮廓的周长
    perimeter = cv2.arcLength(max_contour, True)

    # 计算腰围
    waist = perimeter / 2

    # 在图像上绘制轮廓和腰围
    cv2.drawContours(img, [max_contour], -1, (0, 255, 0), 2)
    cv2.putText(img, 'Waist: {:.2f} cm'.format(waist), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 显示图像
    #cv2.imshow('Waist Measurement', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    
    # 返回预测的三围尺寸
    return waist

# 加载模型
#model = load_pretrained_model()

# 创建 Streamlit 应用
st.title("人体三围数据预测")

# 创建一个图像上传组件
uploaded_file = st.file_uploader("选择图片以预测三围数据", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 读取上传的图片
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # 显示原始图片
    st.image(image, channels="RGB")

    # 使用模型预测三围数据
    #body_sizes = predict_sizes(image, model)
    body_sizes = predict_sizes(image)

    # 显示预测结果
    st.write(f"胸围: {body_sizes[0]:.2f} 厘米")
    st.write(f"腰围: {body_sizes[1]:.2f} 厘米")
    st.write(f"臀围: {body_sizes[2]:.2f} 厘米")

    # 推荐衣服和裤子的尺寸
    # 这里需要一个规则或者算法来根据三围数据推荐尺寸
    # 示例推荐规则（需要根据实际数据调整）
    shirt_size = "M" if body_sizes[0] > 90 else "S"
    pants_size = "32" if body_sizes[1] > 80 else "28"
    st.write(f"推荐衣服尺寸: {shirt_size}")
    st.write(f"推荐裤子尺寸: {pants_size}")
