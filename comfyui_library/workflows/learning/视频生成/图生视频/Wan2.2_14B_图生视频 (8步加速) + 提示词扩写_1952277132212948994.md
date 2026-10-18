---
key: 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json
name: Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json
hash: 258519d5ead7a8c0
coverage: 1
learned_at: 2026-10-15 22:31:00
nodes: [ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, SimpleMath+, easy int, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, WanImageToVideo, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, easy int, easy int, VHS_VideoCombine, VAEDecode, LoadImage, TextBox, CLIPTextEncode, CLIPTextEncode, QwenLoader, WanVideoPromptExtender]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952277132212948994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `SimpleMath+`
- `easy int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LoadImage`
- `TextBox`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `QwenLoader`
- `WanVideoPromptExtender`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`SimpleMath+`、`easy int`、`UNETLoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`、`ImageResizeKJv2`、`VHS_VideoCombine`、`VAEDecode`、`LoadImage`、`TextBox`、`CLIPTextEncode`、`QwenLoader`、`WanVideoPromptExtender`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
