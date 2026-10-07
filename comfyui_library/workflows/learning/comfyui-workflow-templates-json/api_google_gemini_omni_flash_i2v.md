---
key: comfyui-workflow-templates-json/api_google_gemini_omni_flash_i2v.json
name: api_google_gemini_omni_flash_i2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_google_gemini_omni_flash_i2v.json
hash: 7f268cc3bd406dbb
official: true
coverage: 0.571429
learned_at: 2026-10-07 21:33:41
nodes: [SaveVideo, PreviewAny, LoadImage, LoadImage, MarkdownNote, b83478ba-1f3e-4e62-9869-c8a0c8e9a5f5, GeminiVideoOmniV2]
patterns: []
missing: [b83478ba-1f3e-4e62-9869-c8a0c8e9a5f5]
discoveries: [次要节点 `b83478ba-1f3e-4e62-9869-c8a0c8e9a5f5` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_google_gemini_omni_flash_i2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_google_gemini_omni_flash_i2v.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `SaveVideo`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `b83478ba-1f3e-4e62-9869-c8a0c8e9a5f5`
- `GeminiVideoOmniV2`

## 知识

覆盖率 **57%**（4/7）

**有卡**：`SaveVideo`、`LoadImage`、`GeminiVideoOmniV2`

**缺卡**（1）：`b83478ba-1f3e-4e62-9869-c8a0c8e9a5f5`

**用到的条目**：LoadImage、SaveVideo、GeminiVideoOmniV2、sd15-t2i-basic、sd15-t2i-lora、v2、SaveImage、CS_Preview_Any

## 学习发现

- 次要节点 `b83478ba-1f3e-4e62-9869-c8a0c8e9a5f5` 知识库中没有该节点类型的任何知识
