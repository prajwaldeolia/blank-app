
import streamlit as st
from streamlit_modal import Modal

def upload_tab_content(tab_name):
    if tab_name == "Local":
        uploaded_file = st.file_uploader("Upload a file from your local system")
        if uploaded_file:
            st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    elif tab_name == "YouTube":
        youtube_link = st.text_input("Enter the YouTube video URL")
        if youtube_link:
            st.success(f"YouTube video URL received: {youtube_link}")
    elif tab_name == "Google Drive":
        drive_link = st.text_input("Enter the Google Drive file link")
        if drive_link:
            st.success(f"Google Drive file link received: {drive_link}")
    elif tab_name == "S3 Folder":
        s3_path = st.text_input("Enter the S3 folder path")
        if s3_path:
            st.success(f"S3 folder path received: {s3_path}")
    elif tab_name == "Bulk Upload":
        uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)
        if uploaded_files:
            st.success(f"{len(uploaded_files)} files uploaded successfully!")
    elif tab_name == "Existing File":
        existing_file = st.selectbox("Select an existing file", ["File1.txt", "File2.txt", "File3.txt"])
        if existing_file:
            st.success(f"Selected existing file: {existing_file}")

def main():
    st.title("File Upload App")

    # Create a modal for the popup
    modal = Modal(key="upload_modal", title="Upload Files", max_width=600)

    if st.button("Click to Upload"):
        modal.open()

    if modal.is_open():
        with modal.container():
            if "selected_tab" not in st.session_state:
                st.session_state["selected_tab"] = "Local"

            tabs = ["Local", "YouTube", "Google Drive", "S3 Folder", "Bulk Upload", "Existing File"]
            selected_tab = st.radio("Select Upload Option", tabs, index=tabs.index(st.session_state["selected_tab"]))

            # Update session state when the radio button changes
            st.session_state["selected_tab"] = selected_tab

            st.write(f"### {selected_tab} Upload")
            upload_tab_content(selected_tab)

            # Add a centered submit button to close the popup and return to the main page
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("Submit"):
                    modal.close()
                    st.experimental_rerun()

if __name__ == "__main__":
    main()
