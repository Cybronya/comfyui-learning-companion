---
key: 图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json
name: Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json
hash: c1c185d6a6900055
coverage: 0.648148
learned_at: 2026-10-19 21:47:06
nodes: [CLIPLoader, SetNode, GetNode, SetNode, Text Concatenate, GetNode, GetNode, LoadImage, Qwen3_VQA, SaveImage, GetNode, VAELoader, SetNode, GetNode, SaveImage, LoadImage, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPTextEncode, ImageScaleToMaxDimension, AIO_Preprocessor, QwenImageDiffsynthControlnet, CR Prompt Text, SetNode, Primitive integer [Crystools], GetNode, easy showAnything, ShowText|pysssss, AIO_Preprocessor, JjkText, GetNode, VAEDecode, VAEDecode, KSampler, UNETLoader, GetImageSize, EmptySD3LatentImage, LayerUtility: PurgeVRAM V2, PreviewImage, KSampler, AIO_Preprocessor, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], ImpactSwitch, SetNode, ImpactSwitch, SetNode, ImageConcatMulti, ImageConcatMulti, SaveImage, Primitive integer [Crystools], RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.45000000000000007, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 780017534437132, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `Text Concatenate`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `GetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `SaveImage`
- `LoadImage`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `ImageScaleToMaxDimension`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `CR Prompt Text`
- `SetNode`
- `Primitive integer [Crystools]`
- `GetNode`
- `easy showAnything`
- `ShowText|pysssss`
- `AIO_Preprocessor`
- `JjkText`
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `GetImageSize`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `SetNode`
- `ImpactSwitch`
- `SetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `780017534437132`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.45000000000000007`

## 知识

覆盖率 **65%**（35/54）

**有卡**：`CLIPLoader`、`Text Concatenate`、`LoadImage`、`Qwen3_VQA`、`SaveImage`、`VAELoader`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`ImageScaleToMaxDimension`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`CR Prompt Text`、`Primitive integer [Crystools]`、`VAEDecode`、`KSampler`、`UNETLoader`、`GetImageSize`、`EmptySD3LatentImage`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
