---
key: 图片生成/图生图/flux_kontext_dev（附Presets插件，解放双手，无需手写触发词）_1956999676890157057.json
name: flux_kontext_dev（附Presets插件，解放双手，无需手写触发词）_1956999676890157057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux_kontext_dev（附Presets插件，解放双手，无需手写触发词）_1956999676890157057.json
hash: ab42b061b1cf2b62
coverage: 0.947368
learned_at: 2026-10-23 11:36:56
nodes: [ConditioningZeroOut, PreviewImage, SaveImage, FluxGuidance, ReferenceLatent, VAEEncode, KSampler, VAEDecode, FluxKontextImageScale, ImageStitch, CLIPTextEncode, EmptySD3LatentImage, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, UNETLoader, LoadKontextPresets, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 652362659153130, "steps": 20}
---

# 图片生成/图生图/flux_kontext_dev（附Presets插件，解放双手，无需手写触发词）_1956999676890157057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux_kontext_dev（附Presets插件，解放双手，无需手写触发词）_1956999676890157057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ConditioningZeroOut`
- `PreviewImage`
- `SaveImage`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadKontextPresets`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `652362659153130`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`ConditioningZeroOut`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`KSampler`、`VAEDecode`、`FluxKontextImageScale`、`ImageStitch`、`CLIPTextEncode`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`LoadKontextPresets`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
