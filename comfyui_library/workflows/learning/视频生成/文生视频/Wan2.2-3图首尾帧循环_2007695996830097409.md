---
key: 视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json
name: Wan2.2-3图首尾帧循环_2007695996830097409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json
hash: fa5824dc6123b4e6
coverage: 0.864865
learned_at: 2026-10-15 22:47:12
nodes: [IntToText, JjkText, easy mathInt, Int, Int, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, INTConstant, INTConstant, CLIPTextEncode, KSamplerAdvanced, VAEDecode, TrimVideoLatent, VAELoader, LoadImage, Text Load Line From File, RHExtractImage, RHExtractImage, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, RHExtractImage, JWStringConcat, easy mathInt, JWInteger, RHBatchImages:, KSamplerAdvanced, Compare, easy boolean, easy showAnything, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, LoraLoaderModelOnly, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy forLoopEnd, easy forLoopStart, easy ifElse, UNETLoader, easy imageCount, easy showAnything, LoraLoaderModelOnly, VHS_VideoCombine, WanAdvancedI2V, RHUploadZip, PrimitiveStringMultiline, PreviewImage, VHS_VideoInfoSource, LayerUtility: PurgeVRAM V2, HunyuanVideoFoley, RH_Translator, VHS_LoadVideo, Note, PreviewImage, JWInteger, PreviewImage, SimpleMath+, JWInteger, ImageBatchExtendWithOverlap, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
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

覆盖率 **86%**（64/74）

**有卡**：`IntToText`、`easy mathInt`、`Int`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`INTConstant`、`KSamplerAdvanced`、`VAEDecode`、`TrimVideoLatent`、`VAELoader`、`LoadImage`、`Text Load Line From File`、`RHExtractImage`、`ImageResizeKJv2`、`JWStringConcat`、`JWInteger`、`RHBatchImages:`、`Compare`、`easy boolean`、`ImageFromBatch`、`VHS_VideoCombine`、`MathExpression|pysssss`、`UNETLoader`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageCount`、`WanAdvancedI2V`、`RHUploadZip`、`VHS_VideoInfoSource`、`LayerUtility: PurgeVRAM V2`、`HunyuanVideoFoley`、`RH_Translator`、`VHS_LoadVideo`、`SimpleMath+`、`ImageBatchExtendWithOverlap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
