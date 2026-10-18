---
key: 音频生成/音频生成/LTX-2.3视频扩展（完美扩展版）_2045860108604805122.json
name: LTX-2.3视频扩展（完美扩展版）_2045860108604805122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX-2.3视频扩展（完美扩展版）_2045860108604805122.json
hash: 88eabbd830c0e953
coverage: 0.403101
learned_at: 2026-10-18 03:04:51
nodes: [LTXVConditioning, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXAddVideoICLoRAGuide, LTXVCropGuides, ManualSigmas, ResizeImageMaskNode, VHS_VideoInfo, ImagePadKJ, SetNode, SetNode, SetNode, SetNode, SetNode, LTX2AttentionTunerPatch, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, ComfyMathExpression, SetNode, INTConstant, LTX2_NAG, GetNode, GetNode, GetNode, PreviewAny, GetImageRangeFromBatch, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, PreviewImage, GetImageRangeFromBatch, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ComfySwitchNode, GetNode, SetNode, GetNode, SetNode, GetNode, ResizeImageMaskNode, GetImageSizeAndCount, TextGenerateLTX2Prompt, StringConcatenate, SetNode, SimpleMath+, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, DualCLIPLoader, INTConstant, GetNode, UNETLoader, SetNode, GetNode, VHS_LoadVideoFFmpeg, PrimitiveStringMultiline, INTConstant, INTConstant, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, easy showAnything, LazySwitchKJ, GetNode, PrimitiveStringMultiline, PrimitiveBoolean, INTConstant, INTConstant, PrimitiveBoolean, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 音频生成/音频生成/LTX-2.3视频扩展（完美扩展版）_2045860108604805122.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX-2.3视频扩展（完美扩展版）_2045860108604805122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（129 个）：
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVCropGuides`
- `ManualSigmas`
- `ResizeImageMaskNode`
- `VHS_VideoInfo`
- `ImagePadKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `INTConstant`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `GetImageSizeAndCount`
- `TextGenerateLTX2Prompt`
- `StringConcatenate`
- `SetNode`
- `SimpleMath+`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `DualCLIPLoader`
- `INTConstant`
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `VHS_LoadVideoFFmpeg`
- `PrimitiveStringMultiline`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LazySwitchKJ`
- `GetNode`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **40%**（52/129）

**有卡**：`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`LTXVCropGuides`、`ManualSigmas`、`ResizeImageMaskNode`、`VHS_VideoInfo`、`ImagePadKJ`、`LTX2AttentionTunerPatch`、`LTX2SamplingPreviewOverride`、`ComfyMathExpression`、`INTConstant`、`LTX2_NAG`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`TextGenerateLTX2Prompt`、`StringConcatenate`、`SimpleMath+`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`VHS_LoadVideoFFmpeg`、`VHS_VideoCombine`、`CLIPTextEncode`、`LazySwitchKJ`、`PrimitiveBoolean`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
