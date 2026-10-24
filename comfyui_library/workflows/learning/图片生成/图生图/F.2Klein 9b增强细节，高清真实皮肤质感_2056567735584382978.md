---
key: 图片生成/图生图/F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978.json
name: F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978.json
hash: 9c1f4e877d6d23dd
coverage: 0.571429
learned_at: 2026-10-23 10:52:40
nodes: [Reroute, GetNode, SetNode, ReferenceLatent, VAELoader, SetNode, SetNode, SetNode, GetNode, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, GetNode, Reroute, GetNode, GetNode, VAEEncode, UpscaleModelLoader, ImageScaleBy, SetNode, GetNode, CLIPLoader, GetNode, GetNode, SaveImage, Image Comparer (rgthree), GetNode, ModelSamplingFlux, VAEEncode, KSampler, CLIPTextEncode, CLIPTextEncode, ImageUpscaleWithModel, VAEDecode, GetNode, SetNode, easy imageColorMatch, KSampler, GetNode, VAEDecode, LoadImage, easy imageConcat, SaveImage, UNETLoader, SetNode, LoraLoaderModelOnly, TextBox1, LayerUtility: ImageScaleByAspectRatio V2, Int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.4, "denoise": 0.25000000000000006, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 42, "steps": 2}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `Reroute`
- `GetNode`
- `SetNode`
- `ReferenceLatent`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `ImageScaleBy`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `ModelSamplingFlux`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `easy imageColorMatch`
- `KSampler` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `LoadImage`
- `easy imageConcat`
- `SaveImage`
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `TextBox1`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `42`
- `steps` = `2`
- `cfg` = `1.4`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **57%**（28/49）

**有卡**：`ReferenceLatent`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`UpscaleModelLoader`、`ImageScaleBy`、`CLIPLoader`、`SaveImage`、`ModelSamplingFlux`、`KSampler`、`ImageUpscaleWithModel`、`VAEDecode`、`easy imageColorMatch`、`LoadImage`、`easy imageConcat`、`UNETLoader`、`LoraLoaderModelOnly`、`TextBox1`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
