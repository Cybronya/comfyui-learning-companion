---
key: 数字人/数字人/LTX-2.3-数字人_2063143281101459457.json
name: LTX-2.3-数字人_2063143281101459457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX-2.3-数字人_2063143281101459457.json
hash: 13c1e597756aab05
coverage: 0.545455
learned_at: 2026-10-26 01:55:44
nodes: [GetNode, GetNode, SimpleCalculatorKJ, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SamplerCustomAdvanced, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, ResizeImagesByLongerEdge, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, RandomNoise, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, SetNode, GetNode, GetNode, RandomNoise, KSamplerSelect, ManualSigmas, SetNode, ImageScaleBy, ImageResizeKJv2, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, GetImageSize, LTXVPreprocess, LTXVConcatAVLatent, LTXVConditioning, EmptyLTXVLatentVideo, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, LTXVImgToVideoInplaceKJ, Seed (rgthree), SetNode, SimpleCalculatorKJ, SetNode, SetNode, GetNode, GetNode, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, UNETLoader, INTConstant, CFGGuider, PrimitiveFloat, LoraLoaderModelOnly, LTXVScheduler, CLIPTextEncode, LTXVLatentUpsampler, LatentUpscaleModelLoader, INTConstant, INTConstant, LatentUpscaleModelLoader, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX-2.3-数字人_2063143281101459457.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX-2.3-数字人_2063143281101459457.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（99 个）：
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoInplaceKJ`
- `Seed (rgthree)`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `INTConstant`
- `CFGGuider`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `INTConstant`
- `INTConstant`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（54/99）

**有卡**：`SimpleCalculatorKJ`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`LTXVSeparateAVLatent`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`ImageScaleBy`、`LTXVPreprocess`、`GetImageSize`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTX2SamplingPreviewOverride`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplaceKJ`、`Seed (rgthree)`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`UNETLoader`、`INTConstant`、`LoraLoaderModelOnly`、`LTXVScheduler`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
