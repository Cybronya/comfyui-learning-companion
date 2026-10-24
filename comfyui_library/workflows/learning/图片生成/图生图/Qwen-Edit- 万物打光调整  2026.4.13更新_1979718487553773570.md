---
key: 图片生成/图生图/Qwen-Edit- 万物打光调整  2026.4.13更新_1979718487553773570.json
name: Qwen-Edit- 万物打光调整  2026.4.13更新_1979718487553773570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit- 万物打光调整  2026.4.13更新_1979718487553773570.json
hash: 4d79805787384382
coverage: 0.735294
learned_at: 2026-10-23 11:15:22
nodes: [SaveImage, ModelSamplingAuraFlow, LoadImage, FluxKontextImageScale, VAELoader, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), Seed (rgthree), VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, CFGNorm, ConditioningZeroOut, CLIPLoader, LoraLoader, SeedVR2LoadVAEModel, PreviewImage, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, VAEDecode, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, ImpactInt, TextEncodeQwenImageEdit, JjkText, CR Text Concatenate, Note, FSampler, QwenMultiangleLightningNode, LoraLoader, UNETLoader, Note, Note, Fast Groups Bypasser (rgthree)]
patterns: [lora]
missing: []
parameters: {"lora_name": "Qwen-Image-Edit-Lightning-8steps-V1.0-bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/Qwen-Edit- 万物打光调整  2026.4.13更新_1979718487553773570.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit- 万物打光调整  2026.4.13更新_1979718487553773570.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `SaveImage`
- `ModelSamplingAuraFlow`
- `LoadImage`
- `FluxKontextImageScale`
- `VAELoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CFGNorm`
- `ConditioningZeroOut`
- `CLIPLoader`
- `LoraLoader` ★核心
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `ImpactInt`
- `TextEncodeQwenImageEdit`
- `JjkText`
- `CR Text Concatenate`
- `Note`
- `FSampler` ★核心
- `QwenMultiangleLightningNode`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Qwen-Image-Edit-Lightning-8steps-V1.0-bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`SaveImage`、`ModelSamplingAuraFlow`、`LoadImage`、`FluxKontextImageScale`、`VAELoader`、`Seed (rgthree)`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CFGNorm`、`ConditioningZeroOut`、`CLIPLoader`、`LoraLoader`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImpactInt`、`TextEncodeQwenImageEdit`、`CR Text Concatenate`、`FSampler`、`QwenMultiangleLightningNode`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGNorm、SeedVR2LoadDiTModel
