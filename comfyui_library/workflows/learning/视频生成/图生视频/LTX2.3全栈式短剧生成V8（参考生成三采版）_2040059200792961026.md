---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V8（参考生成三采版）_2040059200792961026.json
name: LTX2.3全栈式短剧生成V8（参考生成三采版）_2040059200792961026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2040059200792961026.json
hash: 63e83f6151a6b563
coverage: 0.78125
learned_at: 2026-10-15 22:36:14
nodes: [easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, LTXVEmptyLatentAudio, SetNode, PrimitiveStringMultiline, easy promptReplace, GetNode, SetNode, GetNode, easy indexAnything, SetNode, SetNode, LTXVConditioning, GetNode, PrimitiveInt, LoadImage, easy promptLine, RegexExtract, easy promptLine, easy convertAnything, GetImagesFromBatchIndexed, easy batchAnything, easy forLoopEnd, easy forLoopStart, KSamplerSelect, easy promptList, easy promptReplace, RegexExtract, RegexExtract, easy promptLine, ImageResizeKJv2, easy indexAnything, easy indexAnything, PrimitiveInt, CFGGuider, ImageAddMulti, easy imageRemBg, ManualSigmas, KSamplerSelect, ManualSigmas, LTXAddVideoICLoRAGuideAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, GetNode, LTXVImgToVideoInplace, LTXVLatentUpsampler, TrimVideoLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVCropGuides, LTXVCropGuides, GetNode, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, GetNode, CFGGuider, GetNode, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVConcatAVLatent, ImageResizeKJv2, ResizeImageMaskNode, ComfyMathExpression, PreviewImage, ResizeImagesByLongerEdge, LTXVPreprocess, easy indexAnything, CLIPTextEncode, easy imageRemBg, GetNode, GetNode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, GetNode, GetNode, LTXVImgToVideoInplace, VHS_VideoCombine, RandomNoise, RandomNoise, RandomNoise, CLIPTextEncode, EmptyImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageBatchMulti, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, GetNode, INTConstant, INTConstant, ComfyMathExpression, easy positive, easy positive, SetNode, easy promptConcat, easy positive, easy positive, ShowText|pysssss, LongTextToList, INTConstant, GetNode, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAEDecodeTiled, LTXVAudioVAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V8（参考生成三采版）_2040059200792961026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040059200792961026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（128 个）：
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `PrimitiveStringMultiline`
- `easy promptReplace`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy indexAnything`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `PrimitiveInt`
- `LoadImage`
- `easy promptLine`
- `RegexExtract`
- `easy promptLine`
- `easy convertAnything`
- `GetImagesFromBatchIndexed`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `KSamplerSelect` ★核心
- `easy promptList`
- `easy promptReplace`
- `RegexExtract`
- `RegexExtract`
- `easy promptLine`
- `ImageResizeKJv2`
- `easy indexAnything`
- `easy indexAnything`
- `PrimitiveInt`
- `CFGGuider`
- `ImageAddMulti`
- `easy imageRemBg`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXAddVideoICLoRAGuideAdvanced`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `TrimVideoLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVCropGuides`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `PreviewImage`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `easy imageRemBg`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `VHS_VideoCombine`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageBatchMulti`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `ComfyMathExpression`
- `easy positive`
- `easy positive`
- `SetNode`
- `easy promptConcat`
- `easy positive`
- `easy positive`
- `ShowText|pysssss`
- `LongTextToList`
- `INTConstant`
- `GetNode`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（100/128）

**有卡**：`easy indexAnything`、`LTXVEmptyLatentAudio`、`easy promptReplace`、`LTXVConditioning`、`LoadImage`、`easy promptLine`、`RegexExtract`、`easy convertAnything`、`GetImagesFromBatchIndexed`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`KSamplerSelect`、`easy promptList`、`ImageResizeKJv2`、`CFGGuider`、`ImageAddMulti`、`easy imageRemBg`、`ManualSigmas`、`LTXAddVideoICLoRAGuideAdvanced`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`TrimVideoLatent`、`LTXVCropGuides`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`CLIPTextEncode`、`VHS_VideoCombine`、`RandomNoise`、`EmptyImage`、`ImageBatchMulti`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`INTConstant`、`easy positive`、`easy promptConcat`、`LongTextToList`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
