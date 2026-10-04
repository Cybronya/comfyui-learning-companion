# Node Analysis Skill


## Purpose


建立 ComfyUI Node Knowledge Base。


---


## Output


生成：



node_database.json



结构：

```
Node

|

├── Information
├── Inputs
├── Outputs
├── Category
└── Relationships
```



---


## Usage


Agent 可以：

- 查询节点
- 分析 Workflow
- 推荐节点
- 生成 Workflow


---


## Pipeline

```
ComfyUI

    ↓

scan nodes

    ↓

extract metadata

    ↓

build database

    ↓

Agent knowledge
```
