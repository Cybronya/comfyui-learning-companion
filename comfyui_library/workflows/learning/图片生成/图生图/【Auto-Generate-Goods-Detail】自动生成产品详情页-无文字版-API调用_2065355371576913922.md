---
key: 图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-无文字版-API调用_2065355371576913922.json
name: 【Auto-Generate-Goods-Detail】自动生成产品详情页-无文字版-API调用_2065355371576913922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-无文字版-API调用_2065355371576913922.json
hash: 8dc794ee1d4021a8
coverage: 0.241379
learned_at: 2026-10-09 22:36:21
nodes: [PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, PrimitiveString, ZML_MergeText, easy promptLine, easy showAnything, easy showAnything, easy promptLine, LoadImagesFromURL, LoadImagesFromURL, LoadImagesFromURL, LoadImagesFromURL, Reroute, Reroute, Reroute, Reroute, Reroute, LoadMultiImage, Reroute, easy showAnything, LoadImagesFromURL, Text Multiline, Reroute, RH_LLMAPI_Pro_Node, Text Find and Replace, RH_LLMAPI_Pro_Node, easy showAnything, PrimitiveString, PrimitiveString, easy showAnything, Text Multiline, JjkText, easy showAnything, LoadImagesFromURL, PrimitiveString, SaveImage, RH_RhartImageG2ImageToImage, RH_Nano_Banana2_Image2Image, PrimitiveString, CR String To Combo, SaveImage]
patterns: []
missing: [CR String To Combo, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, Text Find and Replace, Text Multiline, Text Multiline, easy promptLine, easy promptLine]
discoveries: [次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-无文字版-API调用_2065355371576913922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2065355371576913922.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（58 个）：
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `PrimitiveString`
- `ZML_MergeText`
- `easy promptLine`
- `easy showAnything`
- `easy showAnything`
- `easy promptLine`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `LoadImagesFromURL`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadMultiImage`
- `Reroute`
- `easy showAnything`
- `LoadImagesFromURL`
- `Text Multiline`
- `Reroute`
- `RH_LLMAPI_Pro_Node`
- `Text Find and Replace`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `PrimitiveString`
- `PrimitiveString`
- `easy showAnything`
- `Text Multiline`
- `JjkText`
- `easy showAnything`
- `LoadImagesFromURL`
- `PrimitiveString`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `RH_Nano_Banana2_Image2Image`
- `PrimitiveString`
- `CR String To Combo`
- `SaveImage`

## 知识

覆盖率 **24%**（14/58）

**有卡**：`ZML_MergeText`、`LoadImagesFromURL`、`LoadMultiImage`、`RH_LLMAPI_Pro_Node`、`SaveImage`、`RH_RhartImageG2ImageToImage`、`RH_Nano_Banana2_Image2Image`

**缺卡**（14）：`CR String To Combo`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`Text Find and Replace`、`Text Multiline`、`Text Multiline`、`easy promptLine`、`easy promptLine`

**用到的条目**：SaveImage、RH_LLMAPI_Pro_Node、RH_RhartImageG2ImageToImage、RH_Nano_Banana2_Image2Image、LoadImagesFromURL、LoadMultiImage、ZML_MergeText、sd15-t2i-basic

## 学习发现

- 次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
