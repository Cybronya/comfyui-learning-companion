---
key: 视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json
name: Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json
hash: 86e2ca59411cf5c8
coverage: 0.769231
learned_at: 2026-10-11 20:21:31
nodes: [ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, easy int, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, SimpleMath+, VAEDecode, VHS_VideoCombine, CLIPTextEncode, EmptyHunyuanLatentVideo, WanVideoPromptExtender, QwenLoader, TextBox, CLIPTextEncode, easy int, easy int]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleMath+, easy int, easy int, easy int]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json`

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
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `WanVideoPromptExtender`
- `QwenLoader`
- `TextBox`
- `CLIPTextEncode` ★核心
- `easy int`
- `easy int`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`VHS_VideoCombine`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`WanVideoPromptExtender`、`QwenLoader`、`TextBox`

**缺卡**（6）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`easy int`、`easy int`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
