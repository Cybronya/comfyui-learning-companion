---
key: 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2066055876622217216.json
name: 生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2066055876622217216
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2066055876622217216.json
hash: dc2dae7582be40b7
coverage: 0.488636
learned_at: 2026-10-23 13:14:49
nodes: [StringFunction|pysssss, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, SetNode, StringFunction|pysssss, GetNode, easy saveText, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy positive, ImageLoader, easy int, SaveImage, ImageBatchMulti, GetNode, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetImageSizeAndCount, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy positive, easy int, SimpleMath+, CM_IntUnaryOperation, RH_LLMAPI_NODE, Qwen3VL_Advanced, RH_LLMAPI_NODE, RH_LLMAPI_NODE, RH_LLMAPI_NODE, GetNode, GetNode, ImageConcanate, GetNode, Note, easy anythingIndexSwitch, GetNode, PrimitiveString, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, GetNode, GetNode, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, RH_LLMAPI_NODE, MemoryCleaner, SetNode, easy anythingIndexSwitch, easy anythingIndexSwitch, easy showAnything, easy seed, easy anythingInversedSwitch, GetNode, SetNode, Reroute, easy anythingInversedSwitch]
patterns: []
missing: []
---

# 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2066055876622217216.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2066055876622217216.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（88 个）：
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
- `StringFunction|pysssss`
- `GetNode`
- `easy saveText`
- `SetNode`
- `SetNode`
- `GetNode`
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
- `GetNode`
- `easy positive`
- `easy int`
- `SimpleMath+`
- `CM_IntUnaryOperation`
- `RH_LLMAPI_NODE`
- `Qwen3VL_Advanced`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `Note`
- `easy anythingIndexSwitch`
- `GetNode`
- `PrimitiveString`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `GetNode`
- `GetNode`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `RH_LLMAPI_NODE`
- `MemoryCleaner`
- `SetNode`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `easy seed`
- `easy anythingInversedSwitch`
- `GetNode`
- `SetNode`
- `Reroute`
- `easy anythingInversedSwitch`

## 知识

覆盖率 **49%**（43/88）

**有卡**：`StringFunction|pysssss`、`ImageLoader`、`ImageScaleToTotalPixels`、`easy saveText`、`easy positive`、`easy int`、`SaveImage`、`ImageBatchMulti`、`GetImageSizeAndCount`、`SimpleMath+`、`CM_IntUnaryOperation`、`RH_LLMAPI_NODE`、`Qwen3VL_Advanced`、`ImageConcanate`、`easy anythingIndexSwitch`、`RH_RhartImageG2ImageToImage`、`MemoryCleaner`、`easy seed`、`easy anythingInversedSwitch`

**用到的条目**：easy seed、GetImageSizeAndCount、SaveImage、easy saveText、ImageBatchMulti、ImageConcanate、ImageScaleToTotalPixels、RH_LLMAPI_NODE
