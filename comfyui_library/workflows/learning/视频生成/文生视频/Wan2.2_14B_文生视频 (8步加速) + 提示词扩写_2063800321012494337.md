---
key: 视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json
name: Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json
hash: 39a8e8970774b334
coverage: 1
learned_at: 2026-10-15 22:47:13
nodes: [ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, easy int, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, SimpleMath+, easy int, easy int, VAEDecode, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, TextBox, WanVideoPromptExtender, QwenLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（26 个）：
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `easy int`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `easy int`
- `easy int`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `TextBox`
- `WanVideoPromptExtender`
- `QwenLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`easy int`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`SimpleMath+`、`VAEDecode`、`VHS_VideoCombine`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`TextBox`、`WanVideoPromptExtender`、`QwenLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
