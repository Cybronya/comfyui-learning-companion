---
key: 图片生成/图生图/Krea2 JSON Multi-Panel Storyboard_2073788024386838530.json
name: Krea2 JSON Multi-Panel Storyboard_2073788024386838530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2 JSON Multi-Panel Storyboard_2073788024386838530.json
hash: d9103f53df5a2e36
coverage: 0.916667
learned_at: 2026-10-23 11:07:40
nodes: [UNETLoader, CLIPTextEncode, CLIPLoader, VAEDecode, SaveImage, EmptyLatentImage, VAELoader, ClownsharKSampler_Beta, ComfyUI-Krea2T-Enhancer, FluxResolutionNode, UNETLoader, CLIPTextEncode, CLIPLoader, VAEDecode, SaveImage, EmptyLatentImage, VAELoader, ComfyUI-Krea2T-Enhancer, FluxResolutionNode, ClownsharKSampler_Beta, UNETLoader, CLIPTextEncode, CLIPLoader, VAEDecode, SaveImage, EmptyLatentImage, VAELoader, ComfyUI-Krea2T-Enhancer, FluxResolutionNode, ClownsharKSampler_Beta, CLIPTextEncode, CLIPTextEncode, PreviewImage, PreviewImage, CLIPTextEncode, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1.0000000000000002, "height": 1280, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "beta57", "width": 720}
---

# 图片生成/图生图/Krea2 JSON Multi-Panel Storyboard_2073788024386838530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2 JSON Multi-Panel Storyboard_2073788024386838530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ClownsharKSampler_Beta` ★核心
- `ComfyUI-Krea2T-Enhancer`
- `FluxResolutionNode`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ComfyUI-Krea2T-Enhancer`
- `FluxResolutionNode`
- `ClownsharKSampler_Beta` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ComfyUI-Krea2T-Enhancer`
- `FluxResolutionNode`
- `ClownsharKSampler_Beta` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`

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

覆盖率 **92%**（33/36）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`VAELoader`、`ClownsharKSampler_Beta`、`ComfyUI-Krea2T-Enhancer`、`FluxResolutionNode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ClownsharKSampler_Beta、FluxResolutionNode
