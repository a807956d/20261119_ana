import streamlit as st

def analyze_sentiment(text):
    """
    純本機情緒分析函數
    """
    text_clean = text.strip().lower()
    
    # 優先判定：5分 (強烈正面)
    if any(word in text_clean for word in ["太棒", "非常棒", "超級好用", "極度推薦", "完美", "超讚", "極推薦", "無挑剔"]):
        return 5
    # 優先判定：1分 (強烈負面)
    elif any(word in text_clean for word in ["糟糕", "垃圾", "氣死了", "極度不滿", "非常差", "爛", "詐騙", "別買"]):
        return 1
    # 優先判定：2分 (一般負面)
    elif any(word in text_clean for word in ["不好用", "不滿意", "失望", "不推", "不建議", "差勁"]):
        return 2
    # 優先判定：3分 (中立/普通/勉勉強強)
    elif any(word in text_clean for word in ["還可以", "還算", "普通", "一般般", "勉勉強強", "過得去", "差不多", "沒感覺", "值得一試"]):
        return 3
    # 判定：4分 (一般正面)
    elif any(word in text_clean for word in ["不錯", "滿意", "好用", "好", "棒", "值得"]):
        return 4
    # 預設值
    else:
        return 3

# Streamlit 網頁版面設定
st.set_page_config(page_title="中文產品評論情緒分析器", page_icon="📊", layout="centered")

st.title("📊 中文產品評論情緒分析器")
st.write("請在下方輸入產品使用評論，系統將會為您評估 1 至 5 等級的情緒分數。")

# 文字輸入框
user_input = st.text_area("輸入評論內容：", placeholder="例如：這款產品真的太棒了，質感很好！")

# 按下分析按鈕
if st.button("開始分析", type="primary"):
    if user_input.strip():
        # 進行情緒分析
        score = analyze_sentiment(user_input)
        
        # 呈現結果
        st.subheader("分析結果")
        
        # 呈現視覺化評價與星星星星
        stars = "⭐" * score
        st.success(f"預測評分： {score} / 5 分")
        st.subheader(stars)
        
        # 評語說明
        explanations = {
            1: "🔴 非常差 (極度不滿)",
            2: "🟠 差 (不滿意)",
            3: "🟡 普通 (中立或還可以)",
            4: "🟢 好 (滿意)",
            5: "🔵 非常好 (極度推薦)"
        }
        st.info(f"狀態說明：{explanations[score]}")
    else:
        st.warning("請先輸入一些文字內容再進行分析！")
