---
key: comfyui-workflow-templates-json/api_kling_omni_i2v.json
name: api_kling_omni_i2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_kling_omni_i2v.json
hash: 0fb27f206cba2bde
official: true
coverage: 1
learned_at: 2026-10-10 22:44:41
nodes: [LoadImage, LoadImage, LoadImage, BatchImagesNode, SaveVideo, KlingOmniProImageToVideoNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_kling_omni_i2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_kling_omni_i2v.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `SaveVideo`
- `KlingOmniProImageToVideoNode`

## 知识

覆盖率 **100%**（6/6）

**有卡**：`LoadImage`、`BatchImagesNode`、`SaveVideo`、`KlingOmniProImageToVideoNode`

**用到的条目**：LoadImage、SaveVideo、BatchImagesNode、KlingOmniProImageToVideoNode、sd15-t2i-basic、sd15-t2i-lora、node、SaveImage
