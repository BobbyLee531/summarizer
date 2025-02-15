from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 初始化 OpenAI 客户端
client = OpenAI(api_key="sk-8960c699bb5e4f1a8545fad13a7e8e63", base_url="https://api.deepseek.com")

def pull_ds(text: str) -> str:
    """
    调用 OpenAI API 处理文本，并返回格式化后的结果。
    """
    try:
        # 构造消息
        messages = [{
            "role": "user",
            "content": text + "将这个总结成已解决，待办事项和线索搜集三个方面，已解决的事情不用在细节里面再重复一遍已解决，\
                待办事项就是存在待办的问题，事项和具体的描述细节不用另起一行，直接用冒号连接\
                线索收集是有关于竞争品牌的信息，\
                整体用bullet point格式，注意分好层次，每一级分类标题加粗，\
                确保提炼足够精炼，不要有重复的信息但是也不要丢失信息，\
                字体大小一致，注意每一个缺失主语的句子是描述哪个对象的，确保输出中只有内容，没有其他任何提示词"
        }]

        # 调用 API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )

        # 提取返回的内容
        if response.choices and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            return "未收到有效响应，请检查 API 调用。"
    except Exception as e:
        return f"调用 OpenAI API 时出错：{str(e)}"

@app.route('/process', methods=['POST', 'OPTIONS']) 
def process():
    """
    处理前端请求，调用 pull_ds 函数并返回结果。
    """
    if request.method == 'OPTIONS':
        # 处理 CORS 预检请求
        return jsonify({'status': 'ok'}), 200

    try:
        # 获取前端发送的数据
        data = request.json
        input_text = data.get('input', '')

        if not input_text.strip():
            return jsonify({'output': '输入内容不能为空！'})

        # 调用处理函数
        output_text = pull_ds(input_text)

        # 返回处理结果
        return jsonify({'output': output_text})
    except Exception as e:
        return jsonify({'output': f'服务器内部错误：{str(e)}'})

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True, port=5000) 