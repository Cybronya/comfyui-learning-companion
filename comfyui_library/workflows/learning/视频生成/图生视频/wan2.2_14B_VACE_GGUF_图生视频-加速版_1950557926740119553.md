---
key: 视频生成/图生视频/wan2.2_14B_VACE_GGUF_图生视频-加速版_1950557926740119553.json
name: wan2.2_14B_VACE_GGUF_图生视频-加速版_1950557926740119553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950557926740119553.json
hash: 12f04cdf7f23f997
coverage: 1
learned_at: 2026-10-15 22:30:55
nodes: [CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, UnetLoaderGGUF, Text, LoadImage, UnetLoaderGGUF, LoraLoaderModelOnly, VAELoader, CLIPLoader, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, KSamplerAdvanced, WanVaceToVideo, TrimVideoLatent, VAEDecode, CreateVideo, SaveVideo, ImpactInt, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2_14B_VACE_GGUF_图生视频-加速版_1950557926740119553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950557926740119553.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `Text`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanVaceToVideo`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ImpactInt`
- `ImpactInt`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`Text`、`LoadImage`、`VAELoader`、`CLIPLoader`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`WanVaceToVideo`、`TrimVideoLatent`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`ImpactInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent
