---
key: 视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json
name: LTX-2.3-首尾帧_2055556105299873793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json
hash: a381370a6d17e037
coverage: 0.517544
learned_at: 2026-10-15 22:37:57
nodes: [GetNode, GetNode, GetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetImageSize, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SimpleCalculatorKJ, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SamplerCustomAdvanced, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, KSamplerSelect, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, CLIPTextEncode, ResizeImagesByLongerEdge, GetNode, SetNode, SetNode, LTXVConditioning, GetNode, GetNode, LTXVSeparateAVLatent, CFGGuider, LTXVSeparateAVLatent, VHS_VideoCombine, SamplerCustomAdvanced, CFGGuider, SetNode, GetNode, GetNode, LTXVLatentUpsampler, ImageScaleBy, LTXVConcatAVLatent, Fast Groups Bypasser (rgthree), ImageScaleBy, ImageScaleBy, ImageConcatMulti, GetNode, GetNode, ImageScaleBy, ImageConcatMulti, GetNode, SetNode, VAEDecodeTiled, SetNode, GetNode, LTXVAudioVAEDecode, SetNode, GetNode, ResizeImagesByLongerEdge, RandomNoise, RandomNoise, LTXVPreprocess, LTXVPreprocess, ImageResizeKJv2, ImageResizeKJv2, LTXVImgToVideoInplaceKJ, LTXVScheduler, ManualSigmas, LTX2SamplingPreviewOverride, ManualSigmas, ManualSigmas, VAELoader, VAELoaderKJ, VHS_VideoCombine, PrimitiveFloat, INTConstant, LatentUpscaleModelLoader, ModelPatchTorchSettings, SetNode, LTXVChunkFeedForward, KSamplerSelect, INTConstant, INTConstant, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055556105299873793.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（114 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ResizeImagesByLongerEdge`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `LTXVConcatAVLatent`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleBy`
- `ImageScaleBy`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `RandomNoise`
- `RandomNoise`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplaceKJ`
- `LTXVScheduler`
- `ManualSigmas`
- `LTX2SamplingPreviewOverride`
- `ManualSigmas`
- `ManualSigmas`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `INTConstant`
- `LatentUpscaleModelLoader`
- `ModelPatchTorchSettings`
- `SetNode`
- `LTXVChunkFeedForward`
- `KSamplerSelect` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（59/114）

**有卡**：`SimpleCalculatorKJ`、`EmptyLTXVLatentVideo`、`GetImageSize`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`ResizeImagesByLongerEdge`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`CFGGuider`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`ImageScaleBy`、`ImageConcatMulti`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`RandomNoise`、`LTXVPreprocess`、`ImageResizeKJv2`、`LTXVImgToVideoInplaceKJ`、`LTXVScheduler`、`ManualSigmas`、`LTX2SamplingPreviewOverride`、`VAELoader`、`VAELoaderKJ`、`INTConstant`、`LatentUpscaleModelLoader`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
