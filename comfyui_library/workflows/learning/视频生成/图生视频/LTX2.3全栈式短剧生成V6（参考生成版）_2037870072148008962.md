---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V6（参考生成版）_2037870072148008962.json
name: LTX2.3全栈式短剧生成V6（参考生成版）_2037870072148008962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3全栈式短剧生成V6（参考生成版）_2037870072148008962.json
hash: 70c5f811bb512739
coverage: 0.775862
learned_at: 2026-10-15 22:35:59
nodes: [easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy promptList, GetNode, LTXVEmptyLatentAudio, PrimitiveInt, easy indexAnything, SetNode, easy promptLine, PrimitiveStringMultiline, RegexExtract, easy promptLine, easy promptReplace, RegexExtract, ResizeImageMaskNode, ResizeImagesByLongerEdge, GetNode, EmptyImage, ManualSigmas, ComfyMathExpression, CFGGuider, ImageResizeKJv2, easy promptReplace, easy promptLine, SetNode, easy promptReplace, easy indexAnything, GetNode, easy indexAnything, easy indexAnything, RegexExtract, easy convertAnything, SetNode, SetNode, SetNode, PreviewImage, ImageBatchMulti, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConcatAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, ComfyMathExpression, INTConstant, ComfyMathExpression, INTConstant, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, CFGGuider, GetNode, LTXVPreprocess, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, TrimVideoLatent, LTXVAudioVAEDecode, easy forLoopEnd, ComfyMathExpression, PrimitiveInt, easy forLoopStart, easy batchAnything, easy batchAnything, easy positive, easy positive, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVCropGuides, RandomNoise, GetNode, ManualSigmas, ImageAddMulti, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, LoadImage, GetNode, GetImagesFromBatchIndexed, easy positive, easy indexAnything, ShowText|pysssss, easy promptConcat, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, INTConstant, CLIPTextEncode, LTXVAddGuideMulti, easy imageRemBg, easy imageRemBg, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V6（参考生成版）_2037870072148008962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037870072148008962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy promptList`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `easy indexAnything`
- `SetNode`
- `easy promptLine`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `easy promptLine`
- `easy promptReplace`
- `RegexExtract`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `EmptyImage`
- `ManualSigmas`
- `ComfyMathExpression`
- `CFGGuider`
- `ImageResizeKJv2`
- `easy promptReplace`
- `easy promptLine`
- `SetNode`
- `easy promptReplace`
- `easy indexAnything`
- `GetNode`
- `easy indexAnything`
- `easy indexAnything`
- `RegexExtract`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `ImageBatchMulti`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `ComfyMathExpression`
- `INTConstant`
- `ComfyMathExpression`
- `INTConstant`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `GetNode`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `TrimVideoLatent`
- `LTXVAudioVAEDecode` ★核心
- `easy forLoopEnd`
- `ComfyMathExpression`
- `PrimitiveInt`
- `easy forLoopStart`
- `easy batchAnything`
- `easy batchAnything`
- `easy positive`
- `easy positive`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `RandomNoise`
- `GetNode`
- `ManualSigmas`
- `ImageAddMulti`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LoadImage`
- `GetNode`
- `GetImagesFromBatchIndexed`
- `easy positive`
- `easy indexAnything`
- `ShowText|pysssss`
- `easy promptConcat`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXVAddGuideMulti`
- `easy imageRemBg`
- `easy imageRemBg`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（90/116）

**有卡**：`easy indexAnything`、`easy promptList`、`LTXVEmptyLatentAudio`、`easy promptLine`、`RegexExtract`、`easy promptReplace`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`EmptyImage`、`ManualSigmas`、`ComfyMathExpression`、`CFGGuider`、`ImageResizeKJv2`、`easy convertAnything`、`ImageBatchMulti`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`INTConstant`、`KSamplerSelect`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`TrimVideoLatent`、`LTXVAudioVAEDecode`、`easy forLoopEnd`、`easy forLoopStart`、`easy batchAnything`、`easy positive`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`RandomNoise`、`ImageAddMulti`、`LoadImage`、`GetImagesFromBatchIndexed`、`easy promptConcat`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LatentUpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVAddGuideMulti`、`easy imageRemBg`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
