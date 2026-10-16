---
key: 视频生成/图生视频/视频版抖音三宫格写真-分镜视频制作-Qwen Edit2509 Next Scene+wan2.2_1983726049295015938.json
name: 视频版抖音三宫格写真-分镜视频制作-Qwen Edit2509 Next Scene+wan2.2_1983726049295015938.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983726049295015938.json
hash: 7c0dd7d9edfd1b87
coverage: 0.645714
learned_at: 2026-10-15 22:32:45
nodes: [SetNode, easy cleanGpuUsed, easy cleanGpuUsed, VAEEncode, SetNode, UNETLoader, GetNode, SetNode, VAEDecode, ModelSamplingAuraFlow, GetNode, SaveImage, Int, easy promptConcat, ImageListToImageBatch, Reroute, Reroute, CR Overlay Text, CR Overlay Text, CFGNorm, GetNode, easy promptLine, SetNode, CR Overlay Text, CR Overlay Text, PreviewImage, PreviewImage, DeepTranslatorTextNode, DeepTranslatorTextNode, GetNode, ImageConcatMulti, SetNode, SetNode, SetNode, SetNode, JjkText, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, GetNode, easy promptConcat, easy promptConcat, SetNode, ProcessString, RH_LLMAPI_NODE, SaveImage, SaveImage, GetNode, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, UNETLoader, SetNode, wanBlockSwap, PathchSageAttentionKJ, SetNode, CLIPLoader, SetNode, SetNode, VAELoader, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, CLIPTextEncode, GetNode, GetNode, CLIPVisionEncode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, LayerUtility: PurgeVRAM V2, PreviewImage, JWInteger, CLIPTextEncode, ImageFromBatch, SetNode, SetNode, SetNode, ImageFromBatch, ImageFromBatch, easy imageBatchToImageList, VHS_VideoCombine, easy imageBatchToImageList, VHS_VideoCombine, easy imageBatchToImageList, VHS_VideoCombine, VAEDecode, DeepTranslatorTextNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, DeepTranslatorTextNode, GetNode, GetNode, DeepTranslatorTextNode, GetNode, DeepTranslatorTextNode, Reroute, Note, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, ImageConcatMulti, easy cleanGpuUsed, ModelPatchTorchSettings, easy cleanGpuUsed, ModelPatchTorchSettings, easy cleanGpuUsed, ImageConcatMulti, easy cleanGpuUsed, Text, CR Prompt Text, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy imageListToImageBatch, Float, easy imageListToImageBatch, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ConditioningZeroOut, TextEncodeQwenImageEditPlusAdvance_lrzjason, PreviewImage, CLIPLoader, GetNode, LoraLoaderModelOnly, KSampler, SetNode, VAELoader, CR Overlay Text, CR Overlay Text, CR Overlay Text, CR Overlay Text, CR Overlay Text, CR Overlay Text, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, JjkText, JjkText, JjkText, JjkText, Text, Text, GetNode, GetNode, GetNode, CR Overlay Text, CR Overlay Text, PreviewImage, SDVM Image List Repeat, easy imageListToImageBatch, easy imageListToImageBatch, JWInteger, ImageFromBatch, ImageFromBatch, ImageFromBatch, VHS_VideoCombine]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 488644512980328, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/视频版抖音三宫格写真-分镜视频制作-Qwen Edit2509 Next Scene+wan2.2_1983726049295015938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983726049295015938.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（175 个）：
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `GetNode`
- `SaveImage`
- `Int`
- `easy promptConcat`
- `ImageListToImageBatch`
- `Reroute`
- `Reroute`
- `CR Overlay Text`
- `CR Overlay Text`
- `CFGNorm`
- `GetNode`
- `easy promptLine`
- `SetNode`
- `CR Overlay Text`
- `CR Overlay Text`
- `PreviewImage`
- `PreviewImage`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `JjkText`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `GetNode`
- `easy promptConcat`
- `easy promptConcat`
- `SetNode`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `ImageFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `ImageFromBatch`
- `easy imageBatchToImageList`
- `VHS_VideoCombine`
- `easy imageBatchToImageList`
- `VHS_VideoCombine`
- `easy imageBatchToImageList`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `DeepTranslatorTextNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DeepTranslatorTextNode`
- `GetNode`
- `GetNode`
- `DeepTranslatorTextNode`
- `GetNode`
- `DeepTranslatorTextNode`
- `Reroute`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `easy cleanGpuUsed`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `easy cleanGpuUsed`
- `Text`
- `CR Prompt Text`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy imageListToImageBatch`
- `Float`
- `easy imageListToImageBatch`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `PreviewImage`
- `CLIPLoader`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SetNode`
- `VAELoader`
- `CR Overlay Text`
- `CR Overlay Text`
- `CR Overlay Text`
- `CR Overlay Text`
- `CR Overlay Text`
- `CR Overlay Text`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `Text`
- `Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Overlay Text`
- `CR Overlay Text`
- `PreviewImage`
- `SDVM Image List Repeat`
- `easy imageListToImageBatch`
- `easy imageListToImageBatch`
- `JWInteger`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `VHS_VideoCombine`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `488644512980328`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（113/175）

**有卡**：`easy cleanGpuUsed`、`VAEEncode`、`UNETLoader`、`VAEDecode`、`ModelSamplingAuraFlow`、`SaveImage`、`Int`、`easy promptConcat`、`ImageListToImageBatch`、`CR Overlay Text`、`CFGNorm`、`easy promptLine`、`DeepTranslatorTextNode`、`ImageConcatMulti`、`ProcessString`、`RH_LLMAPI_NODE`、`ModelSamplingSD3`、`wanBlockSwap`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`WanImageToVideo`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`ImageFromBatch`、`easy imageBatchToImageList`、`VHS_VideoCombine`、`ModelPatchTorchSettings`、`Text`、`CR Prompt Text`、`easy imageListToImageBatch`、`Float`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoraLoaderModelOnly`、`KSampler`、`SDVM Image List Repeat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
