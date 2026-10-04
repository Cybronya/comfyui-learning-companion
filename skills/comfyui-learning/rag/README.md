# ComfyUI RAG Skill


## Purpose


建立 ComfyUI 专用知识检索系统。


---


## Input


- workflow_manifest
- node_database
- model_database



---


## Output


- Vector Index
- Search API



---


## Example


用户：


找一个 FLUX 图片生成 workflow



RAG:


搜索：

```
Workflow

    ↓

Node

    ↓

Model
```


返回结果。
