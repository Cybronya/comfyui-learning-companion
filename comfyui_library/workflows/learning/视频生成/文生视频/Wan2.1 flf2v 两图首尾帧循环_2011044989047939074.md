---
key: 视频生成/文生视频/Wan2.1 flf2v 两图首尾帧循环_2011044989047939074.json
name: Wan2.1 flf2v 两图首尾帧循环_2011044989047939074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 flf2v 两图首尾帧循环_2011044989047939074.json
hash: 1cd771fd642ee3f1
coverage: 0.8125
learned_at: 2026-10-15 22:47:08
nodes: [ImageResizeKJv2, easy boolean, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, easy forLoopEnd, easy showAnything, VHS_VideoCombine, Note, JWImageExtractFromBatch, JWInteger, easy compare, easy showAnything, JWImageExtractFromBatch, VAELoader, CLIPVisionLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, ModelSamplingSD3, SimpleMath+, MathExpression|pysssss, MathExpression|pysssss, CLIPVisionEncode, VAEDecode, CLIPLoader, WanFirstLastFrameToVideo, ImageResizeKJv2, easy ifElse, INTConstant, INTConstant, KSampler, UNETLoader, PreviewImage, LoraLoaderModelOnly, ImageBatchExtendWithOverlap, PrimitiveStringMultiline, easy forLoopStart, Text Load Line From File, PreviewImage, JWInteger, JjkText, JWStringConcat, RHBatchImages:, easy mathInt, IntToText, RHUploadZip, easy imageCount]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 648429145360997, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.1 flf2v 两图首尾帧循环_2011044989047939074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1 flf2v 两图首尾帧循环_2011044989047939074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `ImageResizeKJv2`
- `easy boolean`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy forLoopEnd`
- `easy showAnything`
- `VHS_VideoCombine`
- `Note`
- `JWImageExtractFromBatch`
- `JWInteger`
- `easy compare`
- `easy showAnything`
- `JWImageExtractFromBatch`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `SimpleMath+`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `WanFirstLastFrameToVideo`
- `ImageResizeKJv2`
- `easy ifElse`
- `INTConstant`
- `INTConstant`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `ImageBatchExtendWithOverlap`
- `PrimitiveStringMultiline`
- `easy forLoopStart`
- `Text Load Line From File`
- `PreviewImage`
- `JWInteger`
- `JjkText`
- `JWStringConcat`
- `RHBatchImages:`
- `easy mathInt`
- `IntToText`
- `RHUploadZip`
- `easy imageCount`

## 关键参数

- `seed` = `648429145360997`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`ImageResizeKJv2`、`easy boolean`、`VHS_VideoCombine`、`easy forLoopEnd`、`JWImageExtractFromBatch`、`JWInteger`、`easy compare`、`VAELoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`ModelSamplingSD3`、`SimpleMath+`、`MathExpression|pysssss`、`VAEDecode`、`CLIPLoader`、`WanFirstLastFrameToVideo`、`INTConstant`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageBatchExtendWithOverlap`、`easy forLoopStart`、`Text Load Line From File`、`JWStringConcat`、`RHBatchImages:`、`easy mathInt`、`IntToText`、`RHUploadZip`、`easy imageCount`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
