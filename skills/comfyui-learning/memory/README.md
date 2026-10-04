# Memory Skill


## Purpose


保存 ComfyUI 长期学习知识。


---


## Input


- Workflow Test
- User Note
- Experiment Result



---


## Output


memory_database.json



---


## Example


用户：


这个 Workflow 运行成功


保存：

```
Workflow:
Wan Video

GPU:
4090

VRAM:
22GB

Status:
tested
```


---


## Relation


Memory 会被：

RAG Skill


读取。


形成：

```
Memory

    ↓

RAG

    ↓

Agent
```
