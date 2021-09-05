import streamlit as st
import os
import pandas as pd
temp = '\\temp.csv'
path = "C:\Amritsar\streamlit"
path = path+temp
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
st.header("Salary Predection Model")
def upload_xlsx(uploaded_file):
    try:
        if uploaded_file:
            df = pd.read_excel(uploaded_file)
            st.dataframe(df)
            df.to_csv(path,index = False)
             
            return df
        
    except Exception as e:
        st.write("Oops!",e.__class__,"occurad")
        return df
    
    
    
            
def upload_csv(uploaded_file):
    
    try:
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
            df.to_csv(path,index = False)
            return df
    except Exception as e:
        st.write("Oops!", e.__class__  ,"occurad")
        return df    


    

#file upload
def file_upload():
    f_option = ('.xlsx','.csv','oracle')
    f_select = st.sidebar.radio("Choice a File Type ", f_option)
    if f_select=='.xlsx':
        uploaded_file = st.sidebar.file_uploader("Choise file ", type="xlsx")
        if uploaded_file:
            if st.sidebar.button("Upload File"):
                df=upload_xlsx(uploaded_file)

            
            
            
            
    elif f_select=='.csv':
        uploaded_file = st.sidebar.file_uploader("Choise file ", type="csv")
        if uploaded_file:
            if st.sidebar.button("Upload File"):
                df = upload_csv(uploaded_file)  
            
            
            
    elif f_select== 'oracle':
        st.info("Enter Oracle Database Infromation ")
        user = st.text_input("Enter The User name ")
        password =  st.text_input("Enter The Password ", type="password")
        host = st.text_input("Enter The host Number")
        port = st.text_input("Enter The Port Number")
        query = st.text_input("enter the query for the desired data")


def lg_reg():
    
    
    df =pd.read_csv(path)
    col_name = st.selectbox("pelase enter the name of columns to predicts", df.columns)
    if st.sidebar.checkbox('Build_model'):
        df = pd.read_csv(path)
        
        y = df[col_name]
        df = df.drop([col_name], axis=1)
    
        x=df
        x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=1)
        lr = LinearRegression()
        lr.fit(x_train,y_train)
        st.write("Model succesfull train")
        st.write("please enter your output with silder and predict")
        
        
        l = []
        for i in df:
            l.append(st.sidebar.slider('{}'.format(i), min(df[i]),max(df[i]),min(df[i])))
        
        if st.button('Predict...'):
            y_pred = lr.predict([l])
            st.write("Your Predited {} is {:.2f}".format(col_name, float(y_pred)))
        
        
        
 
        
    
    
def main():
    

    file_upload()
    lg_reg()
    
main()    
    
    

    
    
    
    
            
        