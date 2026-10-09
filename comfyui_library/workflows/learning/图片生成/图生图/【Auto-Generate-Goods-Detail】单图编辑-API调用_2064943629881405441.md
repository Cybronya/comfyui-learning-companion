---
key: 图片生成/图生图/【Auto-Generate-Goods-Detail】单图编辑-API调用_2064943629881405441.json
name: 【Auto-Generate-Goods-Detail】单图编辑-API调用_2064943629881405441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Auto-Generate-Goods-Detail】单图编辑-API调用_2064943629881405441.json
hash: 78942c69f510d086
coverage: 0.571429
learned_at: 2026-10-09 22:36:21
nodes: [Note, CR String To Combo, MUTOU_SmartAspectRatio, Text Multiline, RH_Nano_Banana2_Gemini31Flash, SaveImage, LoadImagesFromURL]
patterns: []
missing: [CR String To Combo, Text Multiline]
discoveries: [次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/【Auto-Generate-Goods-Detail】单图编辑-API调用_2064943629881405441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2064943629881405441.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `Note`
- `CR String To Combo`
- `MUTOU_SmartAspectRatio`
- `Text Multiline`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `LoadImagesFromURL`

## 知识

覆盖率 **57%**（4/7）

**有卡**：`MUTOU_SmartAspectRatio`、`RH_Nano_Banana2_Gemini31Flash`、`SaveImage`、`LoadImagesFromURL`

**缺卡**（2）：`CR String To Combo`、`Text Multiline`

**用到的条目**：SaveImage、RH_Nano_Banana2_Gemini31Flash、LoadImagesFromURL、MUTOU_SmartAspectRatio、sd15-t2i-basic、sd15-t2i-lora、LoadImage、Text

## 学习发现

- 次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
