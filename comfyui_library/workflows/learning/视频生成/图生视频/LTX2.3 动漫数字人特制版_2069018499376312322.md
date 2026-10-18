---
key: 视频生成/图生视频/LTX2.3 动漫数字人特制版_2069018499376312322.json
name: LTX2.3 动漫数字人特制版_2069018499376312322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 动漫数字人特制版_2069018499376312322.json
hash: 8a1cfb70cd747f28
coverage: 0.809524
learned_at: 2026-10-15 22:40:25
nodes: [CLIPTextEncode, SoundFlow_GetLength, LTXVAudioVAEEncode, PrimitiveInt, easy showAnything, SolidMask, SimpleMath+, PrimitiveBoolean, SetLatentNoiseMask, LTX2_NAG, PrimitiveInt, PrimitiveBoolean, Reroute, LTXVConcatAVLatent, LTXVConditioning, LayerUtility: PurgeVRAM V2, LTX2SamplingPreviewOverride, ComfyMathExpression, EmptyLTXVLatentVideo, Reroute, MelBandRoFormerModelLoader, MelBandRoFormerSampler, LTXVEmptyLatentAudio, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, VAELoaderKJ, CFGGuider, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, SetNode, GetNode, easy showAnything, ComfySwitchNode, ComfySwitchNode, VAEDecode, SamplerCustomAdvanced, VHS_VideoCombine, JoinStringMulti, DualCLIPLoader, RandomNoise, TrimAudioDuration, easy int, easy int, LoraLoaderModelOnly, CLIPTextEncode, PrimitiveStringMultiline, PreviewAudio, easy float, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LTXVPreprocess, ImageResizeKJv2, GetImageSize, ResolutionSelector, ImageScaleToTotalPixels, LTXVImgToVideoInplace, easy float, LoadAudio, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 动漫数字人特制版_2069018499376312322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069018499376312322.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（63 个）：
- `CLIPTextEncode` ★核心
- `SoundFlow_GetLength`
- `LTXVAudioVAEEncode` ★核心
- `PrimitiveInt`
- `easy showAnything`
- `SolidMask`
- `SimpleMath+`
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `LTX2_NAG`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `Reroute`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LayerUtility: PurgeVRAM V2`
- `LTX2SamplingPreviewOverride`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `JoinStringMulti`
- `DualCLIPLoader`
- `RandomNoise`
- `TrimAudioDuration`
- `easy int`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PreviewAudio`
- `easy float`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `GetImageSize`
- `ResolutionSelector`
- `ImageScaleToTotalPixels`
- `LTXVImgToVideoInplace`
- `easy float`
- `LoadAudio`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（51/63）

**有卡**：`CLIPTextEncode`、`SoundFlow_GetLength`、`LTXVAudioVAEEncode`、`SolidMask`、`SimpleMath+`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LayerUtility: PurgeVRAM V2`、`LTX2SamplingPreviewOverride`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVEmptyLatentAudio`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVSeparateAVLatent`、`VAEDecode`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`JoinStringMulti`、`DualCLIPLoader`、`RandomNoise`、`TrimAudioDuration`、`easy int`、`LoraLoaderModelOnly`、`PreviewAudio`、`easy float`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageResizeKJv2`、`GetImageSize`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LTXVImgToVideoInplace`、`LoadAudio`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ResolutionSelector、LoadImage、UNETLoader、CFGGuider
