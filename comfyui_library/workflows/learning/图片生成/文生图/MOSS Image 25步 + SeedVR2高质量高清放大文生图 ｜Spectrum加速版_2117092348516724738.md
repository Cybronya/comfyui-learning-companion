---
key: 图片生成/文生图/MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738.json
name: MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738.json
hash: d2f7537e805e2fe1
coverage: 0.863636
learned_at: 2026-11-02 19:15:33
nodes: [KSampler, ResolutionSelector, Seed (rgthree), EmptyLatentImage, VAEDecode, CLIPTextEncode, CLIPTextEncode, VAELoader, UNETLoader, CLIPLoader, PrimitiveStringMultiline, easy cleanGpuUsed, SpectrumMOSSImageAdaptive, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Any Switch (rgthree), SaveImage, ImpactInt, 孤海注释, 忽略多组孤海]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 666, "steps": 25, "width": 1024}
---

# 图片生成/文生图/MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `KSampler` ★核心
- `ResolutionSelector`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `easy cleanGpuUsed`
- `SpectrumMOSSImageAdaptive`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Any Switch (rgthree)`
- `SaveImage`
- `ImpactInt`
- `孤海注释`
- `忽略多组孤海`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `666`
- `steps` = `25`
- `cfg` = `2.5`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`KSampler`、`ResolutionSelector`、`Seed (rgthree)`、`EmptyLatentImage`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`easy cleanGpuUsed`、`SpectrumMOSSImageAdaptive`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`ImpactInt`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、ResolutionSelector、UNETLoader
