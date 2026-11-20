---
key: 平台全量/wan2.2低噪批量洗图-人物去背景洗+seedvr2高清修复(适合人物lora训练洗图)_1968660137688932353.json
name: wan2.2低噪批量洗图-人物去背景洗+seedvr2高清修复(适合人物lora训练洗图)_1968660137688932353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2低噪批量洗图-人物去背景洗+seedvr2高清修复(适合人物lora训练洗图)_1968660137688932353.json
hash: 27a47e628ddbe4f3
coverage: 0.75
learned_at: 2026-11-14 01:19:41
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, UNETLoader, easy forLoopStart, easy showAnything, RHExtractImage, VAEEncode, VAELoader, easy showAnything, SeedVR2BlockSwap, SetNode, SetNode, GetNode, easy forLoopEnd, SeedVR2, SaveImage, SaveImage, VAEDecode, LoraLoaderModelOnly, Text Multiline, PathchSageAttentionKJ, CLIPLoader, Text Concatenate, RH_Captioner, KSampler, RHBatchImages:, PreviewImage, easy imageCount, Bjornulf_ShowInt, SetNode, GetNode, ImageScaleDownToSize, easy imageRemBg, PrimitiveNode, PrimitiveString, Seed (rgthree), RHUploadZip]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 607301946056183, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.2低噪批量洗图-人物去背景洗+seedvr2高清修复(适合人物lora训练洗图)_1968660137688932353.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2低噪批量洗图-人物去背景洗+seedvr2高清修复(适合人物lora训练洗图)_1968660137688932353.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `easy forLoopStart`
- `easy showAnything`
- `RHExtractImage`
- `VAEEncode` ★核心
- `VAELoader`
- `easy showAnything`
- `SeedVR2BlockSwap`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy forLoopEnd`
- `SeedVR2`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `Text Concatenate`
- `RH_Captioner`
- `KSampler` ★核心
- `RHBatchImages:`
- `PreviewImage`
- `easy imageCount`
- `Bjornulf_ShowInt`
- `SetNode`
- `GetNode`
- `ImageScaleDownToSize`
- `easy imageRemBg`
- `PrimitiveNode`
- `PrimitiveString`
- `Seed (rgthree)`
- `RHUploadZip`

## 关键参数

- `seed` = `607301946056183`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **75%**（30/40）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`UNETLoader`、`easy forLoopStart`、`RHExtractImage`、`VAEEncode`、`VAELoader`、`SeedVR2BlockSwap`、`easy forLoopEnd`、`SeedVR2`、`SaveImage`、`VAEDecode`、`Text Multiline`、`PathchSageAttentionKJ`、`CLIPLoader`、`Text Concatenate`、`RH_Captioner`、`KSampler`、`RHBatchImages:`、`easy imageCount`、`Bjornulf_ShowInt`、`ImageScaleDownToSize`、`easy imageRemBg`、`Seed (rgthree)`、`RHUploadZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、Seed (rgthree)

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
