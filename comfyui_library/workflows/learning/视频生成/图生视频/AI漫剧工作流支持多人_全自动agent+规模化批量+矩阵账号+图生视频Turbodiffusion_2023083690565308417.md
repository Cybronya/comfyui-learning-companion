---
key: 视频生成/图生视频/AI漫剧工作流支持多人_全自动agent+规模化批量+矩阵账号+图生视频Turbodiffusion_2023083690565308417.json
name: AI漫剧工作流支持多人_全自动agent+规模化批量+矩阵账号+图生视频Turbodiffusion_2023083690565308417.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2023083690565308417.json
hash: 17ffb5a6bafcca49
coverage: 0.953488
learned_at: 2026-10-15 22:35:11
nodes: [VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEDecode, LoadImage, easy promptLine, ProcessString, JjkText, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, CR Text Concatenate, CR Text, AILab_QwenVL_Advanced, CR Text Concatenate, CR Text Concatenate, RH_LLMAPI_Pro_Node, ImpactInt, ImpactInt, easy forLoopEnd, easy forLoopStart, easy anythingIndexSwitch, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, easy imageListToImageBatch, easy promptLine, JjkText, CR Text Concatenate, LoadAudio, ImageResizeKJv2, Note, LoraLoaderModelOnly, easy imageCount, Int, easy anythingIndexSwitch, easy forLoopEnd, RH_LLMAPI_Pro_Node, LoadImage, AILab_QwenVL_Advanced, CR Text, ImpactInt, easy anythingIndexSwitch, CR Text Concatenate, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CompressImages, Note, TurboWanModelLoader, TurboWanModelLoader, CLIPLoader, IfInnerExecute, ImageResizeKJv2, ImageResizeKJv2, TurboWanVAELoader, CLIPTextEncode, TurboDiffusionI2VSampler, VHS_VideoCombine, easy forLoopStart, TurboDiffusionI2VSampler, KSampler, easy compare, AppendImageBatch, AppendImageBatch, AppendImageBatch, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 288178094171776, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AI漫剧工作流支持多人_全自动agent+规模化批量+矩阵账号+图生视频Turbodiffusion_2023083690565308417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2023083690565308417.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（86 个）：
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `LoadImage`
- `easy promptLine`
- `ProcessString`
- `JjkText`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CR Text Concatenate`
- `CR Text`
- `AILab_QwenVL_Advanced`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `RH_LLMAPI_Pro_Node`
- `ImpactInt`
- `ImpactInt`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy anythingIndexSwitch`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `easy imageListToImageBatch`
- `easy promptLine`
- `JjkText`
- `CR Text Concatenate`
- `LoadAudio`
- `ImageResizeKJv2`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `easy imageCount`
- `Int`
- `easy anythingIndexSwitch`
- `easy forLoopEnd`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `AILab_QwenVL_Advanced`
- `CR Text`
- `ImpactInt`
- `easy anythingIndexSwitch`
- `CR Text Concatenate`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CompressImages`
- `Note`
- `TurboWanModelLoader`
- `TurboWanModelLoader`
- `CLIPLoader`
- `IfInnerExecute`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `TurboWanVAELoader`
- `CLIPTextEncode` ★核心
- `TurboDiffusionI2VSampler` ★核心
- `VHS_VideoCombine`
- `easy forLoopStart`
- `TurboDiffusionI2VSampler` ★核心
- `KSampler` ★核心
- `easy compare`
- `AppendImageBatch`
- `AppendImageBatch`
- `AppendImageBatch`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `288178094171776`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（82/86）

**有卡**：`VAEEncode`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`LoadImage`、`easy promptLine`、`ProcessString`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CR Text Concatenate`、`CR Text`、`AILab_QwenVL_Advanced`、`RH_LLMAPI_Pro_Node`、`ImpactInt`、`easy forLoopEnd`、`easy forLoopStart`、`easy anythingIndexSwitch`、`ImageFromBatch+`、`easy imageListToImageBatch`、`LoadAudio`、`ImageResizeKJv2`、`easy imageCount`、`Int`、`LayerUtility: PurgeVRAM V2`、`CompressImages`、`TurboWanModelLoader`、`IfInnerExecute`、`TurboWanVAELoader`、`CLIPTextEncode`、`TurboDiffusionI2VSampler`、`VHS_VideoCombine`、`KSampler`、`easy compare`、`AppendImageBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
