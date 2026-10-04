# RAG Rules


# 1. Document Types


RAG 管理三类文档。


---


## Workflow Document


来源：

workflow_manifest.json


转换：


- Workflow Name
- Category
- Nodes
- Models
- Description
- Parameters



示例：

```
Wan Character Video

Category:
video_generation

Nodes:
WanVideoLoader
KSampler

Models:
Wan2.1
```



---


## Node Document


来源：

node_database.json


转换：


- Node Name
- Purpose
- Input
- Output
- Category



---


## Model Document


来源：

model_database.json


转换：


- Model Name
- Type
- Architecture
- Compatibility
- Requirement



---

# 2. Metadata Filtering


搜索时支持：


category:

- video_generation
- image_generation


model:

- Wan
- Flux
- SDXL


node:

- ControlNet
- KSampler



---

# 3. Relation Enhancement


建立关系：

```
Workflow

    ↓

uses

    ↓

Node



Workflow

    ↓

requires

    ↓

Model



Node

    ↓

supports

    ↓

Model
```


---

# 4. Ranking

结果排序因素：

semantic similarity + category match + model compatibility + human verified


---

# 5. Human Feedback

用户确认：

- useful
- not useful
- favorite

用于优化后续搜索。
