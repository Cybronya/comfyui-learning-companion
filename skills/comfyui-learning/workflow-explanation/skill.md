# Workflow Explanation Skill


## Skill Purpose


Workflow Explanation Skill 用于让 AI Agent 理解并讲解 ComfyUI Workflow。


目标：

不是生成 Workflow。

而是：

- 分析 Workflow 结构
- 解释节点关系
- 说明数据流
- 帮助用户学习


---


# Core Ability


Agent 可以回答：


用户：

> 解释这个 workflow


Agent:

输出：

1. Workflow 用途

2. 整体流程

3. 节点作用

4. 模型作用

5. 参数意义

6. 学习建议



---


# Explanation Pipeline

```
Workflow JSON

    ↓

Workflow Scanner

    ↓

Node Database

    ↓

Model Database

    ↓

RAG

    ↓

Explanation
```



---


# Explanation Level


支持三个层级：


## Beginner


适合初学者。


解释：

- 这个 workflow 做什么
- 每一步的大概作用


---


## Intermediate


解释：

- 节点连接关系
- 数据流
- 参数影响


---


## Advanced


解释：

- Diffusion 过程
- Latent 变化
- Sampling 机制
- 模型结构



---


# Explanation Principle


解释应该：

清晰

分阶段

有上下文


避免：

只罗列节点名称。
