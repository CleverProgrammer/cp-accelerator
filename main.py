import streamlit as st

def main():
    st.title("Clever Programmer Button Dashboard")

    if st.button('INTERNAL'):
        st.markdown("[Link](https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi/)", unsafe_allow_html=True)

    if st.button('Customer $7.5k'):
        st.markdown("[Link](https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-full/)", unsafe_allow_html=True)

    if st.button('Customer $5k'):
        st.markdown("[Link](https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-5/)", unsafe_allow_html=True)

    if st.button('Customer $2.5k'):
        st.markdown("[Link](https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-2/)", unsafe_allow_html=True)

    if st.button('PayFunnels'):
        st.markdown("[Link](https://app.payfunnels.com/invoices)", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
