---
key: 图片生成/文生图/QIANSUI+LTX2.3+图文生视频_2032449219776221185.json
name: QIANSUI+LTX2.3+图文生视频_2032449219776221185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QIANSUI+LTX2.3+图文生视频_2032449219776221185.json
hash: bc8081cdf0ba5a89
coverage: 0.806818
learned_at: 2026-10-21 02:54:00
nodes: [GetNode, RH_LLMAPI_Pro_Node, ImageScaleToTotalPixels, PreviewAny, easy ifElse, SetNode, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CheckpointLoaderSimple, CLIPTextEncode, MathExpression|pysssss, ResizeImagesByShorterEdge, SimpleMathDual+, GetNode, Any Switch (rgthree), CreateVideo, LTXVAudioVAEDecode, SetLatentNoiseMask, AudioCrop, SolidMask, Audio Duration (mtb), MathExpression|pysssss, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVAudioVAELoader, LoadAudio, LTXVAudioVAEDecode, VAEDecodeTiled, MarkdownNote, LTX2_NAG, LTXVEnhanceAVideoKJ, LTXVEmptyLatentAudio, GetNode, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, RandomNoise, Any Switch (rgthree), CFGGuider, KSamplerSelect, ManualSigmas, LTXVCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, RandomNoise, GetNode, ManualSigmas, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, SamplerCustomAdvanced, KSamplerSelect, Sigmas Rescale, LTXVConcatAVLatent, CFGGuider, easy positive, PrimitiveInt, CM_IntToFloat, CM_IntToFloat, easy float, easy float, easy int, LTXVImgToVideoConditionOnly, PrimitiveBoolean, PrimitiveBoolean, SaveVideo, VHS_VideoCombine, CLIPTextEncode, VAEDecodeTiled, CreateVideo, Any Switch (rgthree), SaveVideo, LTXVCropGuides, LTXVConditioning, easy convertAnything, PrimitiveInt, PrimitiveInt, Any Switch (rgthree), LTXVPreprocess, GetImageSize, ImageResizeKJv2, VHS_VideoCombine, LoadImage, 图像缩放V2_孤海, easy float, PrimitiveInt, easy int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/QIANSUI+LTX2.3+图文生视频_2032449219776221185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QIANSUI+LTX2.3+图文生视频_2032449219776221185.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `ImageScaleToTotalPixels`
- `PreviewAny`
- `easy ifElse`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `ResizeImagesByShorterEdge`
- `SimpleMathDual+`
- `GetNode`
- `Any Switch (rgthree)`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `SetLatentNoiseMask`
- `AudioCrop`
- `SolidMask`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `LTXVAudioVAEEncode` ★核心
- `LTXVAudioVAELoader`
- `LTXVAudioVAELoader`
- `LoadAudio`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `LTX2_NAG`
- `LTXVEnhanceAVideoKJ`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `Any Switch (rgthree)`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Sigmas Rescale`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `easy positive`
- `PrimitiveInt`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `easy float`
- `easy float`
- `easy int`
- `LTXVImgToVideoConditionOnly`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `SaveVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `Any Switch (rgthree)`
- `SaveVideo`
- `LTXVCropGuides`
- `LTXVConditioning`
- `easy convertAnything`
- `PrimitiveInt`
- `PrimitiveInt`
- `Any Switch (rgthree)`
- `LTXVPreprocess`
- `GetImageSize`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`
- `图像缩放V2_孤海`
- `easy float`
- `PrimitiveInt`
- `easy int`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（71/88）

**有卡**：`RH_LLMAPI_Pro_Node`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`MathExpression|pysssss`、`ResizeImagesByShorterEdge`、`SimpleMathDual+`、`CreateVideo`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`AudioCrop`、`SolidMask`、`Audio Duration (mtb)`、`LTXVAudioVAEEncode`、`LTXVAudioVAELoader`、`LoadAudio`、`VAEDecodeTiled`、`LTX2_NAG`、`LTXVEnhanceAVideoKJ`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`Sigmas Rescale`、`easy positive`、`CM_IntToFloat`、`easy float`、`easy int`、`PrimitiveBoolean`、`SaveVideo`、`VHS_VideoCombine`、`LTXVConditioning`、`easy convertAnything`、`LTXVPreprocess`、`GetImageSize`、`ImageResizeKJv2`、`LoadImage`、`图像缩放V2_孤海`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
