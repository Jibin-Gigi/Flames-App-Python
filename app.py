import streamlit as st

# Function to calculate FLAMES status
def flames_calculation(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    name1_list = list(name1)
    name2_list = list(name2)

    # Remove common characters
    for i in name1:
        if i in name2_list:
            name1_list.remove(i)
            name2_list.remove(i)

    count = len(name1_list) + len(name2_list)
    flames = ['Friendship', 'Love', 'Attraction', 'Marriage', 'Enemy', 'Siblings']

    # Calculate FLAMES
    while len(flames) > 1:
        split_at = (count % len(flames)) - 1
        if split_at >= 0:
            right = flames[split_at + 1:]
            left = flames[:split_at]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]

# Streamlit app
st.title('FLAMES Game')
name1 = st.text_input("Enter your name")
name2 = st.text_input("Enter your crush's name")

if st.button('Calculate Relationship Status'):
    result = flames_calculation(name1, name2)
    st.write('Relationship status:', result)
