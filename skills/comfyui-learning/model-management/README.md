# Model Management Skill


## Purpose


建立 ComfyUI Model Knowledge Base。


---


## Output


生成：



model_database.json



包含：

```
Model

├── Type
├── Location
├── Compatibility
├── Requirements
└── Tags
```



---


## Workflow

```
models folder

    ↓

scan

    ↓

identify

    ↓

metadata

    ↓

database

    ↓

Agent
```



---


## Agent Usage


支持：

- 查找模型
- 检查缺失
- 推荐模型
- 判断兼容性
