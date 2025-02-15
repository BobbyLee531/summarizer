# summarizer

## **简介**  
是一个基于 Flask 和 JavaScript 的 AI 文本总结工具。用户可以在网页上输入文本，并通过后端 AI 模型生成总结内容。  

## **功能**  

- **输入文本** 并点击按钮进行 AI 总结  
- **前端 UI** 使用 HTML、CSS、JavaScript（`index.html`）  
- **后端** 采用 Flask 处理用户请求（`main.py`）  

---

## **安装依赖**  
### **1. 克隆项目**  
```bash
git clone https://github.com/BobbyLee531/summarizer.git
cd summarize
```

### **2. 安装 Python 依赖**  
  
```bash
pip install -r requirements.txt
```

---

## **运行项目**  
### **1. 启动后端（Flask）**  
```bash
python main.py
```
后端将在 `http://127.0.0.1:5000/` 运行。  

### **2. 启动前端**  
直接打开 `index.html`，

---

## **API 说明**  
后端提供一个 `/process` 接口，支持 POST 请求：
- **URL:** `http://127.0.0.1:5000/process`

---

## **文件结构**  
```
├── index.html  # 前端页面
├── main.py     # 后端 Flask 代码
├── requirements.txt  # 依赖文件
└── README.md   # 项目说明
```

---

