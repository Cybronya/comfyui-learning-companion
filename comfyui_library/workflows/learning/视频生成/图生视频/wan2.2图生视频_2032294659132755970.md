---
key: 视频生成/图生视频/wan2.2图生视频_2032294659132755970.json
name: wan2.2图生视频_2032294659132755970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032294659132755970.json
hash: adba8b3472ab008b
coverage: 0.904762
learned_at: 2026-10-15 22:35:35
nodes: [ModelSamplingSD3, CLIPLoader, ModelSamplingSD3, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, KSamplerAdvanced, CLIPTextEncode, KSamplerAdvanced, WanImageToVideo, VAEDecode, VHS_VideoCombine, LoadImage, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionLoader, CLIPTextEncode, Note, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频_2032294659132755970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032294659132755970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `PreviewImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`WanImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`CLIPVisionEncode`、`CLIPVisionLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
