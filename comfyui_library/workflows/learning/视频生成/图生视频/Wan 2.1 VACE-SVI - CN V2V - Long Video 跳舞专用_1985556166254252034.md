---
key: 视频生成/图生视频/Wan 2.1 VACE-SVI - CN V2V - Long Video 跳舞专用_1985556166254252034.json
name: Wan 2.1 VACE-SVI - CN V2V - Long Video 跳舞专用_1985556166254252034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985556166254252034.json
hash: de4f8b784cec24d5
coverage: 0.41958
learned_at: 2026-10-15 22:32:51
nodes: [CLIPTextEncode, WanVaceToVideo, INTConstant, INTConstant, TrimVideoLatent, VAEDecode, LayerUtility: PurgeVRAM, GetImageRangeFromBatch, SetNode, ImageResizeKJv2, LayerUtility: PurgeVRAM, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVaceToVideo, KSampler, TrimVideoLatent, SetNode, SetNode, WanVideoVACEStartToEndFrame, GetNode, MathExpression|pysssss, VHS_VideoCombine, MathExpression|pysssss, INTConstant, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, MathExpression|pysssss, GetNode, ImageResizeKJv2, GetNode, INTConstant, ModelSamplingSD3, ModelSamplingSD3, INTConstant, FloatConstant, GetNode, GetNode, GetNode, easy forLoopStart, easy forLoopEnd, VHS_GetImageCount, MathExpression|pysssss, ImageBatchMulti, VHS_GetImageCount, MathExpression|pysssss, easy showAnything, VHS_VideoCombine, KSampler, VHS_GetImageCount, easy showAnything, easy showAnything, GetNode, PreviewImage, PreviewImage, Reroute, GetNode, PathchSageAttentionKJ, Note, UnetLoaderGGUF, UNETLoader, Note, CLIPLoader, Note, GetNode, GetNode, LoadImage, VAELoader, Note, CLIPTextEncode, TorchCompileModelWanVideoV2, Power Lora Loader (rgthree), GetNode, Note, FloatConstant, VHS_VideoInfo, wanBlockSwap, Note, Note, INTConstant, Note, MaskToImage, Reroute, GetNode, Note, GetImageRangeFromBatch, GetNode, ImageColorMatch+, easy showAnything, VHS_GetImageCount, SetNode, GetNode, GetNode, PreviewImage, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ImageColorMatch+, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, DWPreprocessor, SetNode, GetImageRangeFromBatch, Note, Note, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 50, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan 2.1 VACE-SVI - CN V2V - Long Video 跳舞专用_1985556166254252034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985556166254252034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（143 个）：
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `INTConstant`
- `INTConstant`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `GetImageRangeFromBatch`
- `SetNode`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVaceToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `MathExpression|pysssss`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopStart`
- `easy forLoopEnd`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `ImageBatchMulti`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `easy showAnything`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VHS_GetImageCount`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `GetNode`
- `PathchSageAttentionKJ`
- `Note`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `Note`
- `CLIPLoader`
- `Note`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VAELoader`
- `Note`
- `CLIPTextEncode` ★核心
- `TorchCompileModelWanVideoV2`
- `Power Lora Loader (rgthree)`
- `GetNode`
- `Note`
- `FloatConstant`
- `VHS_VideoInfo`
- `wanBlockSwap`
- `Note`
- `Note`
- `INTConstant`
- `Note`
- `MaskToImage`
- `Reroute`
- `GetNode`
- `Note`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageColorMatch+`
- `easy showAnything`
- `VHS_GetImageCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageColorMatch+`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `SetNode`
- `GetImageRangeFromBatch`
- `Note`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Note`

## 关键参数

- `seed` = `50`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（60/143）

**有卡**：`CLIPTextEncode`、`WanVaceToVideo`、`INTConstant`、`TrimVideoLatent`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`KSampler`、`WanVideoVACEStartToEndFrame`、`MathExpression|pysssss`、`VHS_VideoCombine`、`ImageFromBatch`、`DWPreprocessor`、`ModelSamplingSD3`、`FloatConstant`、`easy forLoopStart`、`easy forLoopEnd`、`VHS_GetImageCount`、`ImageBatchMulti`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`VAELoader`、`TorchCompileModelWanVideoV2`、`Power Lora Loader (rgthree)`、`VHS_VideoInfo`、`wanBlockSwap`、`MaskToImage`、`ImageColorMatch+`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TrimVideoLatent

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
