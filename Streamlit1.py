import streamlit as st


st.title("My Personal Profile")
st.write("Welcome to my first Streamlit application!")



st.header("About Me")
st.subheader("My Hobbies")

name = "Hossam"
st.text("<%^&&Plain text")
st.markdown("**Hossam Elbana**\n\n*Italic text*\n\n# Heading\n\n- List item")
st.write("This is : ",name)
st.caption("Small caption")

st.markdown("- name: hossam")

st.code('name = "Hossam" \n\nprint(name)', language="python")


# # messages
st.success("Everything is working!")
st.info("Here is some information.")
st.warning("Be careful!")
st.error("Something went wrong!")


# st.image("personal_img.jpeg", caption="Eng. Zyad Elbehiry")
# st.video("test_video.mp4")
# st.audio("test_audio.mp3")


x = st.button("Click Me")
if x:
    st.write("Button clicked!")
