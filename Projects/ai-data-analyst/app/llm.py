import ollama

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


    response = ollama.chat(
        model="qwen2.5:3b",
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