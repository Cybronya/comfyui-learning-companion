---
key: 图片生成/图生图/Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513.json
name: Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513.json
hash: 1c6ac793f0b46f5f
coverage: 0.883721
learned_at: 2026-10-23 10:52:07
nodes: [Qwen3_VQA_Plus, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, GetImageSizeAndCount, Int, StringFunction|pysssss, easy seed, KSampler, VAEDecode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, easy showAnything, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, VAELoader, ImageListToBatch+, GetImageSizeAndCount, CM_IntToFloat, CM_FloatUnaryOperation, CM_FloatToInt, easy showAnything, FL_ImageBatchToGrid, easy promptLine, easy saveText, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, easy showAnything, GetImageSizeAndCount, UNETLoader, CLIPLoader, SaveImage, SaveImage, JWIntegerToString, Int, ProcessString, CR Prompt Text, RH_LLMAPI_NODE, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 25519709795560, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `Qwen3_VQA_Plus`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `GetImageSizeAndCount`
- `Int`
- `StringFunction|pysssss`
- `easy seed`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `easy showAnything`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `VAELoader`
- `ImageListToBatch+`
- `GetImageSizeAndCount`
- `CM_IntToFloat`
- `CM_FloatUnaryOperation`
- `CM_FloatToInt`
- `easy showAnything`
- `FL_ImageBatchToGrid`
- `easy promptLine`
- `easy saveText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `easy showAnything`
- `GetImageSizeAndCount`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `SaveImage`
- `JWIntegerToString`
- `Int`
- `ProcessString`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `25519709795560`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`Qwen3_VQA_Plus`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`LoadImage`、`GetImageSizeAndCount`、`Int`、`StringFunction|pysssss`、`easy seed`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`VAELoader`、`ImageListToBatch+`、`CM_IntToFloat`、`CM_FloatUnaryOperation`、`CM_FloatToInt`、`FL_ImageBatchToGrid`、`easy promptLine`、`easy saveText`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`JWIntegerToString`、`ProcessString`、`CR Prompt Text`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
