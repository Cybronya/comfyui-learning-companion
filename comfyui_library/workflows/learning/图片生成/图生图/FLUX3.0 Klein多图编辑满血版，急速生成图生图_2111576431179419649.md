---
key: 图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json
name: FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json
hash: aed64fb3d1f67744
coverage: 0.866667
learned_at: 2026-10-23 10:54:41
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, Int, Int, PrimitiveBoolean, ComfySwitchNode, ReferenceMultiLatent, BasicGuider, ReferenceMultiLatent, ResolutionSelector, VAEDecode, AnySwitch, SamplerCustomAdvanced, KSampler, CLIPTextEncode, JjkText, UNETLoader, LoadImage, ManualSigmas, KSamplerSelect, EmptyFlux2LatentImage, RandomNoise, LoadImage, CreateBoundingBoxes, PreviewAny, CLIPTextEncode, Fast Bypasser (rgthree), SaveImage, PreviewImage, ImageConcatMulti, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ReferenceMultiLatent`
- `BasicGuider`
- `ReferenceMultiLatent`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `AnySwitch`
- `SamplerCustomAdvanced` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `UNETLoader` ★核心
- `LoadImage`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `LoadImage`
- `CreateBoundingBoxes`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `Fast Bypasser (rgthree)`
- `SaveImage`
- `PreviewImage`
- `ImageConcatMulti`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（52/60）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`Int`、`PrimitiveBoolean`、`ReferenceMultiLatent`、`BasicGuider`、`ResolutionSelector`、`VAEDecode`、`AnySwitch`、`SamplerCustomAdvanced`、`KSampler`、`UNETLoader`、`LoadImage`、`ManualSigmas`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`CreateBoundingBoxes`、`Fast Bypasser (rgthree)`、`SaveImage`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
