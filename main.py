import streamlit as st

def main():
    st.title("Clever Programmer Button Dashboard")

    # Using HTML to create buttons
    st.markdown('<a href="https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi/" target="_blank"><button style="height:50px; width:150px; font-size:20px;">INTERNAL</button></a>', unsafe_allow_html=True)

    st.markdown('<a href="https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-full/" target="_blank"><button style="height:50px; width:150px; font-size:20px;">Customer $7.5k</button></a>', unsafe_allow_html=True)

    st.markdown('<a href="https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-5/" target="_blank"><button style="height:50px; width:150px; font-size:20px;">Customer $5k</button></a>', unsafe_allow_html=True)

    st.markdown('<a href="https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-2/" target="_blank"><button style="height:50px; width:150px; font-size:20px;">Customer $2.5k</button></a>', unsafe_allow_html=True)

    st.markdown('<a href="https://app.payfunnels.com/invoices" target="_blank"><button style="height:50px; width:150px; font-size:20px;">PayFunnels</button></a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
