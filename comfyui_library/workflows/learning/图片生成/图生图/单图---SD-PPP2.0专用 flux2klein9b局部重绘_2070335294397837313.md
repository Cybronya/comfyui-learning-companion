---
key: 图片生成/图生图/单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313.json
name: 单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313.json
hash: 9ec4a6631fc000e8
coverage: 0.9375
learned_at: 2026-10-21 00:50:41
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, Text Multiline, KSampler, SaveImage, ConditioningZeroOut, ReferenceLatent, Kontext Inpainting Conditioning, VAEEncode, VAEDecode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 822089962346403, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `KSampler` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Kontext Inpainting Conditioning`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Int`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `822089962346403`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`Text Multiline`、`KSampler`、`SaveImage`、`ConditioningZeroOut`、`ReferenceLatent`、`Kontext Inpainting Conditioning`、`VAEEncode`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
