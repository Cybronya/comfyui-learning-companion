---
key: 视频生成/图生视频/LTX2.3-文+图+音频_2039311541685719041.json
name: LTX2.3-文+图+音频_2039311541685719041.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-文+图+音频_2039311541685719041.json
hash: 051961fd113a086c
coverage: 0.916667
learned_at: 2026-10-15 22:36:08
nodes: [CFGGuider, CFGGuider, TextGenerateLTX2Prompt, LatentUpscaleModelLoader, EmptyImage, ImageScaleBy, KSamplerSelect, VAELoader, CLIPTextEncode, GetImageSize, LTXVAudioVAEEncode, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, GetImageSize, MelBandRoFormerSampler, LTXVSeparateAVLatent, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVPreprocess, VAELoaderKJ, VAELoader, LTXVScheduler, SolidMask, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVCropGuides, RandomNoise, LTXVImgToVideoInplace, VHS_VideoCombine, VHS_VideoCombine, LTXVSetAudioVideoMaskByTime, LTXVConcatAVLatent, LTXVSeparateAVLatent, SetLatentNoiseMask, ResizeImagesByLongerEdge, MarkdownNote, easy cleanGpuUsed, LTXVConcatAVLatent, easy cleanGpuUsed, RandomNoise, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, KSamplerSelect, PrimitiveBoolean, LTXVEmptyLatentAudio, PrimitiveInt, PrimitiveInt, PrimitiveFloat, ResizeImageMaskNode, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, ManualSigmas, LTXVImgToVideoInplace, SamplerCustomAdvanced, VAEDecodeTiled, VRAM_Debug, MelBandRoFormerModelLoader, PreviewAudio, MarkdownNote, MarkdownNote, DualCLIPLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, LoadAudio, TrimAudioDuration, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-文+图+音频_2039311541685719041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039311541685719041.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（72 个）：
- `CFGGuider`
- `CFGGuider`
- `TextGenerateLTX2Prompt`
- `LatentUpscaleModelLoader`
- `EmptyImage`
- `ImageScaleBy`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `GetImageSize`
- `MelBandRoFormerSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `LTXVPreprocess`
- `VAELoaderKJ`
- `VAELoader`
- `LTXVScheduler`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LTXVSetAudioVideoMaskByTime`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `ResizeImagesByLongerEdge`
- `MarkdownNote`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `RandomNoise`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `VRAM_Debug`
- `MelBandRoFormerModelLoader`
- `PreviewAudio`
- `MarkdownNote`
- `MarkdownNote`
- `DualCLIPLoaderGGUF`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `TrimAudioDuration`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（66/72）

**有卡**：`CFGGuider`、`TextGenerateLTX2Prompt`、`LatentUpscaleModelLoader`、`EmptyImage`、`ImageScaleBy`、`KSamplerSelect`、`VAELoader`、`CLIPTextEncode`、`GetImageSize`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`MelBandRoFormerSampler`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVPreprocess`、`VAELoaderKJ`、`LTXVScheduler`、`SolidMask`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`RandomNoise`、`LTXVImgToVideoInplace`、`VHS_VideoCombine`、`LTXVSetAudioVideoMaskByTime`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`ResizeImageMaskNode`、`SamplerCustomAdvanced`、`ManualSigmas`、`VAEDecodeTiled`、`VRAM_Debug`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`LoadImage`、`LoadAudio`、`TrimAudioDuration`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
