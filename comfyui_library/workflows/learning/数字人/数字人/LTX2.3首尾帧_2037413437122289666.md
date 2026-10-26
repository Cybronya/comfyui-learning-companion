---
key: 数字人/数字人/LTX2.3首尾帧_2037413437122289666.json
name: LTX2.3首尾帧_2037413437122289666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3首尾帧_2037413437122289666.json
hash: be05f8b2d52d2f6b
coverage: 0.851852
learned_at: 2026-10-26 01:56:14
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveBoolean, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, ResizeImageMaskNode, ResizeImagesByLongerEdge, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVPreprocess, LTXVEmptyLatentAudio, MarkdownNote, MarkdownNote, LTXVLatentUpsampler, VAELoaderKJ, VAELoaderKJ, UNETLoader, PrimitiveInt, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, CFGGuider, KSamplerSelect, LTXVCropGuides, VHS_VideoCombine, ComfyMathExpression, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, PrimitiveInt, LoadImage, LoraLoaderModelOnly, DualCLIPLoader, LatentUpscaleModelLoader, LTXVImgToVideoInplaceKJ, LoadImage, PrimitiveStringMultiline, LTXVImgToVideoInplace, MatAnyone, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3首尾帧_2037413437122289666.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3首尾帧_2037413437122289666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（54 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LTXVLatentUpsampler` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PrimitiveInt`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LTXVImgToVideoInplace`
- `MatAnyone`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`、`VAELoaderKJ`、`UNETLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVCropGuides`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVConditioning`、`LoadImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplaceKJ`、`LTXVImgToVideoInplace`、`MatAnyone`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
