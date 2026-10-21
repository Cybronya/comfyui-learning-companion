---
key: 图片生成/文生图/Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026.json
name: Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026.json
hash: ad7da497c151b18f
coverage: 0.953488
learned_at: 2026-10-20 23:21:51
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, VAEDecode, UNETLoader, UNETLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, Fast Groups Bypasser (rgthree), EmptyLatentImage, LayerUtility: ImageReelComposit, SaveImage, SaveImage, KSamplerAdvanced, SaveImage, SaveImage, LayerUtility: ImageReel, Saturation, VAEDecode, VAEDecode, easy promptList, easy promptList, DF_Text_Box, SaveImage, ConditioningZeroOut, CLIPLoaderGGUF, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 2048, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageReel`
- `Saturation`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy promptList`
- `easy promptList`
- `DF_Text_Box`
- `SaveImage`
- `ConditioningZeroOut`
- `CLIPLoaderGGUF`
- `PrimitiveInt`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `FlowMatchEulerDiscreteScheduler`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（41/43）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`ConditioningZeroOut`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`LayerUtility: ImageReelComposit`、`SaveImage`、`LayerUtility: ImageReel`、`Saturation`、`easy promptList`、`DF_Text_Box`、`CLIPLoaderGGUF`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
