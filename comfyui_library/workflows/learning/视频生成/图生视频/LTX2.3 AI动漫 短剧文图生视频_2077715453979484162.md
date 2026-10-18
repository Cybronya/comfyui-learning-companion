---
key: 视频生成/图生视频/LTX2.3 AI动漫 短剧文图生视频_2077715453979484162.json
name: LTX2.3 AI动漫 短剧文图生视频_2077715453979484162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 AI动漫 短剧文图生视频_2077715453979484162.json
hash: 6ae10fd866bd9e21
coverage: 0.867647
learned_at: 2026-10-15 22:41:44
nodes: [CFGGuider, KSamplerSelect, SamplerCustomAdvanced, VAELoaderKJ, VAELoader, CLIPTextEncode, CFGGuider, LTX2SamplingPreviewOverride, LTXVConditioning, LTX2_NAG, ImageScaleBy, SimpleMath+, SimpleMath+, CLIPTextEncode, GetImageSize, VAELoader, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplace, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVAudioVAEDecode, VAEDecode, VHS_VideoCombine, VAEDecode, Reroute, ComfySwitchNode, VHS_VideoCombine, ManualSigmas, LTXVScheduler, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LTXVCropGuides, LayerUtility: PurgeVRAM V2, LTXVLatentUpsampler, JoinStrings, RandomNoise, PrimitiveBoolean, ImageScaleToTotalPixels, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, EmptyImage, PrimitiveInt, UNETLoader, DualCLIPLoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveBoolean, easy int, easy int, Reroute, ResolutionSelector, GetImageSize, ComfySwitchNode, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 AI动漫 短剧文图生视频_2077715453979484162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2077715453979484162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（68 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoaderKJ`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `LTX2_NAG`
- `ImageScaleBy`
- `SimpleMath+`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `VAELoader`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Reroute`
- `ComfySwitchNode`
- `VHS_VideoCombine`
- `ManualSigmas`
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM V2`
- `LTXVLatentUpsampler` ★核心
- `JoinStrings`
- `RandomNoise`
- `PrimitiveBoolean`
- `ImageScaleToTotalPixels`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `EmptyImage`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `easy int`
- `easy int`
- `Reroute`
- `ResolutionSelector`
- `GetImageSize`
- `ComfySwitchNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（59/68）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAELoaderKJ`、`VAELoader`、`CLIPTextEncode`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`LTX2_NAG`、`ImageScaleBy`、`SimpleMath+`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplace`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`VHS_VideoCombine`、`LTXVScheduler`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LayerUtility: PurgeVRAM V2`、`LTXVLatentUpsampler`、`JoinStrings`、`RandomNoise`、`PrimitiveBoolean`、`ImageScaleToTotalPixels`、`EmptyImage`、`UNETLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`easy int`、`ResolutionSelector`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ResolutionSelector、LoadImage、UNETLoader、CFGGuider
