---
key: comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_extend.json
name: api_google_gemini_omni_flash_1_1_extend
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_extend.json
hash: 7e16bebcbfcd4e56
official: true
coverage: 0.6
learned_at: 2026-10-07 21:33:40
nodes: [MarkdownNote, LoadVideo, Video Slice, SaveVideo, GeminiVideoOmniV2]
patterns: []
missing: [Video Slice]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_extend.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_extend.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `MarkdownNote`
- `LoadVideo`
- `Video Slice`
- `SaveVideo`
- `GeminiVideoOmniV2`

## 知识

覆盖率 **60%**（3/5）

**有卡**：`LoadVideo`、`SaveVideo`、`GeminiVideoOmniV2`

**缺卡**（1）：`Video Slice`

**用到的条目**：SaveVideo、LoadVideo、GeminiVideoOmniV2、sd15-t2i-basic、sd15-t2i-lora、v2、SaveImage、CS_Preview_Any

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
