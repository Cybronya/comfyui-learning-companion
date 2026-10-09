---
key: 图片生成/文生图/gemini-3-pro 图像反推 + 全能图片G2.0 【公式版】_1922305291264675842.json
name: gemini-3-pro 图像反推 + 全能图片G2.0 【公式版】_1922305291264675842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/gemini-3-pro 图像反推 + 全能图片G2.0 【公式版】_1922305291264675842.json
hash: 07dc40f817e44c35
coverage: 0.45
learned_at: 2026-10-07 22:22:29
nodes: [LoadImage, JjkText, easy saveText, easy showAnything, easy showAnything, easy showAnything, JjkText, SaveImage, SaveImage, SaveImage, SaveImage, RH_Captioner_Pro, RH_Captioner_Pro, AspectRatioSelect, RH_RhartImageG2TextToImage, CR Text Replace, easy saveText, easy showAnything, easy showAnything, easy showAnything, RH_Captioner_Pro, RH_Captioner_Pro, CR Text Replace, easy saveText, easy showAnything, easy showAnything, easy showAnything, RH_Captioner_Pro, RH_Captioner_Pro, CR Text Replace, easy saveText, easy showAnything, easy showAnything, easy showAnything, RH_Captioner_Pro, RH_Captioner_Pro, CR Text Replace, RH_RhartImageG2TextToImage, RH_RhartImageG2TextToImage, RH_RhartImageG2TextToImage]
patterns: []
missing: [CR Text Replace, CR Text Replace, CR Text Replace, CR Text Replace, easy saveText, easy saveText, easy saveText, easy saveText]
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/gemini-3-pro 图像反推 + 全能图片G2.0 【公式版】_1922305291264675842.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1922305291264675842.json`

## 结构

**生成流程**：Output → Other

**节点**（40 个）：
- `LoadImage`
- `JjkText`
- `easy saveText`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `JjkText`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `RH_Captioner_Pro`
- `RH_Captioner_Pro`
- `AspectRatioSelect`
- `RH_RhartImageG2TextToImage`
- `CR Text Replace`
- `easy saveText`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `RH_Captioner_Pro`
- `RH_Captioner_Pro`
- `CR Text Replace`
- `easy saveText`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `RH_Captioner_Pro`
- `RH_Captioner_Pro`
- `CR Text Replace`
- `easy saveText`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `RH_Captioner_Pro`
- `RH_Captioner_Pro`
- `CR Text Replace`
- `RH_RhartImageG2TextToImage`
- `RH_RhartImageG2TextToImage`
- `RH_RhartImageG2TextToImage`

## 知识

覆盖率 **45%**（18/40）

**有卡**：`LoadImage`、`SaveImage`、`RH_Captioner_Pro`、`AspectRatioSelect`、`RH_RhartImageG2TextToImage`

**缺卡**（8）：`CR Text Replace`、`CR Text Replace`、`CR Text Replace`、`CR Text Replace`、`easy saveText`、`easy saveText`、`easy saveText`、`easy saveText`

**用到的条目**：LoadImage、SaveImage、RH_RhartImageG2TextToImage、AspectRatioSelect、RH_Captioner_Pro、sd15-t2i-basic、sd15-t2i-lora、SaveText

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
