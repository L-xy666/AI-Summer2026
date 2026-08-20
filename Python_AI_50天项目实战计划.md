# Python + AI 项目实战计划
## AI 数据分析与智能决策平台

> 目标：用一个完整项目贯穿 Python 工程化、数据分析、面向对象、MySQL、FastAPI、机器学习、LLM、RAG、Agent、Docker。
>
> 学习方式：30% 看课程 + 70% 写代码。
>
> 建议环境：PyCharm / VS Code / Jupyter / MySQL / Ollama / Docker / Git
>
> 项目目录建议：
> E:\AI-Summer2026\Projects\ai-data-platform

---

# 一、最终项目目标

用户上传 CSV / Excel 数据后，系统能够：

1. 自动读取和检查数据
2. 自动进行数据清洗
3. 进行统计分析
4. 自动生成可视化图表
5. 生成数据分析报告
6. 使用机器学习进行预测
7. 使用 Ollama 本地大模型解释分析结果
8. 支持自然语言提问
9. 使用 RAG 检索项目文档
10. 最终形成 Web 应用
11. 使用 Docker 完成部署

最终架构：

用户
 ↓
Web 前端
 ↓
FastAPI
 ↓
业务层
 ├── 数据分析
 ├── 机器学习
 ├── LLM
 ├── RAG
 └── Agent
 ↓
MySQL / Redis / Ollama

---

# 二、50天学习路线

## 第一阶段：Python 工程化（Day 1-7）

### Day 1：项目初始化
- [ ] 创建项目目录
- [ ] 创建虚拟环境
- [ ] Git 初始化
- [ ] 创建 README.md
- [ ] 编写第一个 main.py
- [ ] 学习 requirements.txt / pyproject.toml 基本概念

项目成果：
- 能独立创建规范 Python 项目

### Day 2：文件与路径
- [ ] pathlib
- [ ] CSV 基础读写
- [ ] JSON 基础读写
- [ ] 文件编码
- [ ] 数据目录设计

项目成果：
- 实现 DataLoader 初版

### Day 3：异常处理
- [ ] try / except
- [ ] else / finally
- [ ] 自定义异常
- [ ] 异常信息设计

项目成果：
- 文件不存在、格式错误时程序不会直接崩溃

### Day 4：模块与包
- [ ] import
- [ ] 模块
- [ ] package
- [ ] __init__.py
- [ ] 相对导入与绝对导入

项目成果：
- 把项目拆成多个 Python 模块

### Day 5：类型提示
- [ ] type hints
- [ ] list / dict 类型
- [ ] Optional
- [ ] Union
- [ ] 函数返回值类型
- [ ] 基础泛型概念

项目成果：
- 给核心函数增加类型提示

### Day 6：日志与调试
- [ ] logging
- [ ] 日志等级
- [ ] Debug
- [ ] breakpoint
- [ ] 常见错误排查

项目成果：
- 项目拥有基本日志系统

### Day 7：阶段重构
- [ ] 整理代码
- [ ] Git commit
- [ ] 完成 README 第一版
- [ ] 回顾 Day 1-6

阶段目标：
- 能写一个结构清晰的小型 Python 项目

---

# 三、第二阶段：NumPy + Pandas 数据分析（Day 8-14）

## Day 8：NumPy
- [ ] ndarray
- [ ] shape
- [ ] dtype
- [ ] 索引
- [ ] 切片
- [ ] 向量化

项目：
- 完成基础数值处理模块

## Day 9：Pandas 基础
- [ ] Series
- [ ] DataFrame
- [ ] read_csv
- [ ] head
- [ ] info
- [ ] describe

项目：
- CSV 数据读取

## Day 10：数据筛选
- [ ] loc
- [ ] iloc
- [ ] 条件筛选
- [ ] 排序
- [ ] 新增列
- [ ] 删除列

项目：
- 实现数据筛选功能

## Day 11：数据清洗
- [ ] 缺失值
- [ ] 重复值
- [ ] 异常值
- [ ] 类型转换
- [ ] 字符串处理

