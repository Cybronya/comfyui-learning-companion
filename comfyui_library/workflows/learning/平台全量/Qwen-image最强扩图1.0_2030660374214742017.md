---
key: 平台全量/Qwen-image最强扩图1.0_2030660374214742017.json
name: Qwen-image最强扩图1.0_2030660374214742017
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image最强扩图1.0_2030660374214742017.json
hash: 142b39e98e818d16
coverage: 0.740741
learned_at: 2026-11-14 00:52:14
nodes: [LoadImage, LoadImage, Anything Everywhere3, ModelSamplingAuraFlow, VAELoader, CLIPLoader, ControlNetInpaintingAliMamaApply, ConditioningZeroOut, UNETLoader, ImageScaleToTotalPixels, Note, VAEDecode, VAEEncode, KSampler, LayerUtility: PurgeVRAM, PreviewImage, Note, SaveImage, Image Comparer (rgthree), CLIPTextEncode, Note, RH_Captioner, ShowText|pysssss, RHHiddenNodes, RHHiddenNodes, LoadImage, ImagePadForOutpaint]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 803333849110131, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-image最强扩图1.0_2030660374214742017.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image最强扩图1.0_2030660374214742017.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LoadImage`
- `LoadImage`
- `Anything Everywhere3`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `ControlNetInpaintingAliMamaApply`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `Note`
- `RH_Captioner`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `LoadImage`
- `ImagePadForOutpaint`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `803333849110131`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LoadImage`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`ControlNetInpaintingAliMamaApply`、`ConditioningZeroOut`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`VAEEncode`、`KSampler`、`LayerUtility: PurgeVRAM`、`SaveImage`、`CLIPTextEncode`、`RH_Captioner`、`RHHiddenNodes`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
