import streamlit as st

def main():
    st.title("Clever Programmer Button Dashboard")

    if st.button('INTERNAL'):
        st.write('https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi/')

    if st.button('Customer $7.5k'):
        st.write('https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-full/')

    if st.button('Customer $5k'):
        st.write('https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-5/')

    if st.button('Customer $2.5k'):
        st.write('https://courses.cleverprogrammer.com/profit-with-ai-accelerator-mi-2/')

    if st.button('PayFunnels'):
        st.write('https://app.payfunnels.com/invoices')

if __name__ == "__main__":
    main()
