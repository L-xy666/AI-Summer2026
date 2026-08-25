import ollama
from app.config import LLM_MODEL
from app.prompt import build_analysis_prompt



def generate_ai_analysis(
        df,
        stats,
        top_product
):

    prompt = build_analysis_prompt(
        df,
        stats,
        top_product
    )

    try:
        response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {
                    "role":"system",
                    "content":
                    "你是一名专业的数据分析师，负责分析销售数据。"
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )


        return response["message"]["content"]
    except Exception as e:
        return f"""
##AI分析暂时不可用

原因：
{e}

请检查：
1.Ollama是否启动
运行
ollama serve

2.模型是否存在
运行
ollama list
需要模型：
qwen2.5:3b
"""