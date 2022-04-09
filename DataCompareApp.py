import streamlit as st
import pandas as pd

st.title("Data Compare")

with st.form("my_form"):

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file, encoding = 'utf8')
        #st.write(dataframe)
        final_list = []
        
        for original_row in df.itertuples():
            col1_new_list = []
            col2_new_list = []

            if len(original_row) == 3:
                col1 = original_row.Column1.strip().lower()
                col2 = original_row.Column2.strip().lower()
                col1_token_list = col1.split()
                col2_token_list = col2.split()

                # Build new column 1 list
                for token in col1_token_list:
                    if token not in col2_token_list:
                        col1_new_list.append(token)

                # Build new column 2 list
                for token in col2_token_list:
                    if token not in col1_token_list:
                        col2_new_list.append(token)

                col1_new = " ".join(col1_new_list)
                col2_new = " ".join(col2_new_list)

                final_list.append([col1_new, col2_new])

                output = pd.DataFrame(final_list, columns = ['Column1', 'Column2'])

    # Every form must have a submit button.
    submitted = st.form_submit_button("Show difference")

    if submitted:
        st.table(output)