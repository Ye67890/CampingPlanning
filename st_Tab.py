import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

page_title = '去露營:tent:'
st.set_page_config(page_title=page_title, page_icon=':star', layout='wide')
st.title(page_title)

# st.title("去露營:tent:")

tab_titles = [
    "路程與行程規劃",
    "需帶物品",
    "採買商品",
    "當天天氣",
    "露營地位置"
]
tabs = st.tabs(tab_titles)

with tabs[0]:
    st.write("時間：**11/12 (六) & 11/13 (日)**")
    st.write("地點：[苗栗南庄 林泉休閒露營區](https://m.easycamp.com.tw/store/store_index/899/6484)")
    st.header("路程")
    st.components.v1.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d463495.51697212394!2d120.9384695240214!3d24.827665215564725!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x34685229d2f95afb%3A0x2bc56149f2c170e8!2z5Y2X5bqE5p6X5rOJ6Zyy54ef5Y2AIDM1M-iLl-agl-e4o-WNl-W6hOmEieWNl-axn-adkTE36YSwMzDomZ8!3m2!1d24.5721615!2d120.9870686!4m5!1s0x3442a9727d969f51%3A0xd0f3033a81203ed2!2z5Y-w5YyX5biC5Lit5q2j5Y2A5om_5b636Lev5LiA5q615Y-w5YyX6LuK56uZ!3m2!1d25.0476133!2d121.5174062!5e0!3m2!1szh-TW!2stw!4v1667203376988!5m2!1szh-TW!2stw",
                            width=350, height = 650, scrolling = False)
    st.header("行程規劃")
    st.subheader("Day1 (11/12)")
    # st.markdown("##### 早上")
    st.write("**07:00** 起床刷牙")
    st.write("**09:00** 從台北出發")
    # st.info("可討論採買要在**台北**就買好或是**竹南**，如果要去苗栗採買的話可能會不順，如下圖。")
    # st.write("竹南有[家樂福超市](https://goo.gl/maps/SeWr9uHwkofMtgZp9)和[全聯](https://goo.gl/maps/dNZQh7VsmpBZKijP8)")
    # st.components.v1.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d116079.70274301819!2d120.82658283137062!3d24.606766593247396!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x3469abf6b5599595%3A0xbec729c5d3094400!2z6IuX5qCXIDM2MOiLl-agl-e4o-iLl-agl-W4gg!3m2!1d24.563166499999998!2d120.81853849999999!4m5!1s0x34685229d2f95afb%3A0x2bc56149f2c170e8!2z6IuX5qCX57ij5Y2X5bqE6YSJ5Y2X5rGf5p2RMTfphLDljZfluoTmnpfms4npnLLnh5_ljYA!3m2!1d24.5721615!2d120.9870686!5e0!3m2!1szh-TW!2stw!4v1667205635666!5m2!1szh-TW!2stw",
    #                         width=350, height=650, scrolling=False)
    st.write("預計**10:30**到竹南 (車程約90分鐘)")
    st.markdown("##### 午餐")
    st.write("[香香意麵](https://goo.gl/maps/cDW3imxQ8KZqhMJR9) (對面有停車場！)")
    st.write("**飲料**")
    st.markdown("- [岩語茶Yan Yu Cha 竹南華東店](https://goo.gl/maps/Q2CxDHUwHYLuWQqY9)")
    st.markdown("- [喜力茶飲 苗栗竹南店](https://goo.gl/maps/6g1NNBy96wKD7b699)")
    st.markdown("- [泰個奶熊](https://goo.gl/maps/sZkYyjELD4BhFnyi9)")
    st.markdown("- [穩飲茶府-竹南總府](https://goo.gl/maps/bs71MfPszwohcy3w7)")
    st.markdown("- [七盞茶 竹南光復店](https://goo.gl/maps/73xpNfCkY7Aw9np69)")

    st.write("吃飽後去[家樂福超市](https://goo.gl/maps/SeWr9uHwkofMtgZp9)或[全聯](https://goo.gl/maps/dNZQh7VsmpBZKijP8)採買")
    st.write("採買完後前往營地")
    # st.write("吃飽後可去[蘆竹湳古厝](https://goo.gl/maps/t1bzkseSL9XRwuR56)走走，"
    #          "結束後就去營地。")
    st.write("搭建帳篷")
    st.write("吸收芬多精")
    st.write("抓猴子")
    st.write("吃飯")
    st.write("玩耍")
    st.write("洗澡")
    st.write("刷牙")
    st.write("睡覺")

    st.subheader("Day2 (11/13)")
    st.write("**5:00**被冷醒")
    st.write("**7:00**阿噗蹲馬桶")
    st.write("**8:00**起床刷牙")
    st.write("**烤土司、煎雞蛋**")
    st.write("發呆")
    st.write("收帳篷")
    st.write("開心下山")
    st.write("看要幹嘛")


with tabs[1]:
    st.header("需帶物品")
    st.write("### 勁伸")
    st.write("睡袋(棉被、枕頭)", ", 個人盥洗用品", ", 碗筷", ", 刀子", ", 防蚊液", ", 桌遊")
    st.write("### 健珉")
    st.write("##### 露營器具")
    st.checkbox("睡袋(棉被、枕頭)x2")
    st.checkbox("帳篷x2")
    st.checkbox("睡墊x6")
    st.checkbox("卡式爐")
    st.checkbox("折疊桌")
    st.checkbox("椅子x5")
    st.checkbox("碗筷")
    st.checkbox("延長線")
    st.checkbox("電燈")
    st.write("##### 煮食材需使用的器具")
    st.checkbox("平底鍋")
    st.checkbox("鍋鏟")
    st.checkbox("油")
    st.write("##### 清潔用品與驅蚊")
    st.checkbox("個人盥洗用品")
    st.checkbox("垃圾袋")
    st.checkbox("衛生紙")
    st.checkbox("蚊香")
    st.write("### 容噗")
    st.write("個人盥洗用品", ", 碗筷", ", 洗碗精", ", 菜瓜布", ", 鹽")
    st.write("### 展肇")
    st.write("睡袋(棉被、枕頭)", ", 個人盥洗用品", ", 碗筷", ", 鍋子", ", 大湯匙", ", 延長線")

with tabs[2]:
    st.write("##### 食材")
    st.checkbox("湯底")
    st.checkbox("雞肉")
    st.checkbox("牛肉")
    st.checkbox("豬肉")
    st.checkbox("高麗菜")
    st.checkbox("玉米筍")
    st.checkbox("金針菇")
    st.checkbox("杏包菇")
    st.checkbox("蛋")
    st.checkbox("麵")
    st.checkbox("吐司")



with tabs[3]:
    st.header("天氣")
    st.write("check out this [中央氣象局](https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000511)")

with tabs[4]:
    st.header("露營地位置")
    st.components.v1.iframe("https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d654.9118788310941!2d120.98683181758133!3d24.571989290879895!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2bc56149f2c170e8!2z5Y2X5bqE5p6X5rOJ6Zyy54ef5Y2A!5e0!3m2!1szh-TW!2stw!4v1667197434635!5m2!1szh-TW!2stw",
                        width=350, height=650, scrolling=False)
