---
key: 视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json
name: Wan2.2-3图首尾帧循环_2007695996830097409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json
hash: fa5824dc6123b4e6
coverage: 0.689189
learned_at: 2026-10-11 03:07:12
nodes: [IntToText, JjkText, easy mathInt, Int, Int, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, INTConstant, INTConstant, CLIPTextEncode, KSamplerAdvanced, VAEDecode, TrimVideoLatent, VAELoader, LoadImage, Text Load Line From File, RHExtractImage, RHExtractImage, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, RHExtractImage, JWStringConcat, easy mathInt, JWInteger, RHBatchImages:, KSamplerAdvanced, Compare, easy boolean, easy showAnything, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, LoraLoaderModelOnly, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy forLoopEnd, easy forLoopStart, easy ifElse, UNETLoader, easy imageCount, easy showAnything, LoraLoaderModelOnly, VHS_VideoCombine, WanAdvancedI2V, RHUploadZip, PrimitiveStringMultiline, PreviewImage, VHS_VideoInfoSource, LayerUtility: PurgeVRAM V2, HunyuanVideoFoley, RH_Translator, VHS_LoadVideo, Note, PreviewImage, JWInteger, PreviewImage, SimpleMath+, JWInteger, ImageBatchExtendWithOverlap, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, RHBatchImages:, SimpleMath+, Text Load Line From File, easy boolean, easy forLoopEnd, easy forLoopStart, easy imageCount, easy mathInt, easy mathInt]
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RHBatchImages:` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `IntToText`
- `JjkText`
- `easy mathInt`
- `Int`
- `Int`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VAELoader`
- `LoadImage`
- `Text Load Line From File`
- `RHExtractImage`
- `RHExtractImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `RHExtractImage`
- `JWStringConcat`
- `easy mathInt`
- `JWInteger`
- `RHBatchImages:`
- `KSamplerAdvanced` ★核心
- `Compare`
- `easy boolean`
- `easy showAnything`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `UNETLoader` ★核心
- `easy imageCount`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `WanAdvancedI2V`
- `RHUploadZip`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `VHS_VideoInfoSource`
- `LayerUtility: PurgeVRAM V2`
- `HunyuanVideoFoley`
- `RH_Translator`
- `VHS_LoadVideo`
- `Note`
- `PreviewImage`
- `JWInteger`
- `PreviewImage`
- `SimpleMath+`
- `JWInteger`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（51/74）

**有卡**：`IntToText`、`Int`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`INTConstant`、`KSamplerAdvanced`、`VAEDecode`、`TrimVideoLatent`、`VAELoader`、`LoadImage`、`RHExtractImage`、`ImageResizeKJv2`、`JWStringConcat`、`JWInteger`、`Compare`、`ImageFromBatch`、`VHS_VideoCombine`、`UNETLoader`、`WanAdvancedI2V`、`RHUploadZip`、`VHS_VideoInfoSource`、`HunyuanVideoFoley`、`RH_Translator`、`VHS_LoadVideo`、`ImageBatchExtendWithOverlap`

**缺卡**（13）：`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`RHBatchImages:`、`SimpleMath+`、`Text Load Line From File`、`easy boolean`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageCount`、`easy mathInt`、`easy mathInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RHBatchImages:` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
