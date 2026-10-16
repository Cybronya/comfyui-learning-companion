---
key: 视频生成/图生视频/图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json
name: 图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1987801301234987009.json
hash: 135a571e81fc2bee
coverage: 0.814815
learned_at: 2026-10-15 22:33:00
nodes: [MarkdownNote, Note, KSamplerAdvanced, KSamplerAdvanced, ModelPatchTorchSettings, PathchSageAttentionKJ, MarkdownNote, Note, CLIPTextEncode, UNETLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideo, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoader, UNETLoader, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, LoadImage, easy int, CLIPTextEncode, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987801301234987009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `MarkdownNote`
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `Note`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoadImage`
- `easy int`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`KSamplerAdvanced`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`LoadImage`、`easy int`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
