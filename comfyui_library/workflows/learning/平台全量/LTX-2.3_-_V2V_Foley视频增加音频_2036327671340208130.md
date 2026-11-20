---
key: 平台全量/LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130.json
name: LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130.json
hash: 34909d00ca999297
coverage: 0.534351
learned_at: 2026-11-14 00:37:08
nodes: [GetNode, GetNode, GetNode, VAEEncodeTiled, ManualSigmas, CFGGuider, GetNode, GetNode, GetNode, LTXVConditioning, GetNode, ImageResizeKJv2, LTXVLoopingSampler, MarkdownNote, KSamplerSelect, INTConstant, INTConstant, VHS_VideoCombine, VAEDecodeTiled, RandomNoise, SetNode, SetNode, SetNode, SetNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, SetNode, MarkdownNote, ManualSigmas, LTXVScheduler, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, CFGGuider, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VRAM_Debug, GetImageRangeFromBatch, GetNode, GetNode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, ManualSigmas, ManualSigmas, LTXVLatentUpsampler, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, SamplerCustomAdvanced, GetNode, CFGGuider, LTXVConcatAVLatent, SetNode, SetNode, MarkdownNote, VAEDecodeTiled, LTXVConditioning, SetNode, SetNode, GetNode, CLIPTextEncode, LatentUpscaleBy, GetNode, SimpleCalculatorKJ, GetNode, LTXVImgToVideoInplace, MarkdownNote, GetNode, LTXVAudioVAEDecode, VHS_VideoInfo, SetNode, SimpleCalculatorKJ, GetNode, SimpleCalculatorKJ, GetNode, GetNode, VAELoader, INTConstant, INTConstant, KSamplerSelect, KSamplerSelect, RandomNoise, RandomNoise, SimpleCalculatorKJ, SetNode, SetNode, INTConstant, MarkdownNote, VHS_VideoCombine, GetNode, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVAudioVideoMask, LTXVEmptyLatentAudio, VAEEncodeTiled, DualCLIPLoaderGGUF, UnetLoaderGGUF, VAELoader, LTX2_NAG, CLIPTextEncode, SetNode, PrimitiveFloat, VHS_LoadVideo, GetNode, ToInt, GetNode, LTX2SamplingPreviewOverride, UNETLoader, LTXVChunkFeedForward, ImageResizeKJv2, VHS_VideoCombine, SetNode, SetNode, GetImageSizeAndCount]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（131 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncodeTiled` ★核心
- `ManualSigmas`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVLoopingSampler` ★核心
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `MarkdownNote`
- `ManualSigmas`
- `LTXVScheduler`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VRAM_Debug`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoInfo`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `RandomNoise`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `INTConstant`
- `MarkdownNote`
- `VHS_VideoCombine`
- `GetNode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVideoMask`
- `LTXVEmptyLatentAudio` ★核心
- `VAEEncodeTiled` ★核心
- `DualCLIPLoaderGGUF`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `SetNode`
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `GetNode`
- `ToInt`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `UNETLoader` ★核心
- `LTXVChunkFeedForward`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（70/131）

**有卡**：`VAEEncodeTiled`、`ManualSigmas`、`CFGGuider`、`LTXVConditioning`、`ImageResizeKJv2`、`LTXVLoopingSampler`、`KSamplerSelect`、`INTConstant`、`VHS_VideoCombine`、`VAEDecodeTiled`、`RandomNoise`、`LTXVScheduler`、`LTXVSeparateAVLatent`、`VRAM_Debug`、`GetImageRangeFromBatch`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LatentUpscaleBy`、`SimpleCalculatorKJ`、`LTXVAudioVAEDecode`、`VHS_VideoInfo`、`VAELoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LTXVAudioVideoMask`、`LTXVEmptyLatentAudio`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUF`、`LTX2_NAG`、`VHS_LoadVideo`、`ToInt`、`LTX2SamplingPreviewOverride`、`UNETLoader`、`LTXVChunkFeedForward`、`GetImageSizeAndCount`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、LTXVLoopingSampler
