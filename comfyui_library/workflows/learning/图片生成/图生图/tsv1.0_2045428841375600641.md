---
key: 图片生成/图生图/tsv1.0_2045428841375600641.json
name: tsv1.0_2045428841375600641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/tsv1.0_2045428841375600641.json
hash: 1af9c2f59ab23648
coverage: 1
learned_at: 2026-10-23 11:45:43
nodes: [LoadImage, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, CLIPVisionLoader, UnetLoaderGGUF, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPVisionEncode, VAELoader, CLIPTextEncode, WanImageToVideo, easy cleanGpuUsed, CLIPTextEncode, ModelSamplingSD3, UnetLoaderGGUF, CreateVideo, VAEDecode, RTXVideoSuperResolution, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/tsv1.0_2045428841375600641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/tsv1.0_2045428841375600641.json`

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
- `CreateVideo`
- `VAEDecode` ★核心
- `RTXVideoSuperResolution`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`LoadImage`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPVisionEncode`、`VAELoader`、`CLIPTextEncode`、`WanImageToVideo`、`easy cleanGpuUsed`、`CreateVideo`、`VAEDecode`、`RTXVideoSuperResolution`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CLIPVisionEncode、CLIPVisionLoader
