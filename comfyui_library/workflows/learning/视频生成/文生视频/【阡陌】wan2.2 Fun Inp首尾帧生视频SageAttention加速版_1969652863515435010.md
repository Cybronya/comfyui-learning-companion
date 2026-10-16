---
key: 视频生成/文生视频/【阡陌】wan2.2 Fun Inp首尾帧生视频SageAttention加速版_1969652863515435010.json
name: 【阡陌】wan2.2 Fun Inp首尾帧生视频SageAttention加速版_1969652863515435010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1969652863515435010.json
hash: bd693651f740e110
coverage: 1
learned_at: 2026-10-15 22:43:47
nodes: [VAEDecode, ModelSamplingSD3, ModelSamplingSD3, CreateVideo, SaveVideo, CLIPLoader, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, KSamplerAdvanced, CLIPTextEncode, WanFunInpaintToVideo, KSamplerAdvanced, VAELoader, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/【阡陌】wan2.2 Fun Inp首尾帧生视频SageAttention加速版_1969652863515435010.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969652863515435010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `WanFunInpaintToVideo`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`LoadImage`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`CLIPTextEncode`、`WanFunInpaintToVideo`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