项目：
- DataCleaner

## Day 12：分组与统计
- [ ] groupby
- [ ] agg
- [ ] value_counts
- [ ] pivot_table

项目：
- 自动生成统计摘要

## Day 13：多表数据
- [ ] merge
- [ ] concat
- [ ] join
- [ ] 数据关联

项目：
- 支持多个 CSV 文件

## Day 14：阶段项目
完成：
- [ ] 数据读取
- [ ] 数据清洗
- [ ] 数据统计
- [ ] 数据导出

阶段目标：
- 能独立使用 Pandas 完成一次完整的数据处理

---

# 四、第三阶段：数据可视化（Day 15-18）

## Day 15：Matplotlib
- [ ] figure
- [ ] axes
- [ ] title
- [ ] xlabel / ylabel
- [ ] legend

## Day 16：常用图表
- [ ] 柱状图
- [ ] 折线图
- [ ] 饼图
- [ ] 散点图
- [ ] 直方图

## Day 17：数据关系
- [ ] 相关性
- [ ] correlation
- [ ] heatmap
- [ ] 箱线图

## Day 18：自动图表模块
完成：
- [ ] 根据数据类型选择图表
- [ ] 保存 PNG
- [ ] 统一图表目录

项目成果：
- ChartGenerator

---

# 五、第四阶段：高级 Python + 面向对象（Day 19-23）

## Day 19：OOP 基础强化
- [ ] class
- [ ] object
- [ ] __init__
- [ ] 属性
- [ ] 方法

## Day 20：继承与多态
- [ ] inheritance
- [ ] override
- [ ] polymorphism
- [ ] super

## Day 21：高级特性
- [ ] property
- [ ] classmethod
- [ ] staticmethod
- [ ] __str__
- [ ] __repr__
- [ ] 常见魔术方法

## Day 22：抽象与设计
- [ ] ABC
- [ ] 抽象类
- [ ] 接口思想
- [ ] 依赖注入概念
- [ ] SOLID 基础

## Day 23：项目重构
将项目整理为：

app/
├── core/
├── data/
├── analysis/
├── visualization/
├── models/
└── utils/

核心类：
- DataLoader
- DataCleaner
- DataAnalyzer
- ChartGenerator
- ReportGenerator

阶段目标：
- 从“能运行的脚本”升级成“结构化项目”

---

# 六、第五阶段：MySQL + 数据库（Day 24-28）

## Day 24：SQL 基础
- [ ] SELECT
- [ ] INSERT
- [ ] UPDATE
- [ ] DELETE
- [ ] WHERE
- [ ] ORDER BY

## Day 25：高级 SQL
- [ ] JOIN
- [ ] GROUP BY
- [ ] HAVING
- [ ] 子查询
- [ ] 聚合函数

## Day 26：数据库设计
设计：
- users
- datasets
- analysis_tasks
- analysis_results
- chat_history
- prediction_results

学习：
- [ ] 主键
- [ ] 外键
- [ ] 索引
- [ ] 范式
- [ ] 事务

## Day 27：Python 连接 MySQL
- [ ] 数据库驱动
- [ ] SQLAlchemy
- [ ] ORM
- [ ] Model

## Day 28：数据库模块
完成：
- [ ] 数据集保存
- [ ] 分析结果保存
- [ ] 用户记录
- [ ] 查询历史

阶段目标：
- Python 项目能够稳定使用 MySQL

---

# 七、第六阶段：FastAPI Web 应用（Day 29-34）

## Day 29：HTTP 与 API
- [ ] HTTP
- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE
- [ ] JSON

## Day 30：FastAPI
- [ ] 路由
- [ ] Request
- [ ] Response
- [ ] Query
- [ ] Path
- [ ] Body

## Day 31：Pydantic
- [ ] 数据模型
- [ ] 数据验证
- [ ] 类型检查
- [ ] Response Model

