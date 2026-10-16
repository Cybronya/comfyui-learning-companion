---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V8（参考图生成版）图生视频短剧版短剧分镜版_2064338058337673217.json
name: LTX2.3全栈式短剧生成V8（参考图生成版）图生视频短剧版短剧分镜版_2064338058337673217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064338058337673217.json
hash: 7e6159f525d57a54
coverage: 0.777778
learned_at: 2026-10-15 22:39:23
nodes: [easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, LTXVEmptyLatentAudio, SetNode, PrimitiveStringMultiline, easy promptReplace, GetNode, SetNode, GetNode, easy indexAnything, SetNode, SetNode, LTXVConditioning, PrimitiveInt, easy positive, easy positive, LoadImage, easy promptLine, RegexExtract, easy promptLine, easy convertAnything, easy batchAnything, easy forLoopEnd, easy forLoopStart, KSamplerSelect, easy promptReplace, RegexExtract, RegexExtract, easy promptLine, ImageResizeKJv2, CFGGuider, ImageAddMulti, easy imageRemBg, ManualSigmas, KSamplerSelect, ManualSigmas, LTXAddVideoICLoRAGuideAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, GetNode, LTXVImgToVideoInplace, LTXVLatentUpsampler, TrimVideoLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVCropGuides, LTXVCropGuides, GetNode, ComfyMathExpression, EmptyLTXVLatentVideo, GetNode, CFGGuider, GetNode, SamplerCustomAdvanced, LTXVConcatAVLatent, easy indexAnything, ImageResizeKJv2, ResizeImageMaskNode, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, CLIPTextEncode, LTXVAudioVAEDecode, GetNode, VAEDecodeTiled, GetNode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, GetNode, GetNode, LTXVImgToVideoInplace, VHS_VideoCombine, RandomNoise, RandomNoise, RandomNoise, easy promptConcat, easy positive, EmptyImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, LTXVChunkFeedForward, UNETLoader, GetNode, INTConstant, INTConstant, ComfyMathExpression, INTConstant, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, PrimitiveInt, easy indexAnything, ComfyMathExpression, GetNode, GetNode, easy promptList, CLIPTextEncode, PreviewImage, easy imageRemBg, GetImagesFromBatchIndexed, ImageBatchMulti, easy indexAnything, easy indexAnything, SetNode, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V8（参考图生成版）图生视频短剧版短剧分镜版_2064338058337673217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064338058337673217.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（126 个）：
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
- `PrimitiveInt`
- `easy positive`
- `easy positive`
- `LoadImage`
- `easy promptLine`
- `RegexExtract`
- `easy promptLine`
- `easy convertAnything`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `KSamplerSelect` ★核心
- `easy promptReplace`
- `RegexExtract`
- `RegexExtract`
- `easy promptLine`
- `ImageResizeKJv2`
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
- `EmptyLTXVLatentVideo`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `easy indexAnything`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
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
- `easy promptConcat`
- `easy positive`
- `EmptyImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `GetNode`
- `INTConstant`
- `INTConstant`
- `ComfyMathExpression`
- `INTConstant`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `easy indexAnything`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `easy promptList`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `easy imageRemBg`
- `GetImagesFromBatchIndexed`
- `ImageBatchMulti`
- `easy indexAnything`
- `easy indexAnything`
- `SetNode`
- `ShowText|pysssss`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（98/126）

**有卡**：`easy indexAnything`、`LTXVEmptyLatentAudio`、`easy promptReplace`、`LTXVConditioning`、`easy positive`、`LoadImage`、`easy promptLine`、`RegexExtract`、`easy convertAnything`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`KSamplerSelect`、`ImageResizeKJv2`、`CFGGuider`、`ImageAddMulti`、`easy imageRemBg`、`ManualSigmas`、`LTXAddVideoICLoRAGuideAdvanced`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`TrimVideoLatent`、`LTXVCropGuides`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VHS_VideoCombine`、`RandomNoise`、`easy promptConcat`、`EmptyImage`、`VAELoaderKJ`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LatentUpscaleModelLoader`、`LTXVChunkFeedForward`、`UNETLoader`、`INTConstant`、`LTXICLoRALoaderModelOnly`、`easy promptList`、`GetImagesFromBatchIndexed`、`ImageBatchMulti`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
