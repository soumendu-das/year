import streamlit as st
import time

st.header("Wishify: Personalized New Year Greetings")


st.markdown("Crafted with ❤️ by Soumendu Das")

name=st.text_input("Enter your name :- ")

st.sidebar.title("**WISHIFI🎉**")
st.sidebar.write("Functionality:")
st.sidebar.write(" ⭐ Users input their name.")
st.sidebar.write(" ⭐ The app generates a customized New Year’s wish, incorporating their name.")

st.sidebar.subheader("soumendu chatbot")
with st.sidebar.chat_message("user"):
       prompt = st.sidebar.chat_input("Say something ...")
       if prompt:
        st.sidebar.write("✔ done")

if(st.button("press👆")):
    with st.status("🖐 wait ......."):
        st.write("5")
        time.sleep(1)
        st.write("4")
        time.sleep(1)
        st.write("3")
        time.sleep(1)
        st.write('2')
        time.sleep(1)
        st.write("1")
        time.sleep(1)
       
    st.image("images (5).jpeg")
    st.write(" ✨🎉🎊 Happy New Year 2025,",f"**💖{name}**💖 ","  On this wonderful occasion, Soumendu wishes you all the best for the year ahead.🥳 May this year bring you new success, happiness, and peace. May all your aspirations turn into achievements, and challenges become stepping stones 🥰. Wishing you a year filled with positivity and progress!😊")
    st.write("🎊🎉✨নতুন বছরের শুভেচ্ছা ",f"**💗{name}💗**",", নতুন সূর্যোদয়ের এই শুভ মুহূর্তে সৌমেন্দু তোমার জন্য জানাচ্ছে অন্তরের শুভকামনা 🥰। আশা করি এই বছর তোমার জীবনে সুখ, সমৃদ্ধি, এবং শান্তি নিয়ে আসবে। তোমার প্রতিটি স্বপ্ন পূর্ণ হোক, আর প্রতিটি বাধা হয়ে উঠুক সাফল্যের পথ 🤩। নতুন বছরের প্রতিটি দিন হোক আনন্দে ভরা এবং সাফল্যে উজ্জ্বল।🤗😙 ")
    
    
  
      