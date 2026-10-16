---
key: 视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json
name: wan2.2 图生视频_2030667044726771713.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030667044726771713.json
hash: b1073bb9aedcc213
coverage: 1
learned_at: 2026-10-15 22:35:27
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ImageResizeKJv2, UnetLoaderGGUF, UnetLoaderGGUF, CLIPTextEncode, VHS_VideoCombine, CLIPLoader, VAELoader, ModelPatchTorchSettings, ModelPatchTorchSettings, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, WanImageToVideo, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030667044726771713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageResizeKJv2`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`PathchSageAttentionKJ`、`ImageResizeKJv2`、`UnetLoaderGGUF`、`CLIPTextEncode`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`WanImageToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、ImageResizeKJv2
