---
key: 视频生成/文生视频/wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930.json
name: wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930.json
hash: 518219824b4b3b27
coverage: 0.979592
learned_at: 2026-10-15 22:47:36
nodes: [SimpleMath+, easy getNode, easy getNode, easy getNode, DF_Integer, easy getNode, easy getNode, easy getNode, KSampler, ImageUpscaleWithModel, VAEEncode, ImageScaleBy, VAEDecode, VAEDecode, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, easy setNode, easy setNode, easy setNode, easy getNode, SaveImage, WanMoeKSampler, WanMoeKSampler, LoraLoaderModelOnly, CLIPLoader, EmptyHunyuanLatentVideo, easy setNode, VAELoader, easy setNode, EmptyHunyuanLatentVideo, easy getNode, easy getNode, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, UpscaleModelLoader, CLIPTextEncode, Text Multiline, MuyeTextEditOutput, VAEDecode, VHS_VideoCombine, easy getNode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, easy showAnything, RH_LLMAPI_NODE]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `SimpleMath+`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `DF_Integer`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `ImageScaleBy`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `SaveImage`
- `WanMoeKSampler` ★核心
- `WanMoeKSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `easy setNode`
- `VAELoader`
- `easy setNode`
- `EmptyHunyuanLatentVideo`
- `easy getNode`
- `easy getNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `MuyeTextEditOutput`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy getNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `RH_LLMAPI_NODE`

## 关键参数

- `seed` = `0.875`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **98%**（48/49）

**有卡**：`SimpleMath+`、`easy getNode`、`DF_Integer`、`KSampler`、`ImageUpscaleWithModel`、`VAEEncode`、`ImageScaleBy`、`VAEDecode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`easy setNode`、`SaveImage`、`WanMoeKSampler`、`LoraLoaderModelOnly`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`VAELoader`、`UpscaleModelLoader`、`Text Multiline`、`MuyeTextEditOutput`、`VHS_VideoCombine`、`UNETLoader`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
