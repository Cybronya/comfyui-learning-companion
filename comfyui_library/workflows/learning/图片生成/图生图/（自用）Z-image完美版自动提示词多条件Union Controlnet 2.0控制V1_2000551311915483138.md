---
key: 图片生成/图生图/（自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138.json
name: （自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138.json
hash: 842c07403c5cf9e2
coverage: 0.891892
learned_at: 2026-10-23 13:38:26
nodes: [VAELoader, EmptySD3LatentImage, Note, CLIPTextEncode, GetImageSize, CLIPLoader, Canny, AIO_Preprocessor, QwenImageDiffsynthControlnet, AIO_Preprocessor, UNETLoader, LoadImage, ImageScaleToMaxDimension, ConditioningZeroOut, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, ModelPatchLoader, Qwen3_VQA, SaveImage, TT_img_enc, VAEDecode, CR Prompt Text, Note, Text Concatenate, easy showAnything, SaveImage, Text Concatenate, easy anythingIndexSwitch, easy anythingIndexSwitch, ModelSamplingAuraFlow, KSampler, KSampler, TT_img_enc_v2, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6500000000000001, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 968301150995682, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000551311915483138.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAELoader`
- `EmptySD3LatentImage`
- `Note`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `CLIPLoader`
- `Canny`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageScaleToMaxDimension`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `ModelPatchLoader`
- `Qwen3_VQA`
- `SaveImage`
- `TT_img_enc`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `Note`
- `Text Concatenate`
- `easy showAnything`
- `SaveImage`
- `Text Concatenate`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `KSampler` ★核心
- `TT_img_enc_v2`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `968301150995682`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.6500000000000001`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`VAELoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`GetImageSize`、`CLIPLoader`、`Canny`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`UNETLoader`、`LoadImage`、`ImageScaleToMaxDimension`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`Qwen3_VQA`、`SaveImage`、`TT_img_enc`、`VAEDecode`、`CR Prompt Text`、`Text Concatenate`、`easy anythingIndexSwitch`、`ModelSamplingAuraFlow`、`KSampler`、`TT_img_enc_v2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
