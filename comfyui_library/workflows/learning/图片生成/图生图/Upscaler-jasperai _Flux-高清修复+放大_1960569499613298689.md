---
key: 图片生成/图生图/Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689.json
name: Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689.json
hash: 11f482ddfa536d2b
coverage: 0.736842
learned_at: 2026-10-23 11:27:01
nodes: [VAELoader, UNETLoader, DualCLIPLoader, Anything Everywhere3, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, Anything Everywhere, KSampler, Anything Everywhere, ImageScaleBy, VAEEncode, Note, ControlNetLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ControlNetApplySD3]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.7000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1017638026194592, "steps": 20}
---

# 图片生成/图生图/Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Anything Everywhere`
- `KSampler` ★核心
- `Anything Everywhere`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `Note`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ControlNetApplySD3` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1017638026194592`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`KSampler`、`ImageScaleBy`、`VAEEncode`、`ControlNetLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader
