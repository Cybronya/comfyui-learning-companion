---
key: 视频生成/文生视频/wanduDMDJV1.0_1967613409602801666.json
name: wanduDMDJV1.0_1967613409602801666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wanduDMDJV1.0_1967613409602801666.json
hash: a5467a8955dbe22a
coverage: 0.846154
learned_at: 2026-10-15 22:43:45
nodes: [CLIPTextEncode, VAEDecode, ModelSamplingAuraFlow, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, PathchSageAttentionKJ, KSamplerAdvanced, CLIPTextEncode, ReadExcelData, ShowText|pysssss, easy forLoopStart, easy mathInt, CR Integer To String, Note, PreviewImage, easy showAnything, Text Concatenate, CLIPTextEncode, KSampler, UNETLoader, VAELoader, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, WanImageToVideo, CLIPLoader, UNETLoader, Text Multiline, PlaySound|pysssss, LayerUtility: PurgeVRAM V2, easy forLoopEnd, easy showAnything, easy forLoopStart, RHHiddenNodes, RHHiddenNodes, ShowText|pysssss, CLIPTextEncode, LoraLoaderModelOnly, EmptySD3LatentImage, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, VHS_VideoCombine, CLIPLoader, CR String To Number, ShowText|pysssss, UNETLoader, RHHiddenNodes, CR Text, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 0, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wanduDMDJV1.0_1967613409602801666.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1967613409602801666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ReadExcelData`
- `ShowText|pysssss`
- `easy forLoopStart`
- `easy mathInt`
- `CR Integer To String`
- `Note`
- `PreviewImage`
- `easy showAnything`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `WanImageToVideo`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Text Multiline`
- `PlaySound|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `easy forLoopEnd`
- `easy showAnything`
- `easy forLoopStart`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `VHS_VideoCombine`
- `CLIPLoader`
- `CR String To Number`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `RHHiddenNodes`
- `CR Text`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `0`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（44/52）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`ReadExcelData`、`easy forLoopStart`、`easy mathInt`、`CR Integer To String`、`Text Concatenate`、`KSampler`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`CLIPLoader`、`Text Multiline`、`PlaySound|pysssss`、`LayerUtility: PurgeVRAM V2`、`easy forLoopEnd`、`RHHiddenNodes`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`CR String To Number`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
