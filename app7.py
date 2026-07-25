import random
import streamlit as st

st.title("welcome to our game")

# 1. تهيئة العداد وحفظه في الذاكرة لمرة واحدة فقط
if 'num' not in st.session_state:
    st.session_state.num = 0

# 2. توليد المسألة الحسابية وحفظها في الذاكرة لمرة واحدة فقط (تم حذف السطور العشوائية الزائدة)
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.sign = random.choice(['+', '-', '*', '/'])

# 3. استخراج القيم من الذاكرة لضمان ثباتها عند الضغط على الأزرار
num1 = st.session_state.num1
num2 = st.session_state.num2
sign = st.session_state.sign

# 4. حساب الناتج الصحيح بدقة
if sign == '+':
    sc = num1 + num2
elif sign == '-':
    sc = num1 - num2
elif sign == '*':
    sc = num1 * num2
elif sign == '/':
    sc = num1 / num2

# 5. عرض المسألة للمستخدم
st.write(num1, sign, num2)

# حقل الإدخال مع دعم الكسور بدقة 3 أرقام عشرية لمنع مشاكل القسمة
number = st.number_input("What is the result", step=0.001, format="%.3f")

# 6. زر تأكيد التخمين ومقارنة النتيجة المقربة لضمان الدقة
if st.button("تأكيد التخمين"):
    if round(number, 3) == round(sc, 3):
        st.success("you are winner ")
        st.session_state.num += 1  # زيادة الذاكرة مباشرة
    else:
        st.error("you are not winner ")

# 7. عرض النقاط الحالية للاعب (يبدأ من أول السطر تماماً لتفادي تداخل الأزرار)
st.write(f"النقاط الحالية: {st.session_state.num}")

# 8. زر السؤال التالي (منفصل تماماً وخارج نطاق الأزرار الأخرى)
if st.button("السؤال التالي"):
    del st.session_state.num1
    del st.session_state.num2
    del st.session_state.sign
    st.rerun()
