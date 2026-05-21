import base64

import streamlit as st
from factorial import fact

with open("monkey-cool.gif", "rb") as f:
    gif_base64 = base64.b64encode(f.read()).decode()

html_code = f"""
<style>
@keyframes zigzag {{
    0%   {{ left: 0%; top: 10%; }}
    10%  {{ left: 20%; top: 20%; }}
    20%  {{ left: 10%; top: 35%; }}
    30%  {{ left: 40%; top: 25%; }}
    40%  {{ left: 30%; top: 50%; }}
    50%  {{ left: 60%; top: 40%; }}
    60%  {{ left: 50%; top: 65%; }}
    70%  {{ left: 80%; top: 55%; }}
    80%  {{ left: 70%; top: 80%; }}
    90%  {{ left: 90%; top: 70%; }}
    100% {{ left: 0%; top: 10%; }}
}}

.zigzag-gorilla {{
    position: fixed;
    width: 90px;
    z-index: 9999;
    animation: zigzag 6s linear infinite;
}}
</style>
<img class="zigzag-gorilla" src="data:image/gif;base64,{gif_base64}" />
"""

st.markdown(html_code, unsafe_allow_html=True)
    
def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number:", 
                              min_value=0, 
                              max_value= 900)
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"The factorial of {number} is {result}")
        st.balloons()


if __name__ == "__main__":
    main()
    