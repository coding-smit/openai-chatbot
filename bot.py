import pyautogui
import time
import pyperclip
from openai import OpenAI
from dotenv import load_dotenv


client = OpenAI(
 base_url="https://openrouter.ai/api/v1",
 api_key="OPENROUTER_API_KEY",  # replace with your key
             
)

# def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
#     # Split the chat log into individual messages
#     messages = chat_log.strip().split("/2024] ")[-1]
#     if sender_name in messages:
#         return True 
#     return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(558, 746)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo( 516 ,154)
    pyautogui.dragTo(974, 708, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(974, 708)


    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()        

    # Print the copied text to verify
    print(chat_history)
    # print(is_last_message_from_sender(chat_history))
    # if is_last_message_from_sender(chat_history):
    completion = client.chat.completions.create(
        model="openai/gpt-4o",
        messages=[
            {"role": "system", "content": "You are a person named smit who speaks hindi as well as english. You are from India and you are a funny person. You analyze chat history and roast people in a funny way if message send by sender else not reply. Output should be the next chat response in very short (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
            {"role": "user", "content": chat_history}
        ]
        )

    response = completion.choices[0].message.content
    pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
    pyautogui.click(635 ,706)
    time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

    # Step 7: Press Enter
    pyautogui.press('enter')