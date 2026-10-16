---
key: 视频生成/图生视频/LTX-2.3首尾帧生成视频（极速版）_2045564251896553474.json
name: LTX-2.3首尾帧生成视频（极速版）_2045564251896553474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2045564251896553474.json
hash: f5268e90ce3d3c90
coverage: 0.5
learned_at: 2026-10-15 22:36:50
nodes: [KSamplerSelect, KSamplerSelect, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, SamplerCustomAdvanced, RandomNoise, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVLatentUpsampler, ImageScaleBy, GetImageSize, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, ResizeImagesByLongerEdge, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, GetNode, GetNode, SetNode, SetNode, GetNode, SimpleCalculatorKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, INTConstant, INTConstant, SimpleCalculatorKJ, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2_NAG, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ManualSigmas, ManualSigmas, LTXVImgToVideoInplaceKJ, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, LTX2SamplingPreviewOverride, ImageResizeKJv2, INTConstant, UNETLoader, VHS_VideoCombine, LoadImage, LoadImage, CLIPTextEncode, TextBox1]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3首尾帧生成视频（极速版）_2045564251896553474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045564251896553474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（98 个）：
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVImgToVideoInplaceKJ`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LTX2SamplingPreviewOverride`
- `ImageResizeKJv2`
- `INTConstant`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `TextBox1`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（49/98）

**有卡**：`KSamplerSelect`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`SimpleCalculatorKJ`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`INTConstant`、`LTX2_NAG`、`ManualSigmas`、`LTXVImgToVideoInplaceKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTX2SamplingPreviewOverride`、`UNETLoader`、`VHS_VideoCombine`、`LoadImage`、`TextBox1`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
