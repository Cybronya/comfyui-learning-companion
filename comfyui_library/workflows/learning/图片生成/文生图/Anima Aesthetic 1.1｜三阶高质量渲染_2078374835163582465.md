---
key: 图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json
name: Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json
hash: 5b85e822410ce52a
coverage: 0.923077
learned_at: 2026-10-20 00:18:45
nodes: [EmptyLatentImage, XB_UNetNameBroadcaster, LoraLoaderModelOnly, EnhancedLoadDiffusionModel, FluxResolutionNode, VAELoader, CLIPLoader, ModelSamplingAuraFlow, LatentUpscaleBy, LatentUpscaleBy, CLIPTextEncode, CLIPTextEncode, LatentUpscaleBy, LatentUpscaleBy, SaveImage, VAEDecode, PreviewImage, SaveImage, KSampler, KSampler, KSampler, VAEDecode, ClownsharKSampler_Beta, ClownsharKSampler_Beta, ClownsharKSampler_Beta, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 18, "denoise": 1.8000000000000003, "height": 1024, "sampler_name": -1, "scheduler": 0.3500000000000001, "seed": 0.5, "steps": "beta57", "width": 1024}
---

# 图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `EmptyLatentImage` ★核心
- `XB_UNetNameBroadcaster`
- `LoraLoaderModelOnly` ★核心
- `EnhancedLoadDiffusionModel`
- `FluxResolutionNode`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `LatentUpscaleBy`
- `LatentUpscaleBy`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `LatentUpscaleBy`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `PreviewImage`

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
- `denoise` = `1.8000000000000003`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`EmptyLatentImage`、`XB_UNetNameBroadcaster`、`LoraLoaderModelOnly`、`EnhancedLoadDiffusionModel`、`FluxResolutionNode`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`LatentUpscaleBy`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`KSampler`、`ClownsharKSampler_Beta`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ClownsharKSampler_Beta
