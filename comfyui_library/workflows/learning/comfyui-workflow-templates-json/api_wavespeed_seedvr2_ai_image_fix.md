---
key: comfyui-workflow-templates-json/api_wavespeed_seedvr2_ai_image_fix.json
name: api_wavespeed_seedvr2_ai_image_fix
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_wavespeed_seedvr2_ai_image_fix.json
hash: 463b72878cfa63aa
official: true
coverage: 0.8
learned_at: 2026-10-10 22:46:51
nodes: [MarkdownNote, ImageCompare, SaveImage, WavespeedImageUpscaleNode, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_wavespeed_seedvr2_ai_image_fix.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_wavespeed_seedvr2_ai_image_fix.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `MarkdownNote`
- `ImageCompare`
- `SaveImage`
- `WavespeedImageUpscaleNode`
- `LoadImage`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`ImageCompare`、`SaveImage`、`WavespeedImageUpscaleNode`、`LoadImage`

**用到的条目**：LoadImage、WavespeedImageUpscaleNode、SaveImage、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、node、scale
