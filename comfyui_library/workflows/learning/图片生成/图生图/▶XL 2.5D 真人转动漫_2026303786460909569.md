---
key: 图片生成/图生图/▶XL 2.5D 真人转动漫_2026303786460909569.json
name: ▶XL 2.5D 真人转动漫_2026303786460909569
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/▶XL 2.5D 真人转动漫_2026303786460909569.json
hash: 5a00fb0912fb7b0a
coverage: 0.966667
learned_at: 2026-10-23 11:47:27
nodes: [CR Text Concatenate, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAEEncode, ImageUpscaleWithModel, KSampler, KSampler, WD14Tagger|pysssss, VAEEncode, LoadImage, SaveImage, LoadImage, Note, CheckpointLoaderSimple, VAEDecode, ImageScaleToTotalPixels, CLIPTextEncode, LoadImage, LoadImage, LoadImage, UpscaleModelLoader, VAEDecode, LoadImage, CR Prompt Text, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 6, "checkpoint": "IL-Gembyte_20Emerald(1).safetensors", "denoise": 0.4, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 815010734656864, "steps": 25}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/▶XL 2.5D 真人转动漫_2026303786460909569.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/▶XL 2.5D 真人转动漫_2026303786460909569.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CR Text Concatenate`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `KSampler` ★核心
- `KSampler` ★核心
- `WD14Tagger|pysssss`
- `VAEEncode` ★核心
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `815010734656864`
- `steps` = `25`
- `cfg` = `6`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.4`
- `checkpoint` = `IL-Gembyte_20Emerald(1).safetensors`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`CR Text Concatenate`、`LoadImage`、`VAEEncode`、`ImageUpscaleWithModel`、`KSampler`、`WD14Tagger|pysssss`、`SaveImage`、`CheckpointLoaderSimple`、`VAEDecode`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`UpscaleModelLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、ImageUpscaleWithModel、UpscaleModelLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
