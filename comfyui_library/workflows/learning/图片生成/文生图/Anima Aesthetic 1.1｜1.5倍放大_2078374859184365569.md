---
key: 图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json
name: Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json
hash: 092c31e574be449e
coverage: 1
learned_at: 2026-10-20 00:18:44
nodes: [CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, XB_UNetNameBroadcaster, LoraLoaderModelOnly, EnhancedLoadDiffusionModel, FluxResolutionNode, VAELoader, CLIPLoader, ModelSamplingAuraFlow, VAEDecode, LatentUpscaleBy, KSampler, LatentUpscaleBy, ClownsharKSampler_Beta, ClownsharKSampler_Beta, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 18, "denoise": 4.500000000000001, "height": 1024, "sampler_name": -1, "scheduler": 0.3500000000000001, "seed": 0.5, "steps": "beta57", "width": 1024}
---

# 图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `XB_UNetNameBroadcaster`
- `LoraLoaderModelOnly` ★核心
- `EnhancedLoadDiffusionModel`
- `FluxResolutionNode`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `LatentUpscaleBy`
- `KSampler` ★核心
- `LatentUpscaleBy`
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `18`
- `sampler_name` = `-1`
- `scheduler` = `0.3500000000000001`
- `denoise` = `4.500000000000001`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`XB_UNetNameBroadcaster`、`LoraLoaderModelOnly`、`EnhancedLoadDiffusionModel`、`FluxResolutionNode`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`LatentUpscaleBy`、`ClownsharKSampler_Beta`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ClownsharKSampler_Beta
