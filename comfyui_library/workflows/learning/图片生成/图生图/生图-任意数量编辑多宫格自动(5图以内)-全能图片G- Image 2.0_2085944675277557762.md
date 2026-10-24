---
key: 图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762.json
name: 生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762.json
hash: 8f5e995f778affa3
coverage: 0.512195
learned_at: 2026-10-23 13:14:45
nodes: [StringFunction|pysssss, ImageLoader, ImageLoader, ImageLoader, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, SetNode, easy saveText, SetNode, SetNode, GetNode, SetNode, ImageLoader, easy int, ImageBatchMulti, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, GetNode, GetNode, GetNode, SimpleMath+, CM_IntUnaryOperation, Qwen3VL_Advanced, RH_LLMAPI_NODE, GetNode, GetNode, PrimitiveString, GetNode, MemoryCleaner, SetNode, easy seed, SetNode, Reroute, easy anythingInversedSwitch, SetNode, StringFunction|pysssss, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, easy showAnything, easy anythingIndexSwitch, easy anythingIndexSwitch, easy positive, PreviewImage, Note, GetNode, easy anythingIndexSwitch, ImageLoader, easy int, RH_RhartImageG2ImageToImage, SaveImage, GetNode, GetNode, GetNode, easy anythingInversedSwitch, GetNode, easy positive, RH_RhartImageG2ImageToImage, GetNode, RH_LLMAPI_Pro_Node, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, GetNode, RH_LLMAPI_Pro_Node, GetNode]
patterns: []
missing: []
---

# 图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（82 个）：
- `StringFunction|pysssss`
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy saveText`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageLoader`
- `easy int`
- `ImageBatchMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `CM_IntUnaryOperation`
- `Qwen3VL_Advanced`
- `RH_LLMAPI_NODE`
- `GetNode`
- `GetNode`
- `PrimitiveString`
- `GetNode`
- `MemoryCleaner`
- `SetNode`
- `easy seed`
- `SetNode`
- `Reroute`
- `easy anythingInversedSwitch`
- `SetNode`
- `StringFunction|pysssss`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy positive`
- `PreviewImage`
- `Note`
- `GetNode`
- `easy anythingIndexSwitch`
- `ImageLoader`
- `easy int`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy anythingInversedSwitch`
- `GetNode`
- `easy positive`
- `RH_RhartImageG2ImageToImage`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `GetNode`

## 知识

覆盖率 **51%**（42/82）

**有卡**：`StringFunction|pysssss`、`ImageLoader`、`ImageScaleToTotalPixels`、`easy saveText`、`easy int`、`ImageBatchMulti`、`GetImageSizeAndCount`、`SimpleMath+`、`CM_IntUnaryOperation`、`Qwen3VL_Advanced`、`RH_LLMAPI_NODE`、`MemoryCleaner`、`easy seed`、`easy anythingInversedSwitch`、`RH_RhartImageG2ImageToImage`、`easy anythingIndexSwitch`、`easy positive`、`SaveImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：easy seed、GetImageSizeAndCount、SaveImage、easy saveText、ImageBatchMulti、ImageScaleToTotalPixels、RH_LLMAPI_NODE、RH_LLMAPI_Pro_Node
