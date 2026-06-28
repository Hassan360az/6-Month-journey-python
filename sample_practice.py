import streamlit as st
import requests

# App ka Title
st.title("Student Report Card Viewer (Pure Python!)")
st.write("FastAPI Path Parameters ke zariye backend se data load karein.")

# User se input lene ke liye number field
student_id = st.number_input("Enter Student ID (Try 1, 2, or 3):", min_value=1, step=1)

# Jab user button click karega
if st.button("Get Report Card"):
    
    # FastAPI ka URL jahan hum ne dynamic path parameter lagaya hai
    backend_url = f"http://127.0.0.1:8000/report/{student_id}"
    
    try:
        # Backend ko request bhej rahe hain
        response = requests.get(backend_url)
        
        if response.status_code == 200:
            data = response.json()
            
            # UI par data show karna (Python ke zariye card banana)
            st.success(f"Record found for {data['name']}!")
            
            # Data ko clean formatting mein dikhana
            st.markdown(f"**Name:** {data['name']}")
            st.markdown(f"**Maths Marks:** {data['maths']}")
            st.markdown(f"**English Marks:** {data['english']}")
            
            if data['status'] == "Passed":
                st.info(f"Final Status: {data['status']}")
            else:
                st.error(f"Final Status: {data['status']}")
                
        elif response.status_code == 404:
            st.error("Error: Student ID database mein nahi mili.")
            
    except requests.exceptions.ConnectionError:
        st.error("Backend server nahi chal raha! Pehle uvicorn run karein.")