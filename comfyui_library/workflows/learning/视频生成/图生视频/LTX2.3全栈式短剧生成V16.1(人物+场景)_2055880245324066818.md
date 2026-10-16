---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V16.1(人物+场景)_2055880245324066818.json
name: LTX2.3全栈式短剧生成V16.1(人物+场景)_2055880245324066818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055880245324066818.json
hash: 6dfd61d26249066e
coverage: 0.778761
learned_at: 2026-10-15 22:37:59
nodes: [SetNode, SetNode, SetNode, ManualSigmas, CFGGuider, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, SamplerCustomAdvanced, SetNode, LTXVSeparateAVLatent, easy imageRemBg, easy imageRemBg, LTXVCropGuides, LTXVChunkFeedForward, ImageResizeKJv2, easy promptList, ImageInvert, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy promptReplace, easy promptReplace, easy promptReplace, easy promptLine, SetNode, easy convertAnything, ImageBatchMulti, EmptyImage, ImageInvert, EmptyImage, ImageBatchMulti, RegexExtract, RegexExtract, easy promptLine, RegexExtract, easy promptLine, easy convertAnything, SetNode, SetNode, LTXVConcatAVLatent, PrimitiveInt, easy indexAnything, GetNode, easy indexAnything, GetNode, ImageResizeKJv2, GetImagesFromBatchIndexed, easy indexAnything, easy indexAnything, LTXVEnhanceAVideoKJ, GetNode, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, LTXVPreprocess, ResizeImagesByLongerEdge, PrimitiveInt, GetNode, easy indexAnything, ComfyMathExpression, ComfyMathExpression, GetNode, LTXVConditioning, GetNode, LTXVEmptyLatentAudio, PrimitiveStringMultiline, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, GetNode, easy indexAnything, ResizeImageMaskNode, easy imageRemBg, GetImageRangeFromBatch, ColorMatch, ImageAddMulti, KSamplerSelect, VHS_VideoCombine, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy positive, LongTextToList, easy positive, GetNode, SetNode, SetNode, PrimitiveInt, ShowText|pysssss, INTConstant, INTConstant, LTXVAddGuideMulti, CLIPTextEncode, CLIPTextEncode, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V16.1(人物+场景)_2055880245324066818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055880245324066818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（113 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `CFGGuider`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `LTXVSeparateAVLatent`
- `easy imageRemBg`
- `easy imageRemBg`
- `LTXVCropGuides`
- `LTXVChunkFeedForward`
- `ImageResizeKJv2`
- `easy promptList`
- `ImageInvert`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy promptReplace`
- `easy promptReplace`
- `easy promptReplace`
- `easy promptLine`
- `SetNode`
- `easy convertAnything`
- `ImageBatchMulti`
- `EmptyImage`
- `ImageInvert`
- `EmptyImage`
- `ImageBatchMulti`
- `RegexExtract`
- `RegexExtract`
- `easy promptLine`
- `RegexExtract`
- `easy promptLine`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `easy indexAnything`
- `GetNode`
- `easy indexAnything`
- `GetNode`
- `ImageResizeKJv2`
- `GetImagesFromBatchIndexed`
- `easy indexAnything`
- `easy indexAnything`
- `LTXVEnhanceAVideoKJ`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `GetNode`
- `easy indexAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveStringMultiline`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `easy indexAnything`
- `ResizeImageMaskNode`
- `easy imageRemBg`
- `GetImageRangeFromBatch`
- `ColorMatch`
- `ImageAddMulti`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy positive`
- `LongTextToList`
- `easy positive`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `ShowText|pysssss`
- `INTConstant`
- `INTConstant`
- `LTXVAddGuideMulti`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（88/113）

**有卡**：`ManualSigmas`、`CFGGuider`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`easy imageRemBg`、`LTXVCropGuides`、`LTXVChunkFeedForward`、`ImageResizeKJv2`、`easy promptList`、`ImageInvert`、`easy indexAnything`、`easy promptReplace`、`easy promptLine`、`easy convertAnything`、`ImageBatchMulti`、`EmptyImage`、`RegexExtract`、`LTXVConcatAVLatent`、`GetImagesFromBatchIndexed`、`LTXVEnhanceAVideoKJ`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`ComfyMathExpression`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`GetImageRangeFromBatch`、`ColorMatch`、`ImageAddMulti`、`KSamplerSelect`、`VHS_VideoCombine`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`easy positive`、`LongTextToList`、`INTConstant`、`LTXVAddGuideMulti`、`CLIPTextEncode`、`RandomNoise`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
