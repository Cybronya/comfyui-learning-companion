---
key: 图片生成/反推提示词/tsv1.0_2045799468322263042.json
name: tsv1.0_2045799468322263042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/tsv1.0_2045799468322263042.json
hash: 17088c666f870b7b
coverage: 1
learned_at: 2026-10-26 01:47:04
nodes: [LoadImage, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, CLIPVisionLoader, UnetLoaderGGUF, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPVisionEncode, VAELoader, CLIPTextEncode, WanImageToVideo, easy cleanGpuUsed, CLIPTextEncode, ModelSamplingSD3, UnetLoaderGGUF, SaveVideo, CreateVideo, VAEDecode, RTXVideoSuperResolution]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/反推提示词/tsv1.0_2045799468322263042.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/tsv1.0_2045799468322263042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPVisionEncode`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `UnetLoaderGGUF` ★核心
- `SaveVideo`
- `CreateVideo`
- `VAEDecode` ★核心
- `RTXVideoSuperResolution`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`LoadImage`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPVisionEncode`、`VAELoader`、`CLIPTextEncode`、`WanImageToVideo`、`easy cleanGpuUsed`、`SaveVideo`、`CreateVideo`、`VAEDecode`、`RTXVideoSuperResolution`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CLIPVisionEncode、CLIPVisionLoader
