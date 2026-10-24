---
key: 图片生成/图生图/Qwen-edit-plus OOTD+Pose控制工作流_1972578594327293954.json
name: Qwen-edit-plus OOTD+Pose控制工作流_1972578594327293954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-edit-plus OOTD+Pose控制工作流_1972578594327293954.json
hash: 528a6caa13a69cab
coverage: 0.870968
learned_at: 2026-10-23 11:17:52
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, CLIPLoader, VAELoader, ShowText, LoadImage, PreviewImage, Label (rgthree), Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, AIO_Preprocessor, Label (rgthree), KSampler, VAEDecode, SeedVR2GGUF, PreviewImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, LoraLoaderModelOnly, Anything Everywhere3, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, ImageConcatMulti, ImageConcatMulti, RH_Captioner, Textbox, ConcatTextOfUtils]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 306227514501966, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-edit-plus OOTD+Pose控制工作流_1972578594327293954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-edit-plus OOTD+Pose控制工作流_1972578594327293954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ShowText`
- `LoadImage`
- `PreviewImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `AIO_Preprocessor`
- `Label (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SeedVR2GGUF`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `SaveImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `RH_Captioner`
- `Textbox`
- `ConcatTextOfUtils`

## 关键参数

- `seed` = `306227514501966`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ShowText`、`LoadImage`、`Label (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`KSampler`、`VAEDecode`、`SeedVR2GGUF`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`SaveImage`、`ImageConcatMulti`、`RH_Captioner`、`Textbox`、`ConcatTextOfUtils`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
