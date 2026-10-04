# RAG Skill


## Skill Purpose


RAG Skill 用于连接：

- Workflow Database
- Node Database
- Model Database


让 AI Agent 可以进行语义搜索。


---


# Core Ability


Agent 支持：

自然语言查询。


例如：

用户：

> 找一个 Wan 视频生成 workflow


Agent:


搜索：

workflow:

video_generation


+

node:

Wan


+

model:

Wan model


返回匹配结果。


---


# Knowledge Sources


RAG 输入：


- workflow_manifest.json
- node_database.json
- model_database.json



---


# Processing Pipeline

```
Database

    ↓

Document Preparation

    ↓

Embedding

    ↓

Vector Index

    ↓

Retriever

    ↓

LLM
```



---


# RAG Responsibility


负责：

- 文档转换
- 索引建立
- 相似搜索
- 结果召回


不负责：

- 最终回答生成
- Workflow 评价
