---
key: 图片生成/图生图/Krea2-RealCharacters-V2.5-动漫转真人_2086306808708296705.json
name: Krea2-RealCharacters-V2.5-动漫转真人_2086306808708296705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2-RealCharacters-V2.5-动漫转真人_2086306808708296705.json
hash: f77fb158d1e72467
coverage: 0.933333
learned_at: 2026-10-23 11:07:56
nodes: [Krea2OstrisEditModelPatch, LoadImage, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, VAEEncode, KSampler, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, PreviewImage, VAEDecode, SaveImage, UNETLoader, easy int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 103839017747253, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Krea2-RealCharacters-V2.5-动漫转真人_2086306808708296705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2-RealCharacters-V2.5-动漫转真人_2086306808708296705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `easy int`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `103839017747253`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`Krea2OstrisEditModelPatch`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`KSampler`、`FluxKontextMultiReferenceLatentMethod`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`UNETLoader`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
