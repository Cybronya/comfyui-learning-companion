---
key: 图片生成/图生图/Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777.json
name: Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777.json
hash: 58c22486a1c490f7
coverage: 0.837209
learned_at: 2026-10-23 11:30:45
nodes: [UNETLoader, CLIPTextEncode, VAELoader, SplitSigmas, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, CFGGuider, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, WanVideoNAG, VAEEncode, RandomNoise, Image Comparer (rgthree), SaveImage, SamplerCustomAdvanced, VAEDecode, DisableNoise, UNETLoader, ConditioningZeroOut, CLIPLoader, LoraLoaderModelOnly, VAELoader, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, PreviewImage, Image Comparer (rgthree), easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, KSampler, PreviewImage, InpaintCrop, VAEDecode, Reroute, InpaintStitch, LoadImage, Image Comparer (rgthree), SeedVR2, BasicScheduler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 76975375257106, "steps": 10}
---

# 图片生成/图生图/Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `VAEEncode` ★核心
- `RandomNoise`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `DisableNoise`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `PreviewImage`
- `InpaintCrop`
- `VAEDecode` ★核心
- `Reroute`
- `InpaintStitch`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SeedVR2`
- `BasicScheduler`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `76975375257106`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`SplitSigmas`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`KSamplerSelect`、`CFGGuider`、`CLIPLoader`、`LoraLoaderModelOnly`、`WanVideoNAG`、`VAEEncode`、`RandomNoise`、`SaveImage`、`VAEDecode`、`DisableNoise`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`easy cleanGpuUsed`、`KSampler`、`InpaintCrop`、`InpaintStitch`、`LoadImage`、`SeedVR2`、`BasicScheduler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
