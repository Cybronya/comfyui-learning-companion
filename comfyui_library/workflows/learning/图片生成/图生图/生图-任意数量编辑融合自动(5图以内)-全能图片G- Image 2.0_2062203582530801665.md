---
key: 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2062203582530801665.json
name: 生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2062203582530801665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2062203582530801665.json
hash: fe41df1a424511a1
coverage: 0.512195
learned_at: 2026-10-23 13:14:48
nodes: [StringFunction|pysssss, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, SetNode, GetNode, easy saveText, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy positive, ImageLoader, easy int, SaveImage, ImageBatchMulti, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetImageSizeAndCount, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy positive, easy int, SimpleMath+, CM_IntUnaryOperation, RH_LLMAPI_NODE, Qwen3VL_Advanced, RH_LLMAPI_NODE, GetNode, Note, easy anythingIndexSwitch, GetNode, PrimitiveString, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, GetNode, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, MemoryCleaner, SetNode, easy anythingIndexSwitch, easy anythingIndexSwitch, easy showAnything, easy seed, easy anythingInversedSwitch, SetNode, Reroute, easy anythingInversedSwitch, StringFunction|pysssss, RH_LLMAPI_Pro_Node, GetNode, RH_LLMAPI_Pro_Node, GetNode, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2062203582530801665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2062203582530801665.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（82 个）：
- `StringFunction|pysssss`
- `ImageLoader`
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
- `GetNode`
- `easy saveText`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy positive`
- `ImageLoader`
- `easy int`
- `SaveImage`
- `ImageBatchMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy positive`
- `easy int`
- `SimpleMath+`
- `CM_IntUnaryOperation`
- `RH_LLMAPI_NODE`
- `Qwen3VL_Advanced`
- `RH_LLMAPI_NODE`
- `GetNode`
- `Note`
- `easy anythingIndexSwitch`
- `GetNode`
- `PrimitiveString`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `GetNode`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `MemoryCleaner`
- `SetNode`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `easy seed`
- `easy anythingInversedSwitch`
- `SetNode`
- `Reroute`
- `easy anythingInversedSwitch`
- `StringFunction|pysssss`
- `RH_LLMAPI_Pro_Node`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `GetNode`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **51%**（42/82）

**有卡**：`StringFunction|pysssss`、`ImageLoader`、`ImageScaleToTotalPixels`、`easy saveText`、`easy positive`、`easy int`、`SaveImage`、`ImageBatchMulti`、`GetImageSizeAndCount`、`SimpleMath+`、`CM_IntUnaryOperation`、`RH_LLMAPI_NODE`、`Qwen3VL_Advanced`、`easy anythingIndexSwitch`、`RH_RhartImageG2ImageToImage`、`MemoryCleaner`、`easy seed`、`easy anythingInversedSwitch`、`RH_LLMAPI_Pro_Node`

**用到的条目**：easy seed、GetImageSizeAndCount、SaveImage、easy saveText、ImageBatchMulti、ImageScaleToTotalPixels、RH_LLMAPI_NODE、RH_LLMAPI_Pro_Node
