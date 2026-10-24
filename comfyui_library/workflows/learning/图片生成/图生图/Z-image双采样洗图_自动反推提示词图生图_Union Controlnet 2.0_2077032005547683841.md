---
key: 图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841.json
name: Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841.json
hash: ff1dcaf178d8d92f
coverage: 0.818182
learned_at: 2026-10-23 11:31:19
nodes: [LayerUtility: PurgeVRAM, PreviewImage, KSampler, ModelSamplingAuraFlow, VAELoader, Text Concatenate, easy showAnything, EmptySD3LatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, easy int, CLIPLoader, CLIPTextEncode, UNETLoader, KSampler, AIO_Preprocessor, ConditioningZeroOut, AIO_Preprocessor, AIO_Preprocessor, easy anythingIndexSwitch, ModelPatchLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, MarkdownNote, QwenImageDiffsynthControlnet, VAEDecode, SaveImage, MarkdownNote, LoadImage, Qwen3_VQA, easy int, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 966075165812856, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image双采样洗图_自动反推提示词图生图_Union Controlnet 2.0_2077032005547683841.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `Text Concatenate`
- `easy showAnything`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `easy int`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `easy anythingIndexSwitch`
- `ModelPatchLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `MarkdownNote`
- `QwenImageDiffsynthControlnet`
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `Qwen3_VQA`
- `easy int`
- `Note`

## 关键参数

- `seed` = `966075165812856`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`LayerUtility: PurgeVRAM`、`KSampler`、`ModelSamplingAuraFlow`、`VAELoader`、`Text Concatenate`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`CR Prompt Text`、`easy int`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`AIO_Preprocessor`、`ConditioningZeroOut`、`easy anythingIndexSwitch`、`ModelPatchLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenImageDiffsynthControlnet`、`VAEDecode`、`SaveImage`、`LoadImage`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
