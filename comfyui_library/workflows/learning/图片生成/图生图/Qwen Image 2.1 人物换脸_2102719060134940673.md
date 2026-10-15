---
key: 图片生成/图生图/Qwen Image 2.1 人物换脸_2102719060134940673.json
name: Qwen Image 2.1 人物换脸_2102719060134940673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 人物换脸_2102719060134940673.json
hash: b4c2d8bf3141268d
coverage: 0.866667
learned_at: 2026-10-15 22:25:11
nodes: [VAELoader, QwenImage21Cache, CLIPLoader, SaveImage, TextEncodeQwenImage21, LoadImage, Reroute, GrowMaskWithBlur, LayerUtility: CropByMask V2, GrowMaskWithBlur, LayerUtility: RestoreCropBox, ComfySwitchNode, QwenPERewriteT8, easy cleanGpuUsed, ColorMatch, LayerUtility: ImageScaleRestore V2, EmptyLatentImage, VAEDecode, LoadImage, KSampler, CR Prompt Text, Image Comparer (rgthree), SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, UNETLoader, QwenImage21SpectrumT8, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 人物换脸_2102719060134940673.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 人物换脸_2102719060134940673.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAELoader`
- `QwenImage21Cache`
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `Reroute`
- `GrowMaskWithBlur`
- `LayerUtility: CropByMask V2`
- `GrowMaskWithBlur`
- `LayerUtility: RestoreCropBox`
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `easy cleanGpuUsed`
- `ColorMatch`
- `LayerUtility: ImageScaleRestore V2`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `easy showAnything`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`LoadImage`、`GrowMaskWithBlur`、`LayerUtility: CropByMask V2`、`LayerUtility: RestoreCropBox`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`ColorMatch`、`LayerUtility: ImageScaleRestore V2`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`UNETLoader`、`QwenImage21SpectrumT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
