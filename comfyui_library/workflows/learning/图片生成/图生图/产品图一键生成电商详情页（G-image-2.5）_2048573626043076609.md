---
key: 图片生成/图生图/产品图一键生成电商详情页（G-image-2.5）_2048573626043076609.json
name: 产品图一键生成电商详情页（G-image-2.5）_2048573626043076609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/产品图一键生成电商详情页（G-image-2.5）_2048573626043076609.json
hash: bf37dc468a556685
coverage: 0.283582
learned_at: 2026-10-10 20:48:14
nodes: [easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, Note, PrimitiveStringMultiline, Note, Note, TextSplitByDelimiterEnhanced, ShowText|pysssss, ShowText|pysssss, LoadImage, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ShowText|pysssss, PrimitiveStringMultiline, RH_RhartImageG2ImageToImage, RH_RhartImageG2OfficialImageToImage, SaveImage, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, JoinStringMulti, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, ShowText|pysssss, RH_LLMAPI_Pro_Node, ShowText|pysssss, PrimitiveStringMultiline, ShowText|pysssss, easy showAnything, LoadImage, RHHiddenNodes, PreviewImage, easy int, SaveImage, SaveImage, PreviewImage, LoadImage, LoadImage, LoadImage, RH_RhartImageG25FlareImageToImage, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, Note, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, easy promptConcat, RH_RhartImageG25SunburstImageToImage, PreviewImage]
patterns: []
missing: [easy int, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat]
discoveries: [次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/产品图一键生成电商详情页（G-image-2.5）_2048573626043076609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/产品图一键生成电商详情页（G-image-2.5）_2048573626043076609.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（67 个）：
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `Note`
- `PrimitiveStringMultiline`
- `Note`
- `Note`
- `TextSplitByDelimiterEnhanced`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `JoinStringMulti`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `easy showAnything`
- `LoadImage`
- `RHHiddenNodes`
- `PreviewImage`
- `easy int`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG25FlareImageToImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `RH_RhartImageG25SunburstImageToImage`
- `PreviewImage`

## 知识

覆盖率 **28%**（19/67）

**有卡**：`TextSplitByDelimiterEnhanced`、`LoadImage`、`RH_RhartImageG2ImageToImage`、`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`JoinStringMulti`、`RHHiddenNodes`、`RH_RhartImageG25FlareImageToImage`、`RH_RhartImageG25SunburstImageToImage`

**缺卡**（12）：`easy int`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`、`easy promptConcat`

**用到的条目**：LoadImage、SaveImage、JoinStringMulti、RH_LLMAPI_Pro_Node、RH_RhartImageG25FlareImageToImage、RH_RhartImageG25SunburstImageToImage、RH_RhartImageG2ImageToImage、RH_RhartImageG2OfficialImageToImage

## 学习发现

- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