## Day 32：文件上传
完成：
- [ ] CSV 上传
- [ ] Excel 上传
- [ ] 文件类型检查
- [ ] 文件大小检查

## Day 33：API 设计
实现：
- [ ] POST /upload
- [ ] GET /dataset
- [ ] GET /analysis
- [ ] GET /charts
- [ ] POST /predict
- [ ] POST /ask

## Day 34：Web 第一版
完成：
- [ ] API 文档
- [ ] Swagger 测试
- [ ] 数据上传
- [ ] 分析结果返回

阶段目标：
- Python 数据分析能力变成 Web 服务

---

# 八、第七阶段：机器学习（Day 35-40）

## Day 35：机器学习基础
- [ ] 特征
- [ ] 标签
- [ ] 训练集
- [ ] 测试集
- [ ] 验证集
- [ ] 过拟合

## Day 36：Scikit-learn
- [ ] train_test_split
- [ ] fit
- [ ] predict
- [ ] Pipeline

## Day 37：回归
- [ ] 线性回归
- [ ] MAE
- [ ] MSE
- [ ] RMSE
- [ ] R²

项目：
- 销售额预测

## Day 38：分类
- [ ] 逻辑回归
- [ ] 决策树
- [ ] 随机森林
- [ ] accuracy
- [ ] precision
- [ ] recall
- [ ] F1

项目：
- 用户/学生分类预测

## Day 39：聚类
- [ ] K-Means
- [ ] 聚类思想
- [ ] 特征标准化

项目：
- 用户分群

## Day 40：机器学习模块
完成：

MachineLearningEngine
├── preprocess
├── train
├── evaluate
├── predict
└── save_model

阶段目标：
- 项目拥有真实 AI/ML 能力

---

# 九、第八阶段：Ollama + LLM（Day 41-44）

## Day 41：LLM 基础
- [ ] Token
- [ ] Prompt
- [ ] Context
- [ ] Temperature
- [ ] System Prompt
- [ ] API 调用

## Day 42：Ollama
- [ ] Ollama 模型管理
- [ ] Python 调用 Ollama
- [ ] Prompt 设计
- [ ] 结构化输出

项目：
- AI 自动生成数据分析报告

## Day 43：AI 数据分析助手
实现：

用户：
“分析一下这个数据集”

系统：
1. 获取数据摘要
2. 统计关键指标
3. 调用 LLM
4. 生成分析结论

## Day 44：自然语言问数据
用户可以问：

“哪个产品销量最高？”
“哪个月份销售额最低？”
“哪些因素影响销售？”

AI：
- 理解问题
- 调用数据分析函数
- 返回结果

阶段目标：
- 从普通数据分析升级成 AI 数据分析

---

# 十、第九阶段：RAG + Agent（Day 45-47）

## Day 45：RAG
- [ ] 文档加载
- [ ] 文本切分
- [ ] Embedding
- [ ] 向量数据库
- [ ] 相似度检索

支持：
- PDF
- Markdown
- TXT

## Day 46：Agent
理解：
- [ ] Tool
- [ ] Tool Calling
- [ ] Agent
- [ ] 工作流

工具：
- data_summary
- data_filter
- data_statistics
- generate_chart
- machine_learning_predict

## Day 47：AI Agent
实现：

用户：
“帮我分析销售数据，并告诉我哪个产品最值得推广。”

Agent：
1. 理解问题
2. 查询数据
3. 调用 Pandas
4. 调用统计分析
5. 必要时调用 ML
6. 生成图表
7. LLM 总结

阶段目标：
- 项目拥有真正的 AI Agent 能力

---

# 十一、第十阶段：Docker + 项目完善（Day 48-50）

## Day 48：Docker
- [ ] Dockerfile
- [ ] Image
- [ ] Container
- [ ] Docker Compose
- [ ] 环境变量

容器：
- FastAPI
- MySQL
- Redis
- Ollama（根据机器资源决定）

