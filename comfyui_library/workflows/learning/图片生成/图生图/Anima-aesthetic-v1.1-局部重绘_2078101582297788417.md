---
key: 图片生成/图生图/Anima-aesthetic-v1.1-局部重绘_2078101582297788417.json
name: Anima-aesthetic-v1.1-局部重绘_2078101582297788417
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima-aesthetic-v1.1-局部重绘_2078101582297788417.json
hash: 59b8db70dac81c7f
coverage: 0.882353
learned_at: 2026-10-10 20:48:02
nodes: [UNETLoader, MaskFillHoles, LayerUtility: ImageScaleByAspectRatio V2, KSampler, VAEDecode, PreviewImage, SaveImage, LoadImage, CLIPLoader, VAELoader, VAEEncode, SetLatentNoiseMask, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ModelPatchLoader, AnimaLLLiteApply]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 864435812893963, "steps": 8}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Anima-aesthetic-v1.1-局部重绘_2078101582297788417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima-aesthetic-v1.1-局部重绘_2078101582297788417.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `MaskFillHoles`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `AnimaLLLiteApply`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `864435812893963`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`MaskFillHoles`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`SetLatentNoiseMask`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`AnimaLLLiteApply`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
