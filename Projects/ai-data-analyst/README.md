# AI Data Analyst

基于 Python 的智能数据分析项目。

本项目实现了从 CSV 数据读取、数据清洗、指标分析到可视化展示的完整流程。

目前主要针对销售数据进行分析，后续将扩展 AI 自动分析能力。


## 项目功能

### 数据处理

- CSV 文件读取
- Pandas 数据处理
- 数据结构分析


### 数据分析

实现：

- 数据行数统计
- 数据列数统计
- 平均销量计算
- 最大销量计算
- 最小销量计算
- 销售额最高商品分析
- 商品销售额排行榜
- 商品销售额占比分析


### 数据可视化

使用 Matplotlib 实现：

- 商品销售额柱状图
- 商品销售额占比饼图
- 图表自动保存


## 项目结构



ai-data-analyst

├── app
│ ├── analyzer.py # 数据分析模块
│ ├── data_loader.py # 数据读取模块
│ ├── visualization.py # 数据可视化模块
│ ├── report.py # 报告生成模块
│ └── main.py # 项目入口
│
├── data
│ ├── raw # 原始数据
│ └── processed # 处理后的数据
│
├── outputs # 生成结果
│
├── requirements.txt
└── README.md



## 技术栈

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit（计划）


## 环境配置


创建环境：

```bash
conda create -n ai-summer python=3.12

进入环境：

conda activate ai-summer

安装依赖：

pip install -r requirements.txt
项目运行

进入项目目录：

cd Projects/ai-data-analyst

运行：

python -m app.main

运行后会：

输出数据分析结果
生成销售额柱状图
生成销售额占比饼图
项目规划

后续计划：

 Streamlit 数据分析网页
 用户上传 CSV 文件
 自动生成分析报告
 接入大语言模型进行数据解读
 构建 AI Data Analyst Assistant
Author

L-xy666

AI-Summer2026 Project


---

## 第三步：保存，然后检查

PowerShell：

```powershell
Get-Content README.md

确认内容正常。

第四步提交

注意你现在是在：

E:\AI-Summer2026\Projects\ai-data-analyst

执行：

git status

应该看到：

modified:
README.md

然后：

git add README.md

git commit -m "docs: add project README"

git push

完成后 GitHub 页面会从：

一个空项目

变成：

有介绍、有结构、有运行方式的正式项目。

下一步我们处理：

.gitignore 清理 outputs
开始 Streamlit Dashboard

这两个做完，你这个项目的完整度会明显上一个台阶。

# AI Data Analyst

基于 Python 的智能数据分析项目。

本项目实现了从 CSV 数据读取、数据清洗、指标分析到可视化展示的完整流程。

目前主要针对销售数据进行分析，后续将扩展 AI 自动分析能力。

## 项目功能

### 数据处理

- CSV 文件读取

- Pandas 数据处理

- 数据结构分析

### 数据分析

实现：

- 数据行数统计

- 数据列数统计

- 平均销量计算

- 最大销量计算

- 最小销量计算

- 销售额最高商品分析

- 商品销售额排行榜

- 商品销售额占比分析

### 数据可视化

使用 Matplotlib 实现：

- 商品销售额柱状图

- 商品销售额占比饼图

- 图表自动保存

## 项目结构

ai-data-analyst

├── app

│ ├── analyzer.py # 数据分析模块

│ ├── data_loader.py # 数据读取模块

│ ├── visualization.py # 数据可视化模块

│ ├── report.py # 报告生成模块

│ └── main.py # 项目入口

│

├── data

│ ├── raw # 原始数据

│ └── processed # 处理后的数据

│

├── outputs # 生成结果

│

├── requirements.txt

└── README.md

## 技术栈

- Python 3.12

- Pandas

- NumPy

- Matplotlib

- Seaborn

- Streamlit（计划）

## 环境配置

创建环境：

```bash

conda create -n ai-summer python=3.12

很好，你已经把 README 内容复制进去了。不过我注意到一个问题：

你现在发出来的内容里面有很多：

**# AI Data Analyst**

以及：

\- CSV 文件读取

这种格式。

这是因为你可能是在聊天里复制时带出了转义符，不是 Markdown 文件应该保存的格式。

README.md 里面应该是纯 Markdown。

请把 README.md 改成下面这样（直接覆盖即可）：

# AI Data Analyst

基于 Python 的智能数据分析项目。

本项目实现了从 CSV 数据读取、数据清洗、指标分析到可视化展示的完整流程。

目前主要针对销售数据进行分析，后续将扩展 AI 自动分析能力。


## 项目功能

### 数据处理

- CSV 文件读取
- Pandas 数据处理
- 数据结构分析


### 数据分析

实现：

- 数据行数统计
- 数据列数统计
- 平均销量计算
- 最大销量计算
- 最小销量计算
- 销售额最高商品分析
- 商品销售额排行榜
- 商品销售额占比分析


### 数据可视化

使用 Matplotlib 实现：

- 商品销售额柱状图
- 商品销售额占比饼图
- 图表自动保存


## 项目结构


ai-data-analyst

├── app
│ ├── analyzer.py # 数据分析模块
│ ├── data_loader.py # 数据读取模块
│ ├── visualization.py # 数据可视化模块
│ ├── report.py # 报告生成模块
│ └── main.py # 项目入口
│
├── data
│ ├── raw # 原始数据
│ └── processed # 处理后的数据
│
├── outputs # 生成结果
│
├── requirements.txt
└── README.md



## 技术栈

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit（计划）


## 环境配置

创建环境：

```bash
conda create -n ai-summer python=3.12

进入环境：

conda activate ai-summer

安装依赖：

pip install -r requirements.txt
项目运行

进入项目目录：

cd Projects/ai-data-analyst

运行：

python -m app.main

运行后会：

输出数据分析结果
生成销售额柱状图
生成销售额占比饼图
项目规划

后续计划：

 Streamlit 数据分析网页
 用户上传 CSV 文件
 自动生成分析报告
 接入大语言模型进行数据解读
 构建 AI Data Analyst Assistant
Author

L-xy666

AI-Summer2026 Project