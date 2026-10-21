---
key: 图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json
name: Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json
hash: 2fdc19dcf0de4eab
coverage: 0.909091
learned_at: 2026-10-20 00:01:17
nodes: [UNETLoader, VAELoader, CLIPTextEncode, CLIPLoader, VAEDecode, SaveImage, PreviewImage, EmptyLatentImage, CLIPTextEncode, FluxResolutionNode, ClownsharKSampler_Beta]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1.0000000000000002, "height": 1280, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "beta57", "width": 720}
---

# 图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `FluxResolutionNode`
- `ClownsharKSampler_Beta` ★核心

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`FluxResolutionNode`、`ClownsharKSampler_Beta`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ClownsharKSampler_Beta、FluxResolutionNode
