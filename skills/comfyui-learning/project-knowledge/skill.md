# Project Knowledge Skill


## Skill Purpose


Project Knowledge Skill 用于管理 ComfyUI Learning 项目的整体知识结构。


目标：

让 Agent 理解：

- 项目有哪些资源
- 资源在哪里
- 资源之间如何关联
- 当前知识库状态


---


# Core Ability


Agent 可以回答：


用户：

> 我的 ComfyUI 知识库有什么？


Agent:

返回：

```
Workflow:

数量:
分类:

Models:

数量:

Nodes:

数量:

Learning:

记录:
```



---


# Knowledge Sources


来源：


- workflow_database
- node_database
- model_database
- memory_database
- rag_index



---


# Knowledge Structure

```
Project Knowledge

├── Workflow Knowledge
├── Node Knowledge
├── Model Knowledge
├── Experience Knowledge
└── Learning Knowledge
```



---


# Responsibility


负责：

- 知识组织
- 索引管理
- 关系维护


不负责：

- Workflow 生成
- 自动修改资源
