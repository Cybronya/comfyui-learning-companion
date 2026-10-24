---
key: 图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json
name: F.2klein服装精修衣服去皱版型整理_2058031272836026370
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json
hash: d6f7175955dd5a22
coverage: 0.857143
learned_at: 2026-10-23 10:52:55
nodes: [ReferenceLatent, KSampler, VAEDecode, SaveImage, VAELoader, JjkText, CLIPTextEncode, CLIPLoader, FluxGuidance, UNETLoader, ConditioningZeroOut, JjkText, Float, Float, Image Comparer (rgthree), LoraLoaderModelOnly, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, VAEEncode, easy promptConcat]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 975261551031539, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ReferenceLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `FluxGuidance`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `JjkText`
- `Float`
- `Float`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `VAEEncode` ★核心
- `easy promptConcat`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `975261551031539`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ReferenceLatent`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`FluxGuidance`、`UNETLoader`、`ConditioningZeroOut`、`Float`、`LoraLoaderModelOnly`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`VAEEncode`、`easy promptConcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
