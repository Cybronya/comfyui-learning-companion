---
key: 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121.json
name: 生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121.json
hash: 3925b28e176bffa6
coverage: 0.488636
learned_at: 2026-10-23 13:14:48
nodes: [StringFunction|pysssss, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, SetNode, StringFunction|pysssss, GetNode, easy saveText, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy positive, ImageLoader, easy int, SaveImage, ImageBatchMulti, GetNode, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetImageSizeAndCount, PreviewImage, GetNode, easy anythingInversedSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MemoryCleaner, SetNode, easy showAnything, easy showAnything, SetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveString, Note, GetNode, GetNode, RH_GPT_Image15, RH_GPT_Image15, RH_GPT_Image15, RH_GPT_Image15, GetNode, easy positive, easy anythingIndexSwitch, easy int, SimpleMath+, CM_IntUnaryOperation, RH_LLMAPI_NODE, Qwen3VL_Advanced, RH_LLMAPI_NODE, RH_LLMAPI_NODE, RH_LLMAPI_NODE, GetNode, GetNode, RH_LLMAPI_NODE, ImageConcanate, GetNode, easy seed, GetNode, RH_GPT_Image15, easy anythingIndexSwitch, easy anythingIndexSwitch, Reroute, SetNode, easy anythingInversedSwitch]
patterns: []
missing: []
---

# 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121.json`

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
- `easy anythingInversedSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MemoryCleaner`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveString`
- `Note`
- `GetNode`
- `GetNode`
- `RH_GPT_Image15`
- `RH_GPT_Image15`
- `RH_GPT_Image15`
- `RH_GPT_Image15`
- `GetNode`
- `easy positive`
- `easy anythingIndexSwitch`
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
- `RH_LLMAPI_NODE`
- `ImageConcanate`
- `GetNode`
- `easy seed`
- `GetNode`
- `RH_GPT_Image15`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `Reroute`
- `SetNode`
- `easy anythingInversedSwitch`

## 知识

覆盖率 **49%**（43/88）

**有卡**：`StringFunction|pysssss`、`ImageLoader`、`ImageScaleToTotalPixels`、`easy saveText`、`easy positive`、`easy int`、`SaveImage`、`ImageBatchMulti`、`GetImageSizeAndCount`、`easy anythingInversedSwitch`、`MemoryCleaner`、`RH_GPT_Image15`、`easy anythingIndexSwitch`、`SimpleMath+`、`CM_IntUnaryOperation`、`RH_LLMAPI_NODE`、`Qwen3VL_Advanced`、`ImageConcanate`、`easy seed`

**用到的条目**：easy seed、GetImageSizeAndCount、SaveImage、easy saveText、ImageBatchMulti、ImageConcanate、ImageScaleToTotalPixels、RH_LLMAPI_NODE
