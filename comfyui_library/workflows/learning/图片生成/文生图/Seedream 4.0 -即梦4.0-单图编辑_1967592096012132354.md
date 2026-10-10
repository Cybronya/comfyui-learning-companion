---
key: Seedream 4.0 -即梦4.0-单图编辑_1967592096012132354.json
name: Seedream 4.0 -即梦4.0-单图编辑_1967592096012132354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedream 4.0 -即梦4.0-单图编辑_1967592096012132354.json
hash: b26fdd9ca092841e
coverage: 0.75
learned_at: 2026-10-10 20:59:12
nodes: [SaveImage, LoadImage, RH_Jimeng4_Image2Image, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# Seedream 4.0 -即梦4.0-单图编辑_1967592096012132354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Seedream 4.0 -即梦4.0-单图编辑_1967592096012132354.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（4 个）：
- `SaveImage`
- `LoadImage`
- `RH_Jimeng4_Image2Image`
- `CR Prompt Text`

## 知识

覆盖率 **75%**（3/4）

**有卡**：`SaveImage`、`LoadImage`、`RH_Jimeng4_Image2Image`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveImage、RH_Jimeng4_Image2Image、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
