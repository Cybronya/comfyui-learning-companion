---
key: comfyui-workflow-templates-json/api_hunyuan3d_model2uv.json
name: api_hunyuan3d_model2uv
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_hunyuan3d_model2uv.json
hash: 809e45670eb67297
official: true
coverage: 0.8
learned_at: 2026-10-10 22:44:26
nodes: [SaveGLB, SaveGLB, TencentModelTo3DUVNode, Load3D, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_hunyuan3d_model2uv.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_hunyuan3d_model2uv.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `SaveGLB`
- `SaveGLB`
- `TencentModelTo3DUVNode`
- `Load3D`
- `MarkdownNote`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`SaveGLB`、`TencentModelTo3DUVNode`、`Load3D`

**用到的条目**：SaveGLB、Load3D、TencentModelTo3DUVNode、sd15-t2i-basic、sd15-t2i-lora、node、SaveImage、CS_Preview_Any
