---
key: 视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json
name: LTX 2.3 多图首尾帧_2032460701406601217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json
hash: 144d4586a3c270eb
coverage: 0.898734
learned_at: 2026-10-11 03:16:44
nodes: [ImageScaleBy, SimpleCalculatorKJ, ImageScaleBy, ImageScaleBy, ImageConcatMulti, ImageConcatMulti, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, VHS_VideoCombine, PrimitiveFloat, SimpleCalculatorKJ, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, UnetLoaderGGUF, DualCLIPLoaderGGUF, LTXVChunkFeedForward, SamplerCustomAdvanced, SimpleCalculatorKJ, CLIPTextEncode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, CFGGuider, KSamplerSelect, ImageScaleBy, LTXVLatentUpsampler, MarkdownNote, LTXVImgToVideoInplace, LTXVConcatAVLatent, INTConstant, LTXVConditioning, KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, CFGGuider, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecodeTiled, ManualSigmas, ManualSigmas, RandomNoise, SamplerCustomAdvanced, LTXVScheduler, LTX2SamplingPreviewOverride, RandomNoise, LTXVConcatAVLatent, LTXVEmptyLatentAudio, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, ManualSigmas, ImageResizeKJv2, ImageResizeKJv2, ResizeImagesByLongerEdge, ImageResizeKJv2, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, CLIPTextEncode, INTConstant, INTConstant, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, VHS_VideoCombine, LTXVAddGuideMulti, ImageResizeKJv2, LTX2_NAG]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（79 个）：
- `ImageScaleBy`
- `SimpleCalculatorKJ`
- `ImageScaleBy`
- `ImageScaleBy`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `LTXVChunkFeedForward`
- `SamplerCustomAdvanced` ★核心
- `SimpleCalculatorKJ`
- `CLIPTextEncode` ★核心
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ImageScaleBy`
- `LTXVLatentUpsampler` ★核心
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `INTConstant`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `LTX2SamplingPreviewOverride`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `ManualSigmas`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LTXVAddGuideMulti`
- `ImageResizeKJv2`
- `LTX2_NAG`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（71/79）

**有卡**：`ImageScaleBy`、`SimpleCalculatorKJ`、`ImageConcatMulti`、`EmptyLTXVLatentVideo`、`GetImageSize`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`LTXVChunkFeedForward`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`ResizeImagesByLongerEdge`、`CFGGuider`、`KSamplerSelect`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`INTConstant`、`LTXVConditioning`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ManualSigmas`、`RandomNoise`、`LTXVScheduler`、`LTX2SamplingPreviewOverride`、`LTXVEmptyLatentAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`ImageResizeKJv2`、`LTXVPreprocess`、`LoadImage`、`LTXVAddGuideMulti`、`LTX2_NAG`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
