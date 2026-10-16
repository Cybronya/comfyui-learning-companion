---
key: 视频生成/图生视频/【数字人唱歌】LTX2.3_2057291924830248961.json
name: 【数字人唱歌】LTX2.3_2057291924830248961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2057291924830248961.json
hash: 613490c2353adb92
coverage: 0.885246
learned_at: 2026-10-15 22:38:10
nodes: [INTConstant, INTConstant, AudioInfo, SimpleMath+, SimpleMath+, Display Any (rgthree), SetNode, LTXVImgToVideoInplace, SetNode, EmptyLTXVLatentVideo, GetNode, LTXVPreprocess, INTConstant, LTXVConcatAVLatent, SetLatentNoiseMask, ImageResizeKJv2, ResizeImagesByLongerEdge, JDC_ResizeFactor, GetImageSize, SetNode, LTXVAudioVAEEncode, LTXVScheduler, SolidMask, SamplerCustom, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVLatentUpsampler, Seed (rgthree), LTX2_NAG, GetNode, LTXVConcatAVLatent, LTXVScheduler, LTXVChunkFeedForward, LTXVConditioning, PathchSageAttentionKJ, KSamplerSelect, KSamplerSelect, ManualSigmas, SamplerCustom, SimpleMath+, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, SetNode, ManualSigmas, SetNode, PrimitiveBoolean, LoadImage, PreviewAudio, VAEDecodeTiled, AudioCrop, VHS_VideoCombine, VAELoader, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, LoraLoaderModelOnly, UNETLoader, LoadAudio, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/【数字人唱歌】LTX2.3_2057291924830248961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057291924830248961.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
- `INTConstant`
- `INTConstant`
- `AudioInfo`
- `SimpleMath+`
- `SimpleMath+`
- `Display Any (rgthree)`
- `SetNode`
- `LTXVImgToVideoInplace`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVPreprocess`
- `INTConstant`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `JDC_ResizeFactor`
- `GetImageSize`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `LTXVScheduler`
- `SolidMask`
- `SamplerCustom` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Seed (rgthree)`
- `LTX2_NAG`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `LTXVChunkFeedForward`
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustom` ★核心
- `SimpleMath+`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `PrimitiveBoolean`
- `LoadImage`
- `PreviewAudio`
- `VAEDecodeTiled` ★核心
- `AudioCrop`
- `VHS_VideoCombine`
- `VAELoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（54/61）

**有卡**：`INTConstant`、`AudioInfo`、`SimpleMath+`、`Display Any (rgthree)`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`JDC_ResizeFactor`、`GetImageSize`、`LTXVAudioVAEEncode`、`LTXVScheduler`、`SolidMask`、`SamplerCustom`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`Seed (rgthree)`、`LTX2_NAG`、`LTXVChunkFeedForward`、`LTXVConditioning`、`PathchSageAttentionKJ`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`PrimitiveBoolean`、`LoadImage`、`PreviewAudio`、`VAEDecodeTiled`、`AudioCrop`、`VHS_VideoCombine`、`VAELoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadAudio`、`CLIPTextEncode`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler
