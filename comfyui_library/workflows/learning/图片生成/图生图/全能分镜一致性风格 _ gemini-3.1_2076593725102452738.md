---
key: 图片生成/图生图/全能分镜一致性风格 _ gemini-3.1_2076593725102452738.json
name: 全能分镜一致性风格 _ gemini-3.1_2076593725102452738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能分镜一致性风格 _ gemini-3.1_2076593725102452738.json
hash: ba9cf80018684930
coverage: 0.625
learned_at: 2026-10-10 20:48:14
nodes: [ProcessString, easy showAnything, SaveImage, RH_Nano_Banana2_Gemini31Flash, RH_LLMAPI_Pro_Node, easy promptLine, JjkText, LoadImage]
patterns: []
missing: [easy promptLine]
discoveries: [次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/全能分镜一致性风格 _ gemini-3.1_2076593725102452738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全能分镜一致性风格 _ gemini-3.1_2076593725102452738.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `ProcessString`
- `easy showAnything`
- `SaveImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_LLMAPI_Pro_Node`
- `easy promptLine`
- `JjkText`
- `LoadImage`

## 知识

覆盖率 **62%**（5/8）

**有卡**：`ProcessString`、`SaveImage`、`RH_Nano_Banana2_Gemini31Flash`、`RH_LLMAPI_Pro_Node`、`LoadImage`

**缺卡**（1）：`easy promptLine`

**用到的条目**：LoadImage、SaveImage、ProcessString、RH_LLMAPI_Pro_Node、RH_Nano_Banana2_Gemini31Flash、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
