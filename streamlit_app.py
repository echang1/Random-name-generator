import streamlit as st
import random

def main():
    st.title("Random Person Selector")

    # Input for user to enter names
    names_input = st.text_area("Enter names separated by commas:", "")
    
    if names_input:
        # Split input text into a list of names
        names_list = [name.strip() for name in names_input.split(",") if name.strip()]
        
        if names_list:
            # Button to select a random person
            if st.button("Select Random Person"):
                selected_person = random.choice(names_list)
                st.write(f"The selected person is: **{selected_person}**")
        else:
            st.write("Please enter at least one name.")
    else:
        st.write("Please enter names in the text area.")

if __name__ == "__main__":
    main()
