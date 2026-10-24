---
key: 图片生成/图生图/无AI味逼真质感图生图-Flux.1-Krea-Dev_1951098618625372162.json
name: 无AI味逼真质感图生图-Flux.1-Krea-Dev_1951098618625372162
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/无AI味逼真质感图生图-Flux.1-Krea-Dev_1951098618625372162.json
hash: fd0784dcfa7eaeff
coverage: 0.85
learned_at: 2026-10-23 13:04:10
nodes: [UNETLoader, DualCLIPLoader, CLIPTextEncodeFlux, KSampler, VAELoader, VAEDecode, PrimitiveStringMultiline, RH_Captioner, TextInputBasic, ConditioningZeroOut, VAEEncode, RepeatLatentBatch, RH_Translator, ImageScaleDownToSize, PreviewImage, SaveImage, LoadImage, ShowText|pysssss, easy cleanGpuUsed, ImageStitch]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 751728972999313, "steps": 20}
---

# 图片生成/图生图/无AI味逼真质感图生图-Flux.1-Krea-Dev_1951098618625372162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/无AI味逼真质感图生图-Flux.1-Krea-Dev_1951098618625372162.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncodeFlux` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `RH_Captioner`
- `TextInputBasic`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `RH_Translator`
- `ImageScaleDownToSize`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `ImageStitch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `751728972999313`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`KSampler`、`VAELoader`、`VAEDecode`、`RH_Captioner`、`TextInputBasic`、`ConditioningZeroOut`、`VAEEncode`、`RepeatLatentBatch`、`RH_Translator`、`ImageScaleDownToSize`、`SaveImage`、`LoadImage`、`easy cleanGpuUsed`、`ImageStitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux、RepeatLatentBatch
