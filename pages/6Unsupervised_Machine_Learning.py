import streamlit as st
from Model_KMeans import KMeansClusteringModel
from Model_PCA import PCAModel

st.subheader("`Unsupervised Machine Learning`")

default_session_state = {
    'df': None,
    'target': None,
    'model_type': None,
    'train' : None,
}

for key, value in default_session_state.items():
    if key not in st.session_state:       
        st.session_state[key] = value

model_type = ['KMeans Clustering', 'Dimensionality Reduction-PCA']

def model_selection():
    def on_click():
        if st.session_state['temp_linear_model'] is None:
            st.warning('Please select a model.', icon="⚠️")
            return
        st.session_state['model_type'] = st.session_state['temp_linear_model']
        st.session_state['train'] = True

    with st.form(key='linear_model_multi'):
        st.selectbox("Select Model for Unsupervised Learning", model_type, key='temp_linear_model')
        st.form_submit_button('Select', on_click=on_click)

if st.session_state['df'] is not None and st.session_state['target'] is not None:
    model_selection()
else:
    st.warning('Please Upload Your data via selecting the "Preprocess Data" option in the sidebar to proceed.', icon="⚠️")

if st.session_state['train']:
    model_type = st.session_state['model_type']
    
    if model_type == 'KMeans Clustering':
        try:
            model = KMeansClusteringModel()
            model.parameters()
        except Exception as e:
            st.error(e)
        finally:
            st.session_state['train'] = False
    
    if model_type == 'Dimensionality Reduction-PCA':
        try:
            model = PCAModel()
            model.parameters()
        except Exception as e:
            st.error(e)
        finally:
            st.session_state['train'] = False







