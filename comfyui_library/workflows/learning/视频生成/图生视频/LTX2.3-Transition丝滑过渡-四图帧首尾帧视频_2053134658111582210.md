---
key: 视频生成/图生视频/LTX2.3-Transition丝滑过渡-四图帧首尾帧视频_2053134658111582210.json
name: LTX2.3-Transition丝滑过渡-四图帧首尾帧视频_2053134658111582210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2053134658111582210.json
hash: 485ac125ca066f10
coverage: 0.84058
learned_at: 2026-10-15 22:37:36
nodes: [ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, KSamplerSelect, ImageResizeKJv2, LTXVSeparateAVLatent, LTXVConcatAVLatent, CFGGuider, ManualSigmas, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LTXVConditioning, LTX2_NAG, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVEmptyLatentAudio, CLIPTextEncode, DualCLIPLoader, CLIPTextEncode, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, VAELoader, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVSeparateAVLatent, GetNode, LTXVLatentUpsampler, VAELoader, CFGGuider, SetNode, UNETLoader, CM_IntToFloat, VAELoaderKJ, GetNode, LTXVPreprocess, ImageResizeKJv2, ImageResizeKJv2, LTXVPreprocess, JWInteger, ImageScaleBy, GetImageSize, LTXVPreprocess, LTXVPreprocess, EmptyLTXVLatentVideo, SamplerCustomAdvanced, PrimitiveInt, LoadImage, LoadImage, JWInteger, VAEDecodeTiled, LTXVAudioVAEDecode, SetNode, SetNode, GetNode, GetNode, MarkdownNote, MarkdownNote, LoadImage, LTXVImgToVideoInplaceKJ, LoadImage, LoadImage, VHS_VideoCombine, PrimitiveInt, JWInteger, JWInteger, JWInteger, LoraLoaderModelOnly, TextInput_]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-Transition丝滑过渡-四图帧首尾帧视频_2053134658111582210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053134658111582210.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（69 个）：
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerSelect` ★核心
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `VAELoader`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `VAELoader`
- `CFGGuider`
- `SetNode`
- `UNETLoader` ★核心
- `CM_IntToFloat`
- `VAELoaderKJ`
- `GetNode`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `JWInteger`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `TextInput_`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（58/69）

**有卡**：`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`LTX2_NAG`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LTX2SamplingPreviewOverride`、`VAELoader`、`LTXVLatentUpsampler`、`UNETLoader`、`CM_IntToFloat`、`VAELoaderKJ`、`LTXVPreprocess`、`JWInteger`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LoadImage`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplaceKJ`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`TextInput_`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
