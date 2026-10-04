# Memory Skill


## Skill Purpose


Memory Skill 用于保存 ComfyUI 学习过程中的长期知识。


目标：

让 Agent 记住：

- Workflow 经验
- 模型测试结果
- 用户学习记录
- 项目知识


---


# Core Ability


Agent 可以记录：


用户：

> 这个 Workflow 我测试过。


Agent:

创建：


Workflow Memory


保存：

```
- 使用环境
- 测试结果
- 注意事项
```



---


# Memory Types


## Workflow Memory


记录：


- Workflow
- Purpose
- Models
- Test Result
- Notes



---


## Model Memory


记录：


- Model
- Hardware
- Performance
- Compatibility



---


## Learning Memory


记录：


- Concept
- Explanation
- User Understanding



---


# Memory Pipeline

```
Interaction

    ↓

Extract Knowledge

    ↓

Validate

    ↓

Store Memory

    ↓

RAG Update
```



---


# Principle


Memory 保存：

稳定、有价值的信息。


不保存：

临时聊天内容。
