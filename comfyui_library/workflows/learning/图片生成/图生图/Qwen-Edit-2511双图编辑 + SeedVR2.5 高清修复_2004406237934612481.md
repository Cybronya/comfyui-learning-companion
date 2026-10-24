---
key: 图片生成/图生图/Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481.json
name: Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481.json
hash: 042294587c5c18f7
coverage: 0.923077
learned_at: 2026-10-23 11:15:53
nodes: [FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, CLIPLoader, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, KSampler, SaveImage, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, FluxKontextImageScale, TextEncodeQwenImageEditPlusAdvance_lrzjason, LoadImage, VAELoader, Anything Everywhere, QwenImageLatentAspectRatio, VAEDecode, LoadImage, FluxKontextImageScale, ImageConcatMulti, LayerUtility: PurgeVRAM V2, ImageConcatMulti, PreviewImage, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 140769486862402, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2511双图编辑 + SeedVR2.5 高清修复_2004406237934612481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `KSampler` ★核心
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LoadImage`
- `VAELoader`
- `Anything Everywhere`
- `QwenImageLatentAspectRatio`
- `VAEDecode` ★核心
- `LoadImage`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `PreviewImage`
- `CR Text`

## 关键参数

- `seed` = `140769486862402`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`KSampler`、`SaveImage`、`LayerUtility: PurgeVRAM V2`、`SeedVR2VideoUpscaler`、`FluxKontextImageScale`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoadImage`、`VAELoader`、`QwenImageLatentAspectRatio`、`VAEDecode`、`ImageConcatMulti`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
