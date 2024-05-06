
import google.generativeai as genai
genai.configure(api_key="AIzaSyDHHCM4jdLio7svg2c_KRupC93lvShT6fg")

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_gemini_response(Template,question,Answer):
    prompt = f""" {Template}

السؤال {question}
اجابة السؤال {Answer}

"""
    print(prompt)
    response = chat.send_message(prompt.format(question=question))
    return response.text

