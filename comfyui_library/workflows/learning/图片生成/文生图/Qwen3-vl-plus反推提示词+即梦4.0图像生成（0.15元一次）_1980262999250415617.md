---
key: Qwen3-vl-plus反推提示词+即梦4.0图像生成（0.15元一次）_1980262999250415617.json
name: Qwen3-vl-plus反推提示词+即梦4.0图像生成（0.15元一次）_1980262999250415617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen3-vl-plus反推提示词+即梦4.0图像生成（0.15元一次）_1980262999250415617.json
hash: a9fd5eac737b1f22
coverage: 0.590909
learned_at: 2026-10-10 20:59:07
nodes: [MarkdownNote, LoadImage, easy anythingIndexSwitch, CR Text Concatenate, String, String, String, String, String, RH_Jimeng4_Image2Image, RH_Captioner_Pro, MarkdownNote, PrimitiveInt, PreviewImage, SaveImage, String, String, String, ShowText|pysssss, easy saveText, easy saveText, LoadImage]
patterns: []
missing: [CR Text Concatenate, easy anythingIndexSwitch, easy saveText, easy saveText]
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# Qwen3-vl-plus反推提示词+即梦4.0图像生成（0.15元一次）_1980262999250415617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen3-vl-plus反推提示词+即梦4.0图像生成（0.15元一次）_1980262999250415617.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（22 个）：
- `MarkdownNote`
- `LoadImage`
- `easy anythingIndexSwitch`
- `CR Text Concatenate`
- `String`
- `String`
- `String`
- `String`
- `String`
- `RH_Jimeng4_Image2Image`
- `RH_Captioner_Pro`
- `MarkdownNote`
- `PrimitiveInt`
- `PreviewImage`
- `SaveImage`
- `String`
- `String`
- `String`
- `ShowText|pysssss`
- `easy saveText`
- `easy saveText`
- `LoadImage`

## 知识

覆盖率 **59%**（13/22）

**有卡**：`LoadImage`、`String`、`RH_Jimeng4_Image2Image`、`RH_Captioner_Pro`、`SaveImage`

**缺卡**（4）：`CR Text Concatenate`、`easy anythingIndexSwitch`、`easy saveText`、`easy saveText`

**用到的条目**：LoadImage、SaveImage、RH_Jimeng4_Image2Image、String、RH_Captioner_Pro、sd15-t2i-basic、sd15-t2i-lora、SaveText

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
