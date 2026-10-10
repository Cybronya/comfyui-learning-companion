---
key: Seedream 4.0 -即梦4.0-白底图生成背景_1967932874005577730.json
name: Seedream 4.0 -即梦4.0-白底图生成背景_1967932874005577730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedream 4.0 -即梦4.0-白底图生成背景_1967932874005577730.json
hash: 86dd6cf7235f5433
coverage: 0.423077
learned_at: 2026-10-10 20:59:12
nodes: [RH_Captioner, CR Text Concatenate, LoadImage, ShowText|pysssss, ShowText|pysssss, SaveImage, Image Comparer (rgthree), RH_Jimeng4_Image2Image, LoadImage, RH_Captioner, Note, CR Text, CR Text, RH_LLMAPI_NODE, CR Text Concatenate, Note, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy textIndexSwitch, LoadImage, LoadImage, LoadImage, ShowText|pysssss, PreviewImage, PreviewImage, RHHiddenNodes]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, easy textIndexSwitch]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识]
---

# Seedream 4.0 -即梦4.0-白底图生成背景_1967932874005577730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Seedream 4.0 -即梦4.0-白底图生成背景_1967932874005577730.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（26 个）：
- `RH_Captioner`
- `CR Text Concatenate`
- `LoadImage`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RH_Jimeng4_Image2Image`
- `LoadImage`
- `RH_Captioner`
- `Note`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_NODE`
- `CR Text Concatenate`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy textIndexSwitch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ShowText|pysssss`
- `PreviewImage`
- `PreviewImage`
- `RHHiddenNodes`

## 知识

覆盖率 **42%**（11/26）

**有卡**：`RH_Captioner`、`LoadImage`、`SaveImage`、`RH_Jimeng4_Image2Image`、`RH_LLMAPI_NODE`、`RHHiddenNodes`

**缺卡**（5）：`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`easy textIndexSwitch`

**用到的条目**：LoadImage、SaveImage、RH_Captioner、RH_LLMAPI_NODE、RHHiddenNodes、RH_Jimeng4_Image2Image、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识
