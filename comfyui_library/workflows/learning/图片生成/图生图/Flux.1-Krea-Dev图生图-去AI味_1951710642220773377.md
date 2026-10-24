---
key: 图片生成/图生图/Flux.1-Krea-Dev图生图-去AI味_1951710642220773377.json
name: Flux.1-Krea-Dev图生图-去AI味_1951710642220773377
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-去AI味_1951710642220773377.json
hash: 5d5ecf375664dd20
coverage: 0.966667
learned_at: 2026-10-23 10:58:42
nodes: [ImageUpscaleWithModel, ImageTile+, ImageScaleDownToSize, ImageScaleBy, ImageUntile+, VAELoader, MarkdownNote, LayerColor: HSV, LayerColor: BrightnessContrastV2, YC Color Match, ImageStitch, SaveImage, SaveImage, SaveImage, FluxGuidance, KSampler, VAEDecode, UltimateSDUpscale, FluxGuidance, VAEEncode, StringFunction|pysssss, CLIPTextEncode, UNETLoader, CFGZeroStar, DualCLIPLoader, UpscaleModelLoader, RH_Captioner, CLIPTextEncode, ImageSmartSharpen+, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 1085280752521082, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-Dev图生图-去AI味_1951710642220773377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-去AI味_1951710642220773377.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `ImageUpscaleWithModel`
- `ImageTile+`
- `ImageScaleDownToSize`
- `ImageScaleBy`
- `ImageUntile+`
- `VAELoader`
- `MarkdownNote`
- `LayerColor: HSV`
- `LayerColor: BrightnessContrastV2`
- `YC Color Match`
- `ImageStitch`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UltimateSDUpscale`
- `FluxGuidance`
- `VAEEncode` ★核心
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CFGZeroStar`
- `DualCLIPLoader`
- `UpscaleModelLoader`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `ImageSmartSharpen+`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1085280752521082`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`ImageUpscaleWithModel`、`ImageTile+`、`ImageScaleDownToSize`、`ImageScaleBy`、`ImageUntile+`、`VAELoader`、`LayerColor: HSV`、`LayerColor: BrightnessContrastV2`、`YC Color Match`、`ImageStitch`、`SaveImage`、`FluxGuidance`、`KSampler`、`VAEDecode`、`UltimateSDUpscale`、`VAEEncode`、`StringFunction|pysssss`、`CLIPTextEncode`、`UNETLoader`、`CFGZeroStar`、`DualCLIPLoader`、`UpscaleModelLoader`、`RH_Captioner`、`ImageSmartSharpen+`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CFGZeroStar
