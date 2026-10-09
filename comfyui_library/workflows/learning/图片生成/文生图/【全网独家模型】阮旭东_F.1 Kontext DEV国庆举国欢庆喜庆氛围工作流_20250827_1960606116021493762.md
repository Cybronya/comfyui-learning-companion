---
key: 图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json
name: 【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json
hash: a110ffdb573fda76
coverage: 0.8
learned_at: 2026-10-07 23:38:40
nodes: [Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SaveImage, UpscaleModelLoader, ImageUpscaleWithModel, Note, KSampler, FluxKontextImageScale, VAEDecode, FluxGuidance, ReferenceLatent, ConditioningZeroOut, VAEEncode, SaveImage, LoadImage, CLIPTextEncode, LoadImage, LoraLoader, DualCLIPLoader, VAELoader, UNETLoader, CR Prompt Text, LoadImage, LoadImage, MarkdownNote]
patterns: [image_to_image, lora]
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "阮旭东_国庆举国欢庆喜庆氛围F.1 Kontext DEV.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1066593482669611, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1960606116021493762.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Note`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `VAEDecode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `1066593482669611`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `阮旭东_国庆举国欢庆喜庆氛围F.1 Kontext DEV.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`SaveImage`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`KSampler`、`FluxKontextImageScale`、`VAEDecode`、`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`LoadImage`、`CLIPTextEncode`、`LoraLoader`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