## Day 49：项目工程化
- [ ] README
- [ ] requirements
- [ ] .env
- [ ] .gitignore
- [ ] 日志
- [ ] 错误处理
- [ ] API 文档
- [ ] 项目截图

## Day 50：最终版本
完成：

- [ ] 数据上传
- [ ] 数据清洗
- [ ] 数据分析
- [ ] 图表生成
- [ ] ML 预测
- [ ] LLM 分析
- [ ] RAG
- [ ] Agent
- [ ] Web API
- [ ] MySQL
- [ ] Docker
- [ ] Git
- [ ] README

---

# 十二、最终项目目录

```text
ai-data-platform/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── upload.py
│   │   ├── analysis.py
│   │   ├── prediction.py
│   │   └── chat.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── exceptions.py
│   │
│   ├── data/
│   │   ├── loader.py
│   │   └── cleaner.py
│   │
│   ├── analysis/
│   │   ├── analyzer.py
│   │   └── statistics.py
│   │
│   ├── visualization/
│   │   └── chart_generator.py
│   │
│   ├── ml/
│   │   ├── preprocess.py
│   │   ├── trainer.py
│   │   └── predictor.py
│   │
│   ├── llm/
│   │   ├── ollama_client.py
│   │   ├── prompts.py
│   │   └── agent.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   └── retriever.py
│   │
│   ├── models/
│   │   └── database_models.py
│   │
│   └── services/
│       ├── analysis_service.py
│       ├── prediction_service.py
│       └── chat_service.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── notebooks/
│   ├── 01_numpy.ipynb
│   ├── 02_pandas.ipynb
│   ├── 03_visualization.ipynb
│   └── 04_machine_learning.ipynb
│
├── models/
│
├── tests/
│
├── docs/
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 十三、每天学习的固定流程

建议每天 6-8 小时：

## 上午：学习
2小时左右

- 看 B 站课程
- 做课程代码
- 不追求一次全部看懂

## 下午：项目
3-4小时

把当天知识放进项目。

原则：

> 今天学什么，就想办法让项目用上什么。

## 晚上：复盘
1-2小时

记录：

- 今天学了什么
- 今天写了什么
- 哪些地方不会
- 哪些代码是 AI 帮你写的
- 明天要解决什么

---

# 十四、使用 AI 编程工具的原则

你已经安装了 Trae / CodeBuddy，这些工具可以用。

但是建议遵守：

> **先自己写 → 报错 → 自己分析 → AI 辅助 → 自己理解 → 自己修改**

不要：

> “帮我把这个项目全部写出来。”

尤其是下面这些必须自己理解：

- 函数
- class
- API
- SQL
- Pandas
- ML
- Prompt
- RAG
- Agent

否则最后很容易变成：

**项目是你的，但你不会解释项目。**

---

# 十五、项目最终简历定位

最终可以把项目描述成：

> AI 数据分析与智能决策平台

技术栈：

> Python + Pandas + NumPy + Scikit-learn + FastAPI + MySQL + SQLAlchemy + Ollama + RAG + Agent + Docker

核心功能：

> 支持 CSV/Excel 数据上传、自动数据清洗、统计分析、可视化、机器学习预测，并结合本地大语言模型实现自然语言数据分析、RAG 知识检索及 Agent 工具调用。

---

# 十六、你的第一天

不要一下子把 50 天全部做了。

**今天只做 Day 1。**

第一步：

```text
E:\AI-Summer2026\Projects```

创建：

```text
ai-data-platform
```

然后用 VS Code 打开这个文件夹。

第一版目录只需要：

```text
ai-data-platform/
├── app/
│   └── main.py
├── data/
├── notebooks/
├── tests/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

然后运行：

```python
print("AI Data Platform")
print("Project started!")
```

**不要急着安装一堆库。**

等做到 Day 8 数据分析阶段，再安装 Pandas / NumPy；做到 Web 阶段再安装 FastAPI；做到 LLM 阶段再处理 Ollama。

这样你的环境会一直保持干净。

