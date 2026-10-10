---
key: 视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json
name: SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json
hash: 3ee5a201c19a9eeb
coverage: 0.781095
learned_at: 2026-10-10 23:05:14
nodes: [KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, CFGGuider, ManualSigmas, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXAVTextEncoderLoader, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVConcatAVLatent, RandomNoise, easy showAnything, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTXVAddGuideMulti, VAEDecodeTiled, PrimitiveNode, PrimitiveNode, PrimitiveNode, easy mathInt, CFGGuider, VAEDecodeTiled, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVEmptyLatentAudio, CFGGuider, LTXVSeparateAVLatent, RandomNoise, EmptyLTXVLatentVideo, LTXVPreprocess, ResizeLongestToNode, image_scale_pixel_v2, LTXAVTextEncoderLoader, CM_FloatToInt, ImageResizeKJv2, PrimitiveFloat, CM_FloatToInt, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVConditioning, LTXVAddGuideMulti, LTXVAddGuideMulti, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LTXVAudioVAEDecode, VHS_MergeImages, AudioConcat, SamplerCustomAdvanced, ImageResizeKJv2, PrimitiveInt, LTXVAddGuideMulti, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, JWStringGetLine, 1hew_ImageGridSplit, 1hew_ImageGridSplit, 1hew_ImageGridSplit, 1hew_ImageGridSplit, JWStringGetLine, ShowText, JjkConcat, ShowText, easy saveText, RH_LLMAPI_Pro_Node, easy saveText, ShowText, ShowText, ImageSizeInfo, ImageSizeInfo, ImageSizeInfo, ImageSizeInfo, ImageSizeInfo, JWImageSequenceExtractFromBatch, easy mathInt, easy mathInt, 1hew_ImageGridSplit, JWImageSequenceExtractFromBatch, LTXVAudioVAEDecode, LoadImage, PrimitiveNode, PrimitiveNode, LTXVAddGuideMulti, PrimitiveFloat, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LTXVConditioning, LTXVPreprocess, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, LTXVLatentUpsampler, LTXVSeparateAVLatent, PreviewImage, 1hew_ImageGridSplit, 1hew_ImageGridSplit, ImageSizeInfo, ImageSizeInfo, ImageSizeInfo, ImageSizeInfo, LTXVLatentUpsampler, DisTorchPurgeVRAMV2, DisTorchPurgeVRAMV2, LTXVLatentUpsampler, ResizeLongestToNode, LTXVSeparateAVLatent, PrimitiveInt, DF_Integer, DF_Integer, PrimitiveFloat, easy mathInt, GetImageSize+, GetImageSize+, LTXVAddGuideMulti, LTXVConcatAVLatent, LTXVLatentUpsampler, image_scale_pixel_v2, PrimitiveNode, LTXVEmptyLatentAudio, easy showAnything, ShowText, VHS_VideoCombine, LoraLoaderModelOnly, PrimitiveNode, LTXVAddGuideMulti, easy mathInt, JWInteger, RH_Nano_Banana2_Gemini31Flash, JWInteger, easy mathInt, easy mathInt, CLIPTextEncode, RH_LLMAPI_Pro_Node, PreviewImage, string_util_StrFind, JjkConcat, If ANY execute A else B, JWStringGetLine, JWStringSplit, RH_LLMAPI_Pro_Node, TextBoxMira, TextBoxMira, PrimitiveNode, PrimitiveNode, PrimitiveFloat, PrimitiveFloat, LTXVAudioVAELoader, LatentUpscaleModelLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: [If ANY execute A else B, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, GetImageSize+, GetImageSize+, easy saveText, easy saveText]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SBAPI三分镜叙事长视频Gemini图文优化+LTX23+VBVR+LoRA六阶段采样_2082795014106730497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（201 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `easy showAnything`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `VAEDecodeTiled` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy mathInt`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `ResizeLongestToNode`
- `image_scale_pixel_v2`
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_MergeImages`
- `AudioConcat`
- `SamplerCustomAdvanced` ★核心
- `ImageResizeKJv2`
- `PrimitiveInt`
- `LTXVAddGuideMulti`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `JWStringGetLine`
- `1hew_ImageGridSplit`
- `1hew_ImageGridSplit`
- `1hew_ImageGridSplit`
- `1hew_ImageGridSplit`
- `JWStringGetLine`
- `ShowText`
- `JjkConcat`
- `ShowText`
- `easy saveText`
- `RH_LLMAPI_Pro_Node`
- `easy saveText`
- `ShowText`
- `ShowText`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `JWImageSequenceExtractFromBatch`
- `easy mathInt`
- `easy mathInt`
- `1hew_ImageGridSplit`
- `JWImageSequenceExtractFromBatch`
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `LTXVAddGuideMulti`
- `PrimitiveFloat`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `PreviewImage`
- `1hew_ImageGridSplit`
- `1hew_ImageGridSplit`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `ImageSizeInfo`
- `LTXVLatentUpsampler` ★核心
- `DisTorchPurgeVRAMV2`
- `DisTorchPurgeVRAMV2`
- `LTXVLatentUpsampler` ★核心
- `ResizeLongestToNode`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `DF_Integer`
- `DF_Integer`
- `PrimitiveFloat`
- `easy mathInt`
- `GetImageSize+`
- `GetImageSize+`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `image_scale_pixel_v2`
- `PrimitiveNode`
- `LTXVEmptyLatentAudio` ★核心
- `easy showAnything`
- `ShowText`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `LTXVAddGuideMulti`
- `easy mathInt`
- `JWInteger`
- `RH_Nano_Banana2_Gemini31Flash`
- `JWInteger`
- `easy mathInt`
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `PreviewImage`
- `string_util_StrFind`
- `JjkConcat`
- `If ANY execute A else B`
- `JWStringGetLine`
- `JWStringSplit`
- `RH_LLMAPI_Pro_Node`
- `TextBoxMira`
- `TextBoxMira`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **78%**（157/201）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`LTXVLatentUpsampler`、`ImageResizeKJv2`、`LTXVPreprocess`、`LTXVAddGuideMulti`、`VAEDecodeTiled`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ResizeLongestToNode`、`image_scale_pixel_v2`、`CM_FloatToInt`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`VHS_MergeImages`、`AudioConcat`、`JWStringGetLine`、`1hew_ImageGridSplit`、`ShowText`、`JjkConcat`、`RH_LLMAPI_Pro_Node`、`ImageSizeInfo`、`JWImageSequenceExtractFromBatch`、`LoadImage`、`DisTorchPurgeVRAMV2`、`DF_Integer`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`JWInteger`、`RH_Nano_Banana2_Gemini31Flash`、`string_util_StrFind`、`JWStringSplit`、`TextBoxMira`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`

**缺卡**（12）：`If ANY execute A else B`、`easy mathInt`、`easy mathInt`、`easy mathInt`、`easy mathInt`、`easy mathInt`、`easy mathInt`、`easy mathInt`、`GetImageSize+`、`GetImageSize+`、`easy saveText`、`easy saveText`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
