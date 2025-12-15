import streamlit as st

# --------------------------------------------------
# Page config (important for full-screen background)
# --------------------------------------------------
st.set_page_config(
    page_title="Birthday Surprise",
    layout="wide"
)

# --------------------------------------------------
# Background video (FIXED & WORKING)
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* Remove default Streamlit background */
    .stApp {
        background: transparent;
    }

    /* Video background */
    .video-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: cover;
        z-index: -2;
    }

    /* Dark overlay for readability */
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.45);
        z-index: -1;
    }
    </style>

    <video class="video-background" autoplay muted loop playsinline>
        <source src="https://www.w3schools.com/howto/rain.mp4" type="video/mp4">
    </video>

    <div class="overlay"></div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Main UI
# --------------------------------------------------
st.markdown("<h1 style='text-align:center; color:white;'>🎁 Birthday Surprise 🎁</h1>", unsafe_allow_html=True)

if st.button("🎉 Click for surprise", use_container_width=True):
    st.balloons()

    ascii_html = """
<pre style="
    font-family: monospace;
    font-size: 18px;
    line-height: 1.2;
    white-space: pre;
    text-align: center;
">

<span style="color:#ff9800;">
████████████████████████████████████████████████████████
</span>

<span style="color:#9c27b0;">
 _           _                                                                
(_)         (_)                                                               
(_)         (_)   _  _  _       _  _  _  _    _  _  _  _   _               _  
(_) _  _  _ (_)  (_)(_)(_) _   (_)(_)(_)(_)_ (_)(_)(_)(_)_(_)_           _(_) 
(_)(_)(_)(_)(_)   _  _  _ (_)  (_)        (_)(_)        (_) (_)_       _(_)   
(_)         (_) _(_)(_)(_)(_)  (_)        (_)(_)        (_)   (_)_   _(_)     
(_)         (_)(_)_  _  _ (_)_ (_) _  _  _(_)(_) _  _  _(_)     (_)_(_)       
(_)         (_)  (_)(_)(_)  (_)(_)(_)(_)(_)  (_)(_)(_)(_)        _(_)         
                              (_)           (_)            _  _(_)           
                              (_)           (_)           (_)(_)             
</span>

<span style="color:#2196f3;">
██████╗ ██╗██████╗ ████████╗██╗  ██╗██████╗  █████╗ ██╗   ██╗
██╔══██╗██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
██████╔╝██║██████╔╝   ██║   ███████║██║  ██║███████║ ╚████╔╝ 
██╔══██╗██║██╔══██╗   ██║   ██╔══██║██║  ██║██╔══██║  ╚██╔╝  
██████╔╝██║██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║   ██║   
╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   
</span>

<span style="color:#4caf50;">
🎂 🎉 🎈  W I S H I N G   Y O U   V E R Y   H A P P Y   B I R T H D A Y   D A D D Y
</span>

<span style="color:#f44336;">
❤  S M I L E S   |   J O Y   |   S U C C E S S   |   H A P P I N E S S  ❤
</span>

<span style="color:#ff9800;">
████████████████████████████████████████████████████████
</span>

</pre>
"""

    st.markdown(ascii_html, unsafe_allow_html=True)

    # Audio (plays after user interaction)
    st.audio("audio.mp3", autoplay=True)
