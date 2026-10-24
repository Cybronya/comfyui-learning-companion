---
key: 图片生成/图生图/Wan2.1降维打击：强力姿势迁移，动作随心掌控！动作迁移_动作一致性_姿势一致性_1948755732972875777.json
name: Wan2.1降维打击：强力姿势迁移，动作随心掌控！动作迁移_动作一致性_姿势一致性_1948755732972875777
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1降维打击：强力姿势迁移，动作随心掌控！动作迁移_动作一致性_姿势一致性_1948755732972875777.json
hash: 6ff87a3ddf6589b5
coverage: 0.926829
learned_at: 2026-10-23 11:27:54
nodes: [LoadImage, LoadImage, PathchSageAttentionKJ, CLIPLoader, LayerUtility: LoadJoyCaptionBeta1Model, DeepTranslatorTextNode, LayerUtility: JoyCaption2ExtraOptions, easy showAnything, DWPreprocessor, RepeatImageBatch, LayerUtility: ImageScaleByAspectRatio V2, WanVaceToVideo, WanVideoNAG, KSampler, ModelSamplingSD3, TrimVideoLatent, VAEDecode, ColorMatch, PreviewImage, LayerUtility: JoyCaptionBeta1, UNETLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoNAG, VAEEncode, KSampler, PreviewImage, SaveImage, SaveImage, VAEDecode, ImageUpscaleWithModel, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, UpscaleModelLoader, GetImageRangeFromBatch]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1056293621599390, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1降维打击：强力姿势迁移，动作随心掌控！动作迁移_动作一致性_姿势一致性_1948755732972875777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1降维打击：强力姿势迁移，动作随心掌控！动作迁移_动作一致性_姿势一致性_1948755732972875777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `LoadImage`
- `LoadImage`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `DeepTranslatorTextNode`
- `LayerUtility: JoyCaption2ExtraOptions`
- `easy showAnything`
- `DWPreprocessor`
- `RepeatImageBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVaceToVideo`
- `WanVideoNAG`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ColorMatch`
- `PreviewImage`
- `LayerUtility: JoyCaptionBeta1`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoNAG`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `GetImageRangeFromBatch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1056293621599390`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`LoadImage`、`PathchSageAttentionKJ`、`CLIPLoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`DeepTranslatorTextNode`、`LayerUtility: JoyCaption2ExtraOptions`、`DWPreprocessor`、`RepeatImageBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVaceToVideo`、`WanVideoNAG`、`KSampler`、`ModelSamplingSD3`、`TrimVideoLatent`、`VAEDecode`、`ColorMatch`、`LayerUtility: JoyCaptionBeta1`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`GetImageRangeFromBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
