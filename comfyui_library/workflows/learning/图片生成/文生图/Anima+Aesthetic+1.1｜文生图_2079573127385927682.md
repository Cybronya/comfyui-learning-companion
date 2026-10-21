---
key: 图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json
name: Anima+Aesthetic+1.1｜文生图_2079573127385927682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json
hash: 905fd4a5b177c0f8
coverage: 0.882353
learned_at: 2026-10-20 00:38:40
nodes: [CLIPLoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, VAELoader, SaveImage, SaveImage, UNETLoader, KSampler, VAEDecode, XB_UNetNameBroadcaster, ClownsharKSampler_Beta, LoraLoaderModelOnly, FluxResolutionNode, PreviewImage, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 30, "denoise": 3.0100000000000007, "height": 1024, "sampler_name": -1, "scheduler": 1, "seed": 0.35, "steps": "beta57", "width": 1024}
---

# 图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `XB_UNetNameBroadcaster`
- `ClownsharKSampler_Beta` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxResolutionNode`
- `PreviewImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0.35`
- `steps` = `beta57`
- `cfg` = `30`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `3.0100000000000007`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`VAEDecode`、`VAELoader`、`SaveImage`、`UNETLoader`、`KSampler`、`XB_UNetNameBroadcaster`、`ClownsharKSampler_Beta`、`LoraLoaderModelOnly`、`FluxResolutionNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
