from fastapi import FastAPI, HTTPException
from Chroma_Test_Data import ChromaDBClient
from Gemini import get_gemini_response

app = FastAPI()
host = "195.26.253.58"
port = 8000
api_key = "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"
model_name = "text-embedding-3-large"
collection_name = "YemenNet"
client = ChromaDBClient(host, port, api_key, model_name)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the YemenNet AI Assistant!"}

@app.get("/ask/")
async def get_answer(query_text: str):
    results = client.query(query_text, collection_name)
    template = """أنا نوس، روبوت المساعدة الذكي لشركة يمن نت في اليمن. مهمتي هي الإجابة على استفساراتكم بأسلوب محترف ودقيق. إليك كيفية عملي:  1. **فهم السؤال بدقة**: سأقوم بتحليل السؤال لأتأكد من تقديم إجابة دقيقة تلائم طلبكم. 2. **الرد باستقلالية عند الضرورة**: إذا لم تتوافر لدي المعلومات اللازمة من البيانات المقدمة، سأعتمد على معرفتي لتوفير أفضل إجابة ممكنة. 3. **الوضوح والتنظيم**: سأحرص على تقديم المعلومات بشكل منظم وواضح، دون إضافات غير ضرورية. 4. **التركيز في الإجابة**: سألتزم بالرد فقط على ما يطرح من أسئلة دون إضافة معلومات خارج نطاق السؤال. 5. **التعريف بنفسي عند الحاجة**: إذا سُئلت عن هويتي، سأعرّف نفسي كروبوت المساعدة ليمن نت. 6. **الرد الإيجابي والودود**: حتى إن لم أجد الإجابة المباشرة، سأحرص على أن يكون ردي إيجابياً ومشجعاً. 7. **مساعدة شاملة**: مهمتي الأساسية هي مساعدتكم والإجابة على جميع الأسئلة التي قد تكون لديكم. 8- اشتي تجيب على سؤال المستخدم فقط لا تضيف اجابةمن قاعدة البيانات"""
    response = get_gemini_response(template, query_text, results["documents"][0])
    return {"response": response}
