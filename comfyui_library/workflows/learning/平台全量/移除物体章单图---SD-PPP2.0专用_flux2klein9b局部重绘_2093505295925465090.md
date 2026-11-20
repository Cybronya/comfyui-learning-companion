---
key: 平台全量/移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093505295925465090.json
name: 移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093505295925465090
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093505295925465090.json
hash: df8b87bd79e9cb99
coverage: 0.9375
learned_at: 2026-11-14 02:27:40
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, Text Multiline, KSampler, SaveImage, ConditioningZeroOut, ReferenceLatent, Kontext Inpainting Conditioning, VAEEncode, VAEDecode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1093103436495859, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093505295925465090.json

> 来源文件 `comfyui_library/workflows/平台全量/移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093505295925465090.json`

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

- `seed` = `1093103436495859`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`Text Multiline`、`KSampler`、`SaveImage`、`ConditioningZeroOut`、`ReferenceLatent`、`Kontext Inpainting Conditioning`、`VAEEncode`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
