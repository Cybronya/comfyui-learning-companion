---
key: comfyui-workflow-templates-json/api_seedance2_0_r2v_real_human.json
name: api_seedance2_0_r2v_real_human
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_seedance2_0_r2v_real_human.json
hash: bac47c35251e4733
official: true
coverage: 0.7
learned_at: 2026-10-07 21:34:47
nodes: [LoadImage, ByteDanceCreateImageAsset, MarkdownNote, SaveVideo, MarkdownNote, ByteDanceCreateVideoAsset, MarkdownNote, ByteDance2ReferenceNodeV2, SaveText, SaveText]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_seedance2_0_r2v_real_human.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_seedance2_0_r2v_real_human.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `LoadImage`
- `ByteDanceCreateImageAsset`
- `MarkdownNote`
- `SaveVideo`
- `MarkdownNote`
- `ByteDanceCreateVideoAsset`
- `MarkdownNote`
- `ByteDance2ReferenceNodeV2`
- `SaveText`
- `SaveText`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`LoadImage`、`ByteDanceCreateImageAsset`、`SaveVideo`、`ByteDanceCreateVideoAsset`、`ByteDance2ReferenceNodeV2`、`SaveText`

**用到的条目**：LoadImage、SaveText、SaveVideo、ByteDance2ReferenceNodeV2、ByteDanceCreateImageAsset、ByteDanceCreateVideoAsset、sd15-t2i-basic、sd15-t2i-lora
